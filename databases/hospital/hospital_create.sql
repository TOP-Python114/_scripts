drop database if exists `hospital`;

create database if not exists `hospital`;

use hospital;

create table if not exists `departments` (
	`id` tinyint unsigned not null auto_increment,
    `name` varchar(100) not null unique,
    constraint `PK_id` primary key (`id`),
    constraint `CH_departments_name` check (`name` <> '')
);

create table if not exists `wards` (
	`id` mediumint unsigned not null auto_increment,
    `name` varchar(20) not null unique,
    `department_id` tinyint unsigned not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_wards_name` check (`name` <> '')
);
alter table `wards`
	add constraint `FK_wards_department_id`
	   foreign key (`department_id`) references `departments` (`id`);


create table if not exists `doctors` (
	`id` smallint unsigned not null auto_increment,
    `name` varchar(50) not null,
    `surname` varchar(50) not null,
    `salary` decimal(8,2) not null,
    `premium` decimal(8,2) not null default 0,
	constraint `PK_id` primary key (`id`),
	constraint `CH_doctors_name` check (`name` <> ''),
	constraint `CH_doctors_surname` check (`surname` <> ''),
	constraint `CH_doctors_salary` check (`salary` > 0),
	constraint `CH_doctors_premium` check (`premium` >= 0)
);

create table if not exists `specializations` (
	`id` smallint unsigned not null auto_increment,
    `name` varchar(100) not null unique,
    constraint `PK_id` primary key (`id`),
    constraint `CH_specializations_name` check (`name` <> '')
);

create table if not exists `doctors_specializations` (
	`id` int unsigned not null auto_increment,
	`doctor_id` smallint unsigned not null,
	`specialization_id` smallint unsigned not null,
    constraint `PK_id` primary key (`id`)
);
alter table `doctors_specializations`
	add constraint `FK_doctors_specializations_doctor_id`
	   foreign key (`doctor_id`) references `doctors` (`id`);
alter table `doctors_specializations`
	add constraint `FK_doctors_specializations_specialization_id`
	   foreign key (`specialization_id`) references `specializations` (`id`);


create table if not exists `vacations` (
	`id` int unsigned not null auto_increment,
    `start_date` date not null,
    `end_date` date not null,
    `doctor_id` smallint unsigned not null,
	constraint `PK_id` primary key (`id`),
    constraint `CH_vacations_end_date` check (`end_date` > `start_date`)
);
alter table `vacations`
	add constraint `FK_vacations_doctor_id`
       foreign key (`doctor_id`) references `doctors` (`id`);


create table if not exists `sponsors` (
	`id` smallint unsigned not null auto_increment,
    `name` varchar(100) not null unique,
    constraint `PK_id` primary key (`id`),
    constraint `CH_sponsors_name` check (`name` <> '')
);

create table if not exists `donations` (
	`id` int unsigned not null auto_increment,
    `amount` decimal(11,2) not null,
    `date` date not null,
    `department_id` tinyint unsigned not null,
    `sponsor_id` smallint unsigned not null,
    constraint `PK_id` primary key (`id`),
    constraint `CH_donations_amount` check (`amount` >= 0)
);
alter table `donations`
	add constraint `FK_donations_department_id`
       foreign key (`department_id`) references `departments` (`id`);
alter table `donations`
	add constraint `FK_donations_sponsor_id`
       foreign key (`sponsor_id`) references `sponsors` (`id`);


drop trigger if exists `TG_INSERT_donations_date`;

delimiter $$
create trigger `TG_INSERT_donations_date`
before insert
on `donations` 
for each row
begin
	if (new.`date` > curdate()) then 
		signal 
			sqlstate '45001' 
            set message_text = 'date should be less than current date';
    end if;
end$$
