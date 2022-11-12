select
	`CountryCode`,
    `Name`,
    `Population`
  from `city`
 where `Population` > 1000000
 order by `Population` desc
