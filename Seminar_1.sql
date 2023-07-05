CREATE DATABASE IF NOT EXISTS Seminar_1;
USE Seminar_1;
DROP TABLE IF EXISTS Product;
CREATE TABLE IF NOT EXISTS Product
(Id INT PRIMARY KEY AUTO_INCREMENT,
ProductName VARCHAR(20) NOT NULL,
Manufacturer VARCHAR(20) NOT NULL,
ProductCount INT,
Price INT NOT NULL 
);
INSERT Product (ProductName, Manufacturer, ProductCount, Price)
VALUES
     ('iPhone X', 'Apple', 3, 76000),
     ('iPhone 8', 'Apple', 2, 51000),
     ('Galaxy S9', 'Samsung', 2, 56000),
     ('Galaxy S8', 'Samsung', 1, 41000),
     ('P20', 'Huawei', 5, 36000);
SELECT ProductName, Manufacturer, Price 
FROM Product
WHERE ProductCount > 2;
SELECT ProductName
FROM Product
WHERE Manufacturer = 'Samsung';
SELECT * FROM Product
WHERE ProductCount*Price > 100000 AND ProductCount*Price < 145000;
SELECT * FROM Product
WHERE ProductName LIKE 'iPhone%';
SELECT * FROM Product
WHERE ProductName LIKE 'Galaxy%';
SELECT * FROM Product
WHERE ProductName RLIKE '[0-9]';
SELECT * FROM Product
WHERE ProductName LIKE '%8%';