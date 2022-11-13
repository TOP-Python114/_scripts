select
	`CountryCode` as 'Country code',
    count(*) as 'Number of cities',
    sum(`Population`) as 'Population'
  from `city`
 group by `CountryCode`
