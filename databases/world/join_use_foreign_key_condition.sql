select
	`country`.`Name` as 'Country',
    `city`.`Name` as 'City'
  from `city`
  join `country`
    on `city`.`CountryCode` = `country`.`Code`
 order by `Country`, `City`
