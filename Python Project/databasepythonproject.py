import mysql.connector
from mysql.connector import errorcode

HOST1 = "127.0.0.1" #local host ip 1
HOST2 = "10.0.0.87" #local host ip 2

def print_choices():
    #Prints the menu options for every time the loop is initiated
    print("")
    print("Employee Sale System")
    print("*"*30)
    print("1. Inventory")
    print("2. Customers")
    print("3. View Orders")
    print("4. Place Orders")
    print("5. QUIT")
    print("*"*30)
    print("")

def query1():
    customer_cursor = cm_connection.cursor() #starts the cursor
    customer_query = ("SELECT * FROM products") #selects all columns from the products table

    customer_cursor.execute(customer_query) #executes the query

    for row in customer_cursor.fetchall():
        print("Product:{} ID:{} Cost:{} Stock:{}".format(row[0], row[1], row[2], row[3])) #formats and prints all the columns for each row

    customer_cursor.close() #closes the cursor

def query2():
    customer_cursor = cm_connection.cursor() #starts the cursor
    customer_query = ("SELECT * FROM customers") #selects all columns from the customers table

    customer_cursor.execute(customer_query) #executes the query

    for row in customer_cursor.fetchall():
        print("ID:{} Name:{} Account:{}".format(row[0], row[1], row[2])) #formats and prints all the columns for each row

    customer_cursor.close() #closes the cursor

def query3():
    customer_cursor = cm_connection.cursor() #starts the cursor
    customer_query = ("SELECT * FROM sales") #selects all columns from the sales table

    customer_cursor.execute(customer_query) #executes the query

    for row in customer_cursor.fetchall():
        print("ID:{} Account:{} Product:{} Quantity:{} Total:{} ".format(row[0], row[1], row[2], row[3], row[4])) #formats and prints all the columns for each row

    customer_cursor.close() #closes the cursor

def query4():
    cursor = cm_connection.cursor() #starts the cursor
    
    ID = input("Enter Customer ID: ") #input for employee to enter customer id
    Product = input("Enter Product ID: ") #input for employee to enter product id
    Amount = input("Enter Amount of Product: ")#input for employee to enter amount of item that the customer intends to buy
    
    query = "SELECT customerAccount FROM customers WHERE customerID = %s" #first query for finding the account associated to the customer ID
    cursor.execute(query, (ID,)) #executes the query, using ID for %s
    account = cursor.fetchone() #holds the tuple in the account variable

    if account: #checks if it exists
        account = account[0] #takes the single value from the queried object

    query = "SELECT Cost FROM products WHERE ProductID = %s" #second query for finding the cost associated to the product ID
    cursor.execute(query, (Product,))#executes the query, using Product for %s
    cost = cursor.fetchone() #holds the tuple in the cost variable

    if cost: #checks if it exists
        cost = cost[0] #takes the single value from the queried object

    total = float(Amount) * float(cost) #calculation for the total cost
    insert_query = "INSERT INTO sales (CustomerID, customerAccount, ProductName, Quantity, TotalCost) VALUES (%s, %s, %s, %s, %s)" #query to insert all the newly obtained values into the sales table
    cursor.execute(insert_query, (ID, account, Product, Amount, total)) #query is executed using the local variables
    cm_connection.commit() #commits changes to the database

    cursor.close() #closes the cursor
    
try:
    cm_connection = mysql.connector.connect(
        user="cs509",
        password="cs509pw",
        host=HOST1,
        database="nation")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: #used for if the user or password is not correct
        print("Invalid credentials") 
    elif err.errno == errorcode.ER_BAD_DB_ERROR: #used for if the database specified is not found
        print("Database not found")
    else:
        print("Cannot connect to database:", err) #used for any other reason that the program can not connect to the database

else:
    userInput = "none" #initial value for user
    while(userInput != '5'): #while user hasn't quit
        print_choices() #prints menu of choices every loop

        userInput = input("Enter your choice: ") #user input for choice

        if(userInput != '5'):
                if(userInput == '1'): #choice for looking at inventory
                    query1()
                elif(userInput == '2'): #choice for looking at customers
                    query2()
                elif(userInput == '3'): #choice for looking at sales
                    query3()
                elif(userInput == '4'): #choice for creating a new sale
                    query4()
                else:
                    print("~INVALID CHOICE!~") #if not one of the above choices, it would show this message
    print("Goodbye!") #prints this message for when the user quits the application
    cm_connection.close()
