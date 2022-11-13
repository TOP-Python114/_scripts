select
	c.`Name` as 'Country',
    cl.`Language` as 'Language',
    cl.`Percentage`
  from `countrylanguage` as cl
  join `country` as c
    on cl.`CountryCode` = c.`Code` and c.`Code` = 'RUS'
 order by `Country`, cl.`Percentage` desc
