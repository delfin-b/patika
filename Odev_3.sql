select country from country
where country Ilike 'A%a';

select country from country 
where country ilike '%______%'  and country ilike '%n';

select title from film where title ilike '%t%t%t%t';

select title,length,rental_rate from film where (title like 'C%') 
and (length>90) and (rental_rate=2.99);