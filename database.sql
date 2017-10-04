drop database clinic;
create database if not exists clinic;
use clinic;

create table  patients (
    id int not null auto_increment,
    name varchar(100),
    address varchar(100),
    pesel varchar(12),
    phone varchar(25),
    
    primary key(id)
);

create table specializations (
    id int not null auto_increment,
    spec text,
    primary key(id)
);

create table doctors (
    id int not null auto_increment,
    name varchar(100),
    address varchar(100),
    pesel varchar(12),
    phone varchar(25),
    specialization int,
    salary real,
    
    primary key(id),
    foreign key(specialization)
        references specializations(id)
);

create table visits (
    id int not null auto_increment,
    dt date,
    doctor int,
    patient int,
    disease varchar(100),
    medicaments text,
    
    primary key(id),
    foreign key(patient)
        references patients(id),
    foreign key(doctor)
        references doctors(id)
);


