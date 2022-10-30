select * 
from `city` 
where `CountryCode` = 'RUS' 
order by `name`;


insert into `city`
	(`countrycode`, `name`, `district`, `population`)
values
	('RUS', 'Azov', 'Azov', 78760),
    ('RUS', 'Anapa', 'Anapa', 95873);


update `city` 
set
	`population` = 187111
where `id` = 3683;


delete from `city`
where `id` = 3766;
