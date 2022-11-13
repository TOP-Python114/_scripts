select
	`country`.`Name` as 'Country',
    `city`.`Name` as 'City'
  from `city` 
  join `country`
 order by `Country`, `City`
