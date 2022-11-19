select
	subq.cN as 'City',
    count(*) as 'Languages'
  from `country`
  join `countrylanguage` as cl
    on `country`.`Code` = cl.`CountryCode`
  join (select
			`city`.`Name` as cN,
            `country`.`Code` as cC
		  from `city`
		  join `country`
			on `city`.`CountryCode` = `country`.`Code`
		   and `city`.`Population` > 5000000) as subq
	on `country`.`Code` = subq.cC
 group by `City`
having `Languages` < 5
