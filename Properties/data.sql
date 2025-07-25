CREATE DATABASE IF NOT EXISTS Biscuit Depot;
USE Biscuit Depot;


CREATE TABLE IF NOT EXISTS inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT INT ,
    price VARCHAR(50) NOT NULL ,
    quantity INT NOT NULL ,
    expiry DATE NOT INT ,
    batch_no VARCHAR(50) NOT NULL,
    subtype VARCHAR(50) NOT NULL
);

INSERT INFO inventory (name, price, quantity, expiry, batch_no, subtype)
VALUES 
('Cream crackers', 'NGN2000', 20, '2025-03-22', 'AD-678' , 'Cookies'),
('Fab', 'NGN4000', 50, ,'2025-09-12', 'GT-334', 'Cookies'),
('Munchkins', 'NGN2500', 23, '1965-08-15', 'EA-566', 'Cookies'),
('Oreos', 'NGN6700', 9, '2023-07-23', 'RG-223', 'Cookies');