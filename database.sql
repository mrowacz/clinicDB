drop database clinic;
create database if not exists clinic;

use clinic;
drop table if exists patients;
drop table if exists doctors;
drop table if exists visits;
drop table if exists examinations;

create table  patients (
    id int not null,
    name varchar(100),
    address varchar(50),
    pesel varchar(12),
    phone varchar (12),
    
    primary key(id)
);

create table doctors (
    id int not null,
    specialization int,
    name varchar(100),
    address varchar(50),
    pesel varchar(12),
    phone varchar (12),
    salary real,
    
    primary key(id)
);

create table visits (
    id int not null,
    dt date,
    doctor int,
    patient int,
    disease varchar(100),
    medicaments text,
    examinations text,
    
    primary key(id),
    foreign key(doctor)
        references doctors(id)
);

create table examinations (
    id int not null,
    extype text,
    description text,
    doc_opinion text,
    patient int,
    doctor int,
    done boolean,
    commented boolean,
    
    primary key(id)
);



