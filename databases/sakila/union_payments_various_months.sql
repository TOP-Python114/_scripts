select 
	p.payment_date,
    p.amount,
    concat(concat(c.last_name, ' '), c.first_name) as 'Name'
  from payment as p
  join customer as c
    on p.customer_id = c.customer_id
 where concat(concat(c.last_name, ' '), c.first_name) = 'BROWN ELIZABETH'
   and month(p.payment_date) = 5
union
select 
	p.payment_date,
    p.amount,
    concat(concat(c.last_name, ' '), c.first_name) as 'Name'
  from payment as p
  join customer as c
    on p.customer_id = c.customer_id
 where concat(concat(c.last_name, ' '), c.first_name) = 'BROWN ELIZABETH'
   and month(p.payment_date) = 8