select 
	store_film_pop.sid,
    store_film_pop.ft,
    store_pop.max_pop
  from (select
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
		 group by sid, ft) as store_film_pop
  join (select
			store_film_pop.sid as sid,
			max(store_film_pop.pop) as max_pop
		  from (select
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
				 group by s.store_id, f.title) as store_film_pop
		 group by store_film_pop.sid) as store_pop
	 on store_film_pop.sid = store_pop.sid 
	and store_film_pop.pop = store_pop.max_pop