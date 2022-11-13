select
	`Continent`,
    count(*) as `Countries`,
	avg(`LifeExpectancy`) as `Average life`
  from `country`
 group by `Continent`
 order by `Average life`
