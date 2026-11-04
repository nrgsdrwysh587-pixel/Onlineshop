CREATE DATABASE OnlineShop;
GO

USE OnlineShop;
GO

CREATE TABLE products (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100),
    price INT,
    category NVARCHAR(50)
);
GO

INSERT INTO products (name, price, category)
VALUES
(N'کفش اسپرت', 1500000, N'کفش'),
(N'کیف زنانه', 900000, N'کیف'),
(N'تی شرت', 500000, N'لباس');
GO
