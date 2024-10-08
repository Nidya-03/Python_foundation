use LoanManagementSystem;
CREATE TABLE Customer (
    customer_id INT IDENTITY(1,1) PRIMARY KEY ,
    name VARCHAR(50),
    email VARCHAR(60),
    phone_number VARCHAR(15),
    address VARCHAR(150),
    credit_score INT
);
CREATE TABLE Loan (
    loan_id INT IDENTITY(101,1) PRIMARY KEY ,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id) on DELETE CASCADE,
    principal_amount Decimal(10, 2),
    interest_rate INT,
    loan_term_months INT,
    loan_type VARCHAR(20),
    loan_status VARCHAR(20)    
);


INSERT INTO Customer (name, email , phone_number, address, credit_score) VALUES
	('Nidya Thirshala', 'nidya@gmail.com', '+91 8925048088', '123 Happy St, Villupuram', 830),
	('Raja', 'raja@gmail.com', '+91 6380681165', '456 Park Avenue, Villupram', 850),
	('Jaya', 'jaya@gmail.com', '+91 7094024076', '789 Diamond Road, Pondicherry', 900),
	('Megha', 'mega@gmail.com', '+91 94435049088', '11 Olive Garden, Chennai', 850),
	('Vicky', 'vicky@gmail.com', '+91 9489455173', '23 Sam Street, Banglore', 750),
	('Mithra', 'mithra@gmail.com', '+91 876875643', '57 Park Street, Cuddalore', 880),
	('Adhish', 'adhish@gmail.com', '+91 7094024398', '800 Hyung Avenue, Villupuram', 790),
	('Ashritha', 'ashritha@gmail.com', '+91 87654 32109', '345 Platinum Lane, Chennai', 900),
	('Maha', 'maha@gmail.com', '+91 78901 88348', '6 V Avenue, Vizag', 650),
	('Ziva', 'ziva@gmail.com', '+91 89012 83759', '12 Ghost Street, Chennai', 580);

INSERT INTO Loan (customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status) VALUES
	(7, 500000, 8, 36, 'CarLoan', 'Approved'),
	(1, 1000000, 7, 60, 'HomeLoan', 'Pending'),
	(5, 300000, 9, 24, 'CarLoan', 'Approved'),
	(6, 800000, 6, 48, 'HomeLoan', 'Approved'),
	(4, 700000, 8, 36, 'CarLoan', 'Approved'),
	(3, 1200000, 7, 60, 'HomeLoan', 'Pending'),
	(2, 400000, 9, 24, 'CarLoan', 'Approved'),
	(9, 900000, 6, 48, 'HomeLoan', 'Pending'),
	(8, 600000, 8, 36, 'CarLoan', 'Pending'),
	(10, 1100000, 7, 60, 'HomeLoan', 'Pending');

alter table Loan add property_value int null,property_address varchar(255) null,car_value int null,car_model varchar(255)null;
alter table Loan add no_emi int null;
EXEC sp_RENAME 'Loan.car_type', 'car_model', 'COLUMN'
select * from Customer;
select * from Loan
ALTER TABLE Loan ADD NoOfEMI INT DEFAULT 0;
