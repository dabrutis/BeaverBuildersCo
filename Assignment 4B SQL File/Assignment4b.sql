/* 
1.
*/
ALTER TABLE customer
ADD COLUMN PrimaryContact ENUM('Call', 'Text', 'Email') NOT NULL DEFAULT 'Email';
/* 
2.
*/
INSERT INTO customer (Location, Demographic, PurchaseFrequency, PrimaryContact)
VALUES ('159 Something Something Street', 'Beaver', '21', NULL);

INSERT INTO customer (Location, Demographic, PurchaseFrequency, PrimaryContact)
VALUES ('159 Something Something Street', 'Beaver', '21', "Email");
/* 
3.
*/
UPDATE customer
SET Demographic = "Human", PrimaryContact = "Text", Location = "260 Nothing Nothing Avenue", PurchaseFrequency = "5"
WHERE Location="159 Something Something Street";
/* 
4.
*/
DELETE FROM customer WHERE Location = "260 Nothing Nothing Avenue";
/* 
5.
*/
ALTER TABLE customer
ADD CustomerID int NOT NULL AUTO_INCREMENT primary key
/* 
6.
*/
ALTER TABLE employee ADD Status ENUM("Active","Inactive") NOT NULL DEFAULT "Inactive";