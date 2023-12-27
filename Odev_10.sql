--select city.city, country.country
--from city
--left join country
--on city.country_id=country.country_id;

--select payment.payment_id, customer.first_name, customer.last_name
--from payment
--right join customer
--on payment.customer_id=customer.customer_id;

select rental.rental_id, customer.first_name, customer.last_name
from customer
full outer join rental
on rental.customer_id=customer.customer_id;