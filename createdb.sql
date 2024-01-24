create table customers{
    id int primary key,
    name varchar(255),
    email varchar(255),
    phone varchar(255),
    password varchar(255),
}

create table canteen{
    id int primary key,
    name varchar(255),
    phone varchar(255),
}

create table canteen_admin{
    id int primary key,
    name varchar(255),
    phone varchar(255),
    password varchar(255),
    canteen_id int,
    foreign key (canteen_id) references canteen(id),
}

create table Prepared_dishes{
    id int primary key,
    name varchar(255),
    price int,
    stock_present int,
    canteen_id int,
    foreign key (canteen_id) references canteen(id),
}

create table dishes_to_be_prepared{
    id int primary key,
    name varchar(255),
    prep_time_inmins int,
    inc_factor float,
    price int,
    stock_present int,
    canteen_id int,
    foreign key (canteen_id) references canteen(id),
}


create table payment{
    id int primary key,
    customer_id int,
    amount int,
    time timestamp, 
    foreign key (customer_id) references customers(id),
}

create table orders{
    id int primary key,
    customer_id int,
    dish_id int,
    quantity int,
    payment_id int,
    status varchar(255),
    foreign key (customer_id) references customers(id),
    foreign key (dish_id) references dishes_to_be_prepared(id)or Prepared_dishes(id),
    foreign key (payment_id) references payment(id),
}   

INSERT INTO customers (id, name, email, phone, password) VALUES (1, 'Rahul','rahul.students@iiit.ac.in','1234567890','1234567890');
INSERT INTO customers (id, name, email, phone, password) VALUES (2, 'rohan','rohan.students@iiit.ac.in','1234567891','1234567891');
INSERT INTO customers (id, name, email, phone, password) VALUES (3, 'rohit','rohit.students@iiit.ac.in','1234567892','1234567892');
INSERT INTO customers (id, name, email, phone, password) VALUES (4, 'ram','ram.students@iiit.ac.in','1234567892','1234567892');

INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (1, 'Pizza', 100, 10,5);
INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (2, 'Burger', 50, 20,5);
INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (3, 'Sandwich', 30, 25,5);
INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (4, 'Samosa', 15, 50,5);
INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (5, 'Idli', 60, 40,4);
INSERT into Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (6, 'Vada', 70, 40,6);
INSERT into Prepared_dishes(id, name, price, stock_present,canteen_id) VALUES (7, 'Ice-cream', 25, 40,2);
INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (8, 'Pizza', 110, 10,2);
INSERT INTO Prepared_dishes (id, name, price, stock_present,canteen_id) VALUES (9, 'Burger', 60, 20,2);

INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (1, 'dosa', 6, 1.33, 50, 10,4);
INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (2, 'puri', 5, 2, 15, 10,1);
INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (3, 'chapati',2, 2, 11, 10,1);
INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (4, 'rice', 8, 2, 20, 10,1);
INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (5, 'Mango juice', 4, 1.5, 40, 20,3);
INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (6, 'Mango juice', 3, 1.5, 50, 20,6);
INSERT INTO dishes_to_be_prepared (id, name, prep_time_inmins, inc_factor, price, stock_present,canteen_id) VALUES (7, 'Maggi', 5, 1.3, 40, 30,4);


INSERT INTO canteen (id, name, phone) VALUES (1, 'Tantra', '1234567890');
INSERT INTO canteen (id, name, phone) VALUES (2, 'David', '1234567892');
INSERT INTO canteen (id, name, phone) VALUES (3, 'JC', '1234567891');
INSERT INTO canteen (id, name, phone) VALUES (4, 'BBC', '1234567893');
INSERT INTO canteen (id, name, phone) VALUES (5, 'VC', '1234567894');
INSERT INTO canteen (id, name, phone) VALUES (6, 'VC Juice', '1234567895');

