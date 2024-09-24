use TicketBookingSystem;
create table Venu(venu_id int primary key,venu_name varchar(68),address varchar(25));

create table Event(event_id int primary key,event_name varchar(68),event_date date,event_time time,venu_id 
int foreign key references Venu(venu_id),total_seats int,available_seats int,
ticket_price decimal,event_type varchar(30));

create table Customer(customer_id int primary key,customer_name varchar(20),email varchar(20),phone_number varchar(255));

create table Booking(booking_id int primary key,customer_id int foreign key references customer(customer_id)
,event_id int foreign key references Event(event_id),
num_tickets int,total_cost decimal(10,2),booking_date date);

alter table Event add booking_id int;
alter table Event add foreign key (booking_id) references Booking(booking_id);

alter table Customer add booking_id int;
alter table Customer add foreign key(booking_id) references Booking(booking_id);


insert into Venu values(1,'Chepauk stadium','Chennai'),(2,'Nehru Stadium','Chennai'),(3,'United Center','Usa'),
(4,'The Forum','Usa'),(5,'Allianz Arrena','Germany'),(6,'Barclays center','Usa'),(7,'Tokyo Dome','Japan'),
(8,'Mercedes Benz Arena','China'),(9,'Olympic Stadium','Seoul'),(10,'Indoor Stadium','Singapore');
select * from Venu;

insert into Event(event_id, event_name, event_date, event_time, venu_id, 
total_seats, available_seats, ticket_price, event_type) values 
(1, 'FIFA World cup', '2024-10-02', '23:55:54', 1, 15000,4000, 2000.00, 'Sports');
INSERT INTO Event (event_id, event_name, event_date, event_time, venu_id, total_seats, available_seats, ticket_price, event_type)
VALUES(2, 'Coachella music', '2024-03-15', '20:00:00', 2, 5000, 5000, 290, 'Concert'),
(3, 'Lollapalooza', '2024-04-05', '19:30:00', 3, 800, 800, 4599, 'Movies'),
(4, 'Super bowl cup', '2024-03-01', '18:00:00', 4, 300, 250, 1099, 'Sports'),
(5, 'Berlin Film festival', '2024-07-15', '21:00:00', 5, 500, 500, 2999, 'Movies'),
(6, 'Cupa del ray', '2024-04-19', '17:30:00', 6, 820, 820, 4500, 'Sports'),
(7, 'Escobar festival', '2024-10-01', '22:00:00', 7, 700, 700, 100, 'Concert'),
(8, 'World cup of darts', '2024-11-17', '10:00:00', 8, 550, 550, 299, 'Sports'),
(9, 'The Voicecup', '2024-01-03', '19:30:00', 9, 1000, 1000, 450, 'Concert'),
(10, 'The cup and saucer', '2024-04-25', '21:30:00', 10, 600, 600, 1000, 'Movies');
select * from Event;



insert into Customer(customer_id,customer_name,email,phone_number) values(1,'Nidya','nidya@gmail.com','123456789');
insert into Customer(customer_id,customer_name,email,phone_number) values(2,'Thirshala','thrish@gmail.com','12389765'),
(3,'Raja','raja@gmail.com','789654322'),(4,'Mithra','mithra@gmail.com','555567843'),(5,'Maha','maha@gmail.com','5647658374'),
(6,'Jaya','jaya@gmail.com','4475683407'),(7,'Mala','mala@gmail.com','244798465'),(8,'Vicky','vicky@gmail.com','755837899'),
(9,'Sam','sam@gmail.com','7526764876'),(10,'Riya','riya@gmail.com','34786457988');
select * from Customer;

insert into Booking (booking_id,customer_id,event_id,num_tickets,total_cost,booking_date)values
(101,1,1,4,8000.00,'2024-08-02');
insert into Booking (booking_id,customer_id,event_id,num_tickets,total_cost,booking_date)values
(102,2,2,5,1450.00,'2024-01-02'),(103,3,3,7,32193.00,'2024-01-02');
insert into Booking (booking_id,customer_id,event_id,num_tickets,total_cost,booking_date)values
(104,4,4,6,6594.00,'2024-01-04'),(105,5,5,8,23992.00,'2024-04-02');
insert into Booking (booking_id,customer_id,event_id,num_tickets,total_cost,booking_date)values
(106,6,6,2,9000.00,'2024-01-19'),
(107,3,7,6,600.00,'2024-02-01');
insert into Booking (booking_id,customer_id,event_id,num_tickets,total_cost,booking_date)values
(108,8,4,9,9891.00,'2024-02-02'),(109,9,9,5,2250,'2024-01-01'),
(110,2,6,2,9000.00,'2024-03-01');
select * from Booking;
--task2--3
select * from Event where available_seats>0;
--4
select * from Event where event_name like '%cup%';
--5
select * from Event where ticket_price between 1000 and 2500;
--6
select * from Event where event_date >='2024-04-18' and event_date<='2024-08-15';
--7
select * from Event where available_seats>0 and event_type='Concert';
--8
select * from Customer order by customer_id offset 5 rows fetch next 5 rows only;
--9
select * from Booking where num_tickets>4;
--10
select * from Customer where phone_number like '%000';
--11
select * from Event where total_seats>15000 order by total_seats;
update Event set total_seats=18000 where event_id=3;
--12
select * from Event where event_name not like '[xyz]%';

