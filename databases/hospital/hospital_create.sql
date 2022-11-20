drop database if exists `hospital`;

create database if not exists `hospital`;

use hospital;

create table if not exists `departments` (
	`id` tinyint unsigned not null auto_increment,
    `name` varchar(100) not null unique,
    constraint `PK_id` primary key(`id`),
    constraint `CH_departments_name` check (`name` <> '')
);

create table if not exists `doctors` (
	`id` smallint unsigned not null auto_increment,
    `name` varchar(50) not null,
    `surname` varchar(50) not null,
    `salary` decimal(8,2) not null,
    `premium` decimal(8,2) not null default 0,
	constraint `PK_id` primary key(`id`),
	constraint `CH_doctors_name` check (`name` <> ''),
	constraint `CH_doctors_surname` check (`surname` <> ''),
	constraint `CH_doctors_salary` check (`salary` > 0),
	constraint `CH_doctors_premium` check (`premium` >= 0)
);
