use CarRentalSystem;
create table Vehicle(vehicle_id int primary key,make varchar(255),model varchar(255),year int,
dailyrate decimal(10,2),status bit,passengercapacity int,enginecapacity int);

create table Customer(customer_id int primary key,firstname varchar(255),lastname varchar(255),email varchar(255),phonenumber text);

create table Lease(lease_id int primary key,vehicle_id int foreign key references Vehicle(vehicle_id)on delete cascade on update cascade,
customer_id int foreign key references Customer(customer_id)on delete cascade on update cascade ,startdate date,enddate date,type varchar(255));

create table Payment(payment_id int primary key,lease_id int foreign key references Lease(lease_id)on delete cascade on update cascade,
paymentdate date,amount int);


insert into Vehicle values(1,'Toyota','Camry',2022,50.00,1,4,1450);
insert into Vehicle values(2,'Honda','Civic',2023,45.00,1,7,1500),(3,'Ford','Focus',2022,48.00,0,4,1400),(4,'Nissan','Altima',2023,52.00,1,7,1200),
(5,'Chevrolet','Malibu',2022,49.00,0,7,1400);
insert into Vehicle values(6,'Hyundai','Sonata',2023,4900,0,7,1400),(7,'BMW','3Series',2023,60.00,1,7,2499),(8,'Mercedes','C-Class',2022,58.00,1,8,2599),
(9,'Audi','A4',2022,54.00,1,4,2500),(10,'Lexus','ES',2023,54.00,1,4,2500);
select * from Vehicle

alter table Customer alter column phonenumber varchar(255);
insert into Customer values(1,'John','Doe','johndoe@example.com','555-555-5555');
insert into Customer values(2,'Jane','Smith','janesmith@example.com','555-123-4567'),
(3,'Robert','Johnson','robert@example.com','555-789-1234'),(4,'Sarah','Brown','sarah@example.com','555-456-7890'),
(5,'David','Lee','david@example.com','555-987-6543'),(6,'Laura','Hall','laura@example.com','555-234-5678'),(7,'Michael','Davis','michael@example.com','555-876-5432'),
(8,'Emma','Wilson','emma@example.com','555-432-1098'),(9,'William','Taylor','wiiliam@example.com','555-321-6547'),
(10,'Olivia','Adams','olivia@example.com','555-765-4321');
select * from Customer;

insert into Lease values(1,1,1,'2023-01-01','2023-01-05','Daily');
insert into Lease values(2,2,2,'2023-02-15','2023-02-28','Monthly'),(3,3,3,'2023-03-10','2023-03-15','Daily'),
(4,4,4,'2023-04-20','2023-04-30','Monthly'),(5,5,5,'2023-05-05','2023-05-10','Daily'),(6,4,3,'2023-06-15','2023-06-30','Monthly'),
(7,7,7,'2023-07-01','2023-07-10','Daily'),(8,8,8,'2023-09-07','2023-09-10','Mothly'),
(9,3,3,'2023-09-07','2023-09-10','Daily'),(10,10,10,'2023-10-10','2023-10-31','Monthly');
select * from Lease;

insert into Payment values(1,1,'2023-01-03',200.00),(2,2,'2023-02-20',1000.00),(3,3,'2023-03-12',75.00),(4,4,'2023-04-25',900.00),(5,5,'2023-05-07',60.00),
(6,6,'2023-06-18',1200.00),(7,7,'2023-07-03',40.00),(8,8,'2023-08-14',1100.00),(9,9,'2023-09-09',80.00),(10,10,'2023-10-25',1500.00);
select * from Payment
--1
Update Vehicle set dailyrate=68 where make='Mercedes';
select * from Vehicle;
--2
delete from Customer where customer_id=7;
select * from Payment;
select* from Lease;
select*from Customer;
--3
EXEC sp_rename 'Payment.paymentDate', 'transactionDate';
select * from Payment;

--4
select customer_id,firstname,lastname,phonenumber from Customer where email='emma@example.com';

--5
select l.lease_id,v.vehicle_id,v.make,v.model,v.year,l.startdate,l.enddate,l.type from Lease l join Vehicle v
on l.vehicle_id=v.vehicle_id where l.customer_id=6 and getdate() between l.startdate and l.enddate;

--6
select p.* from Payment p join Lease l on p.lease_id=l.lease_id 
where l.customer_id=(select customer_id from Customer 
where phonenumber='555-555-5555');
--7
select avg(dailyrate) as 'Average daily rate for available cars' 
from Vehicle where status=1;
--8
select * from Vehicle where dailyrate=(select max(dailyrate) from Vehicle);

--9
select * from Vehicle v join Lease l on v.vehicle_id=l.vehicle_id join Customer c on
l.customer_id=c.customer_id where c.customer_id=4;

--10
SELECT TOP 1 l.*FROM Lease l
ORDER BY  l.StartDate DESC;
--11

select * from Payment where year(transactionDate)='2023';


--12
select * from Customer where customer_id not in (select l.customer_id from Lease l
 join Payment p on l.lease_id=p.lease_id);

 --13
select v.vehicle_id,v.make,v.model,v.year,v.dailyRate,v.status,v.passengerCapacity,v.engineCapacity,
sum(p.amount) AS TotalPayments from Vehicle v join Lease l ON v.vehicle_id = l.vehicle_id
join Payment p ON l.lease_id = p.lease_id group by v.vehicle_id,v.make,v.model,v.year,v.dailyRate, v.status,
v.passengerCapacity,v.engineCapacity;   

--14
select c.customer_id,c.firstname,c.lastname,SUM(p.amount) AS TotalPayments
from Customer c join Lease l ON c.customer_id = l.customer_id
join Payment p ON l.lease_id = p.lease_id group by c.customer_id, c.firstName, c.lastName
order by customer_id;

--15
select l.lease_id,v.vehicle_id,v.make,v.model,v.year,v.dailyRate,v.status,v.passengerCapacity,
v.engineCapacity,l.startDate,l.endDate,l.type from Lease l join Vehicle v on l.vehicle_id=v.vehicle_id;

--16
SELECT l.lease_id,c.firstName, c.lastName ,c.email,c.phoneNumber,v.make,
v.model,v.year,v.dailyRate,l.startDate,l.endDate, l.type
from Lease l
join Customer c on l.customer_id = c.customer_id
join Vehicle V ON L.vehicle_id = V.vehicle_id
where L.endDate >= GETDATE();

--17
SELECT top 1 c.customer_id, c.firstName, c.lastName,sum(p.amount) AS Mostly_spent_lease
from Customer C join Lease L ON C.customer_id = L.customer_id join
Payment p on l.lease_id = p.lease_id group by c.customer_id, c.firstName, c.lastName order by  Mostly_spent_lease desc;

--18
select v.*,l.lease_id,l.startDate,l.endDate,l.type ,c.*from Vehicle v
left join Lease l ON v.vehicle_id = l.vehicle_id left join
Customer c ON l.customer_id = c.customer_id where l.endDate >= GETDATE() 
order by v.vehicle_id;