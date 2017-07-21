create database shopjwlry;
use shopjwlry;

CREATE TABLE USERS (
    id_user int not null auto_increment,
name_us TEXT not null,
    surname TEXT not null,
    city TEXT not null,
    email TEXT not null,
    mobile INTEGER,
    primary key (Id_user)
    );
    describe users;

CREATE TABLE Login (
    id_user INT,
    login TEXT not null,
    pass TEXT not null,
    role text not null,
    foreign key (id_user) references USERS(id_user)
);
select* from login;
CREATE TABLE Products (
    id_product INT not null,
   category TEXT not null,
    karat TEXT not null,
   material TEXT not null,
    price INTEGER not null,
    promo_price INTEGER not null,
    quantity INTEGER not null,
    primary key (id_product)
);
describe Products;
CREATE TABLE Orders (
    order_nr INT not null auto_increment,
    id_user INT,
    id_product INTEGER,
    payment_status TEXT not null,
order_date DATE not null,
    user_comment TEXT,
    foreign key (id_user) references USERS (id_user),
    foreign key (id_product) references Products (id_product),
    primary key (order_nr)
);
describe Orders;
CREATE TABLE Payments (
    id_payment INTEGER,
    order_status TEXT,
    id_user INTEGER,
    order_nr INTEGER,
    payment_date DATE,
    foreign key (id_user) references USERS (id_user),
    foreign key (order_nr) references Orders (order_nr),
    primary key (id_payment)
);
insert into Users (name_us, surname, city, email, mobile) values 
( 'Adam', 'Kwiatkowski', 'Warszawa', 'akwiat@abc.pl', 123456789 ),
( 'Kamil', 'Gruszka', 'Wroclaw', 'kgruszka@def.pl', 123756489 ),
( 'Ryszard', 'Pietruszka', 'Krakow', 'rpietruszka@abc.pl', 321456789 ),
( 'Norbert', 'Kabaczek', 'Poznan', 'nkabaczek@def.pl', 125676789 ),
( 'Jacek', 'Pomidor', 'Katowice', 'jpomidor@abc.pl', 125678389 ),
( 'Michal', 'Ogorek', 'Warszawa', 'mogorek@def.pl', 123987659 ), 
( 'Anna', 'Truskawka', 'Krakow', 'atruskawka@def.pl', 987654321),
( 'Kasia', 'Morela', 'Lublin', 'kmorela@abc.pl', 978645312),
( 'Gabriela', 'Porzeczka','Warszawa','gporzeczka@def.pl', 456789234),
( 'Ewa', 'Len', 'Bialystok', 'elen@abc.pl', 234765983 ),
( 'Ewelina','Cebula','Opole','ecebula@def.pl9', 345789321),
( 'Admin', 'Admin', 'world', 'admin@shopjwlry.com', 102030405);
select * from Users; 
delete from users where id_user=19;
insert into login values
(1, 'adamkw', 'kotek123','user'),
(2, 'kamilgr','chomik456','user'),
(3, 'ryszardpi','swinka658','user'),
(4, 'norbertka','robak325','user'),
(5, 'jacekpo','pies983','user'),
(6, 'michalog','wrobel652','user'),
(7, 'annatr','mysz546','user'),
(8, 'kasiamo','mucha902','user'),
(9, 'gabrielapo','szczur379','user'),
(10, 'ewale','rys561','user'),
(11, 'ewelinace','bobr320','user'),
(12, 'admin', 'admin','admin');
select * from login; 
insert into Products values 
(1, 'ring', '0,15', 'silver', 750, 630, 15),
(2, 'ring ', '0,25', 'gold', 1030, 950, 30),
(3, 'ring ', '0,50', 'white_gold', 3500, 3150, 5),
(13, 'ring ', '0,36', 'gold ', 1800, 1690, 5),
(4, 'earrings', '0,25', 'white_gold' , 1200, 999, 0),
(5, 'earrings ', '0,20', 'gold ', 1005, 995, 7),
(6, 'earrings', '0,55', 'white_gold', 4000, 3850, 3),
(14, 'earrings ', '0,15', 'silver ', 1100, 1010, 8),
(7, 'bracelets', '0,65', 'white_gold', 6900, 5500, 2),
(8, 'bracelets ', '0,55', 'white_gold', 6000, 5050, 5),
(9, 'bracelets ', '0,35', 'gold ', 1999, 1699, 1),
(10, 'necklaces', '0,10', 'silver ', 660, 599, 6),
(11, 'necklaces ', '0,35', 'gold ', 1700, 1550, 11),
(12, 'necklaces ', '0,40', 'white_gold', 1960, 1870, 3);
select * from Products;

insert into Orders (id_user, id_product, payment_status, order_date, user_comment) values
(5,9, 'awaiting cheque payment', '2017-05-20', 'prosze zapakowac na prezent'),
(11,1, 'delivered', '2017-03-12',NULL),
(5,12, 'cancelled', '2017-04-20', 'pomylka, prosba o anulowanie zamowienia'),
(2,11, 'awaiting cheque payment', '2017-05-22', 'prosze zapakowac na prezent'),
(4,10, 'shipped', '2017-05-19', 'prosze o ekspresowa wysylke'),
(1,9, 'awaiting cheque payment', '2017-05-24', 'prosze zapakowac na prezent'),
(8,8, 'delivered', '2017-02-20', null),
(3,7, 'awaiting cheque payment', '2017-05-26', 'prosze zapakowac na prezent'),
(10,6, 'cancelled', '2017-04-04','zona sie rozmyslila'),
(11,5, 'shipped', '2017-05-21', null),
(5,4, 'delivered', '2017-05-02', null),
(11,8, 'delivered', '2017-04-20', null),
(2,3, 'awaiting cheque payment', '2017-05-15', 'prosze dolaczyc fakture'),
(6,2, 'delivered', '2017-05-20', null),
(5,1, 'shipped', '2017-04-06', 'prosze o kontakt telefoniczny gdy przesylka zostanie wyslana'),
(11,12, 'awaiting cheque payment', '2017-05-02',NULL),
(1,11, 'awaiting cheque payment', '2017-05-12', 'prosze zapakowac na prezent'),
(7,10, 'cancelled', '2017-01-31', null),
(10,9, 'delivered', '2017-02-18', 'prosze dolaczyc fakture'),
(9,8, 'shipped', '2017-05-11', null),
(8,7, 'awaiting cheque payment', '2017-04-20', 'prosze zapakowac na prezent');
select * from Orders;
SELECT 
    order_nr,
    payment_status,
    order_date,
    ADDDATE(order_date,
        INTERVAL 21 DAY) AS 'payment ddl'
FROM
    orders;

SELECT 
    *
FROM
   USERS
        NATURAL RIGHT JOIN
    login
        NATURAL LEFT JOIN
orders
        NATURAL LEFT JOIN
    products
        NATURAL LEFT JOIN
    payments;

CREATE VIEW users_orders AS
    SELECT 
        id_user, name_us, surname, id_product, order_nr ,category, price
    FROM
        users
            NATURAL LEFT JOIN
        orders
            NATURAL LEFT JOIN
        products;
    
	select * from users_orders;
  
    drop view users_orders;
