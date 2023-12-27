select distinct replacement_cost from film;

select count(distinct replacement_cost) from film;

select count(*) from film 
where title ilike 'T%' and rating='G';

select count (distinct country) from country
where country like '_____';

select count(*) from city
where city like 'R%' or city like '%r';