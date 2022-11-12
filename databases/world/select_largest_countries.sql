select 
	`Name`,
    `SurfaceArea`
  from `country`
 where `Name` <> 'Antarctica'
 order by `SurfaceArea` desc
 limit 5
