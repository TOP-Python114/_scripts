insert into `departments`
	(`name`)
values
	('Глазная хирургия');

insert into `sponsors`
	(`name`)
values
	('Фонд \"Круг добра\"');

insert into `donations`
	(`amount`, `date`, `department_id`, `sponsor_id`)
values
	(224108.50, '2022-10-01', 1, 1);

insert into `donations`
	(`amount`, `date`, `department_id`, `sponsor_id`)
values
	(224108.50, '2023-12-01', 1, 1);

insert into `donations`
	(`amount`, `date`, `department_id`, `sponsor_id`)
values
	(-100.00, '2021-05-09', 1, 1);
