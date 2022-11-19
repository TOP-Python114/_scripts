select
	`city`.`Name` as 'City',
    count(*) as 'Languages'
  from `countrylanguage` as cl
  join `country`
    on cl.`CountryCode` = `country`.`Code`
  join `city`
    on `country`.`Code` = `city`.`CountryCode`
   and `city`.`Population` > 5000000
 group by `City`
having `Languages` < 5