--task3 1
select event_name,avg(ticket_price) as 'Average Price' from Event group by event_name;

--2
select event_id ,event_name,sum((total_seats-available_seats)*ticket_price) as 'Total Revenue' from Event
group by event_id,event_name;

--3
select top 1 e.event_id,e.event_name,sum(b.num_tickets ) as Highest_ticket_sales from Booking b
join Event e on b.event_id=e.event_id group by e.event_id,e.event_name order by Highest_ticket_sales desc;

--4
select e.event_id, e.event_name, sum(b.num_tickets) as total_tickets_sold
from Event e JOIN Booking b on e.event_id = b.event_id
group by e.event_id, e.event_name;


--5
select * from Event 
where event_id not in(select event_id from Booking);

--6
select top 1 c.customer_id, c.customer_name, sum(b.num_tickets) as booked_most_tickets
from Booking b
join Customer c on b.customer_id = c.customer_id
group by c.customer_id, c.customer_name
order by booked_most_tickets desc;

--7
select e.event_name,format(b.booking_date, 'MMMM') as event_month,
sum(b.num_tickets) as total_tickets_sold from  Booking b
join Event e on b.event_id = e.event_id group by e.event_name, format(b.booking_date, 'MMMM')
order by event_month, e.event_name;

--8
select v.venu_id,avg(e.ticket_price) as'Average ticket price' from Venu v join Event e on v.venu_id=e.venu_id 
group by v.venu_id;

--9
select e.event_type, sum(num_tickets) as 'Total tickets sold' from Booking b join Event e
on e.event_id=b.event_id group by e.event_type;

--10
select year(E.event_date) AS Event_Year,sum(B.total_cost) AS Total_Revenue
from Booking b JOIN Event e on b.event_id = e.event_id
group by year(e.event_date) order by Event_Year;

--11

select *  from Customer where customer_id in(select customer_id from Booking
 group by customer_id having count(customer_id)>1);

 --12
 select customer_id,event_id ,sum(total_cost) as 'Total Revenue' from Booking 
 group by customer_id,event_id order by 'Total Revenue' desc;

 --13
 select event_type,venu_id,avg(ticket_price) as 'Average ticket price' from Event
 group by event_type,venu_id order by event_type;

 --14

select c.customer_name, sum(b.num_tickets) as total_ticket_purchase
from customer c
join booking b
on c.customer_id = b.customer_id
where b.booking_date between dateadd(day, -30, getdate()) AND getdate()
group by c.customer_name;


update Booking set booking_date='2024-09-02' where booking_id=104;

--task4-1

select venu_id,avg(ticket_price) as 'Average Ticket price' from 
(select venu_id,ticket_price from Event) a group by venu_id;

--2
select * from Event where event_id in(select event_id from Event where 
available_seats=0 or (total_seats - available_seats)>=available_seats);

--3
select event_id ,event_name,total_seats -  available_seats as 'Tickets sold'
from Event order by event_id;

--4
select * from Customer c where not exists(select customer_id from Booking b
where b.customer_id=c.customer_id);

--5
select * from Event where event_id not in(select event_id from Event where total_seats!=available_seats);

--6
select event_type,Ticket_sold from(select event_type,(total_Seats-available_seats) as
Ticket_sold from Event)as a;

--7
select event_id,event_name,ticket_price from Event where ticket_price>(select avg(ticket_price)
from Event);

--8
select c.customer_id,c.customer_name,(select sum(e.ticket_price) from Event e where e.event_id in
(select b.event_id from Booking b where b.customer_id=c.customer_id)) as Total_Revenue from Customer c;

--9
select b.customer_id,c.customer_name from Booking b join Customer c on b.customer_id=c.customer_id
where event_id in(select event_id from Event e where e.venu_id=4);

--10
select event_type,Ticket_sold from(select event_type,sum(total_Seats-available_seats) as
Ticket_sold from Event e group by event_type)as e;

--11

select c.customer_id,c.customer_name,format(b.booking_date,'MM') as Booking_Montth from Customer c join
Booking b on c.customer_id=b.customer_id order by c.customer_id,format(b.booking_date,'MM');
--12
SELECT v.venu_name,(select avg(e.ticket_price)from Event e
WHERE e.venu_id = v.venu_id) as Average_ticket_price from Venu v;