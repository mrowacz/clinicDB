create database if not exists clinic;
use clinic;

drop table patients;

create table  patients (
    id int,
    name varchar(100),
    address varchar(50),
    pesel varchar(12),
    phone varchar (12)
);








