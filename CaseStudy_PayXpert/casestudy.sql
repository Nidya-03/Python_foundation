use PayXpert;
create table Employee(employee_id int primary key identity(1,1),Firstname nvarchar(255) not null,Lastname nvarchar(255) not null,
Dateofbirth date,Gender nvarchar(255),Email  nvarchar(255) not null unique,Phonenumber nvarchar(25) not null,Address nvarchar(255) not null,
Position nvarchar(25) not null,Joiningdate date not null,Terminationdate date null);

create table Payroll(Payroll_id int primary key identity(101,1),employee_id int foreign key(employee_id) references Employee(employee_id)
,PayPeriodStartDate date,PayPeriodEndDate date,Basicsalary decimal(10,2),OvertimePay decimal(10,2)
,Deductions decimal(10,2),Netsalary as(Basicsalary+OvertimePay-Deductions)persisted);

create table Tax(tax_id int primary key identity(201,1),employee_id int foreign key references Employee(employee_id),Taxyear int,
TaxableIncome decimal(10,2),TaxAmount decimal(10,2));

create table FinancialRecord(record_id int primary key identity(301,1),employee_id int foreign key references Employee(employee_id),
Recorddate date not null,Description nvarchar(255) ,Amount decimal(10,2)not null,Recordtype nvarchar(255) not null);

insert into Employee(Firstname,Lastname,Dateofbirth,Gender,Email,Phonenumber,Address,Position,Joiningdate,Terminationdate)values
('Nidya','Thirshala','2003-04-18','Female','nidya@gmail.com','892504989','Chennai','Trainee','2023-09-12','2026-09-12'),
('Jaya','Mala','2002-07-12','Female','jaya@gmail.com','7094035067','Chennai','Teacher','2023-08-07','2025-08-07'),
('Mega','Nathan','1998-04-13','Male','mega@gmail.com','9443908865','Villupuram','Engineer','2016-09-08','2024-09-08'),
('Vicky','Trevor','2004-09-08','Male','vicky@gmail.com','9349514173','Pondy','Tester','2022-04-09','2027-04-09'),
('Victor','Raja','2002-09-14','Male','raja@gmail.com','8382992445','Pondy','Data Engineer','2023-08-06','2028-08-06'),
('Sam','Mithra','1999-09-02','Female','mithra@gmail.com','729028095','Chennai','Trainee','2020-09-08','2027-09-08'),
('Maha','Lakshmi','2001-06-04','Female','maha@gmail.com','8968978735','Coimabtore','Content Writer','2021-09-02','2024-09-02'),
('Pooja','Hegde','1997-09-02','Female','pooja@gmail.com','9890743556','Coimbatore','Doctor','2017-04-06','2026-04-06'),
('Joseph','Vijay','1999-09-15','Male','joseph@gmail.com','8983756875','Pondy','Software Engineer','2020-08-09','2024-08-09'),
('Vijay','Sethupathi','2000-07-19','Male','vijay@gmail.com','9748549363','Villupuram','Trainee','2024-09-27','2030-09-27');

insert into Payroll(employee_id,PayPeriodStartDate,PayPeriodEndDate,Basicsalary,OvertimePay,Deductions) values
(1,'2023-09-12','2026-09-12',50000.00,5000.00,2000.00),
(2,'2023-08-07','2025-08-07',45000.00,4000.00,1500.00),
(3,'2016-09-08','2024-09-08',60000.00,3000.00,2500.00),
(4,'2022-04-09','2027-04-09',50000.00,2000.00,1200.00),
(5,'2023-08-06','2028-08-06',48000.00,3000.00,2800.00),
(6,'2020-09-08','2027-09-08',55000.00,4000.00,2000.00),
(7,'2021-09-02','2024-09-02',35000.00,2000.00,1000.00),
(8,'2017-04-06','2026-04-06',45000.00,2500.00,1000.00),
(9,'2020-08-09','2024-08-09',68000.00,1300.00,700.00),
(10,'2024-09-27','2030-09-27',70000.00,3000.00,2300.00);
select * from Payroll

insert into Tax(employee_id,Taxyear,TaxableIncome,TaxAmount) values
(1,'2024',500000.00,25000.00),
(2,'2024',450000.00,20000.00),
(3,'2022',600000.00,60000.00),
(4,'2023',500000.00,25000.00),
(2,'2024',500000.00,25000.00),
(5,'2022',600000.00,30000.00),
(6,'2023',400000.00,20000.00),
(2,'2020',500000.00,22000.00),
(1,'2022',700000.00,29000.00),
(10,'2026',700000.00,25000.00);
select * from Tax

insert into FinancialRecord(employee_id,Recorddate,Description,Amount,Recordtype) values
(1,'2023-09-12','Record of Income',500000.00,'Income'),
(2,'2024-08-07','Record of Tax',450000.00,'Tax'),
(3,'2020-09-08','Record of Expense',300000.00,'Expense'),
(4,'2022-04-09','Record of Income',500000.00,'Income'),
(5,'2024-03-09','Record of Tax',500000.00,'Tax'),
(6,'2023-09-08','Record of Expense',50000.00,'Expense'),
(7,'2017-04-06','Record of Income',450000.00,'Income'),
(8,'2020-07-09','Record of Tax',29000.00,'Tax'),
(9,'2023-08-09','Record of Expense',65000.00,'Expense'),
(10,'2024-09-27','Record of Income',700000.00,'Income');

SELECT * FROM Tax WHERE employee_id = 2 and Taxyear=2024