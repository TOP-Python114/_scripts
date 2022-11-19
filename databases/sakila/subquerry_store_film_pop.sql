select
	s.store_id as sid,
    f.title as ft,
    count(*) as pop
  from film as f
  join inventory as i
    on f.film_id = i.film_id
  join rental as r
    on i.inventory_id = r.inventory_id
  join store as s
    on i.store_id = s.store_id
 group by sid, ft
--  order by pop desc
