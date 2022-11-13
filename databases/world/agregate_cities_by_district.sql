select
	`CountryCode`,
    `District`,
    sum(`Population`) as 'Population by district'
  from `city`
 group by `CountryCode`, `District`
 order by `CountryCode`, `Population by district` desc
