--select distinct, order by, where, limit, fetch, group by, having, join - inner - outer - left- tight - full - cross, union, intersect, except

select customer.first_name from customer

select first_name, last_name from customer

select first_name || ' ' || last_name from customer

select now()

select first_name, last_name as surname from customer

select first_name || ' ' || last_name as full_name from customer

select first_name, last_name from customer order by first_name asc

select first_name, last_name from customer order by first_name asc, last_name desc

select length(first_name) len, last_name from customer ORDER BY len DESC

select first_name, last_name from customer order by first_name NULLS LAST

select DISTINCT first_name from customer order by first_name DESC

select DISTINCT first_name, last_name from customer

select distinct film.rental_rate from film order by rental_rate desc

select distinct on (rental_rate) rental_rate from film order by rental_rate desc

select first_name, last_name from customer where first_name = 'MARY'

select first_name, last_name from customer where first_name = 'MARY' and last_name = 'SMITH'

select first_name, last_name from customer where first_name = 'MARY' or first_name = 'PATRICIA'

select first_name, last_name from customer where first_name in ('MARY', 'PATRICIA')

select first_name, last_name from customer where first_name like 'M%'

select first_name, length(first_name) name_lenth from customer where first_name like 'A%' and length(first_name) between 5 and 7 order by name_lenth

select first_name, last_name from customer where first_name like 'A%' and last_name <> 'Motley'

select title, length, rental_rate from film where length > 180 and rental_rate < 1

select title, length, rental_rate from film where rental_rate = 0.99 or rental_rate = 2.99

select film_id, title, release_year from film order by film_id limit 5

select film_id, title, release_year from film order by film_id limit 5 offset 3

select film_id, title, release_year from film order by rental_rate desc limit 10

select film.film_id, film.title from film order by title fetch first ROW ONLY

select film.film_id, film.title from film order by title fetch first 5 ROW ONLY

select film.film_id, film.title from film order by title offset 5 rows fetch next 5 rows only

select film.film_id, film.title from film where film_id in (1, 2, 3)

select actor.first_name, actor.last_name from actor where last_name in ('Allen', 'Chase', 'Davis') order by last_name

select payment.payment_id, payment.amount, payment.payment_date from payment where payment_date::date in ('2007-02-15', '2007-02-16')

select film.film_id, film.title from film where film_id not in (1, 2, 3)

select payment.payment_id, payment.amount from payment where payment_id between 17503 and 17505 order by payment_id

select payment.customer_id, payment.payment_date from payment where payment_date between '2007-02-15' and '2007-02-16' order by payment_date

select customer.first_name, customer.last_name from customer where first_name like 'A%' and last_name like '%e' order by first_name

select customer.first_name, customer.last_name from customer where first_name like '%er%'

select customer.first_name, customer.last_name from customer where first_name like '_her%'

--  ~~like ~~*ilike !~~ not like !~~* not ilike

-- SELECT * FROM t WHERE message LIKE '%10$%%' ESCAPE '$';  escapes the character

select address.address, address.address2 from address where address2 is null

select address.address, address.address2 from address where address2 is not null

select f.title from film as f order by f.title limit 5

SELECT
    customer.customer_id,
    customer.first_name,
    customer.last_name,
    payment.amount,
    payment.payment_date
FROM
    customer
        INNER JOIN payment ON payment.customer_id = customer.customer_id
ORDER BY
    payment.payment_date;

SELECT
    customer_id,
    first_name,
    last_name,
    amount,
    payment_date
FROM
    customer
        INNER JOIN payment USING(customer_id)
ORDER BY
    payment_date;

SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name customer_name,
    s.first_name || ' ' || s.last_name staff_name,
    p.amount,
    p.payment_date
FROM
    customer c
        INNER JOIN payment p USING(customer_id)
        INNER JOIN staff s USING(staff_id)
ORDER BY
    payment_date;

SELECT
    f.film_id,
    f.title,
    i.inventory_id
FROM
    film f
        LEFT JOIN inventory i ON i.film_id = f.film_id
ORDER BY
    i.inventory_id;

SELECT
    f.film_id,
    f.title,
    i.inventory_id
FROM
    film f
        LEFT JOIN inventory i USING (film_id)
WHERE
    i.inventory_id IS NULL
ORDER BY
    f.title;

SELECT
    f.film_id,
    f.title,
    i.inventory_id
FROM
    inventory i
        RIGHT JOIN film f USING(film_id)
WHERE i.inventory_id IS NULL
ORDER BY
    f.title;

SELECT
    f1.title,
    f2.title,
    f1.length
FROM
    film f1
        INNER JOIN film f2 ON f1.film_id > f2.film_id
        AND f1.length = f2.length;

SELECT
    f.film_id,
    f.title,
    i.inventory_id
FROM
    film f
        FULL OUTER JOIN inventory i USING (film_id)
WHERE
    i.inventory_id IS NULL
ORDER BY
    f.title;

-- SELECT *
-- FROM products
-- CROSS JOIN warehouses;
-- CARTESIAN PRODUCE ALL COMBINATION OF ROWS FROM TABLES

SELECT * from city natural join country
-- join on common column name

SELECT
    customer_id,
    SUM (amount)
FROM
    payment
GROUP BY
    customer_id
ORDER BY
    customer_id;

SELECT
    first_name || ' ' || last_name full_name,
    SUM (amount) amount
FROM
    payment
        INNER JOIN customer USING (customer_id)
GROUP BY
    customer.customer_id
ORDER BY
    amount DESC;

SELECT
    customer_id,
    staff_id,
    SUM(amount)
FROM
    payment
GROUP BY
    staff_id,
    customer_id
ORDER BY
    customer_id;

SELECT
    payment_date::date payment_date,
    SUM(amount) sum
FROM
    payment
GROUP BY
    payment_date::date
ORDER BY
    payment_date DESC;

SELECT
    customer_id,
    SUM (amount) amount
FROM
    payment
GROUP BY
    customer_id
HAVING
    SUM (amount) > 200
ORDER BY
    amount DESC;

select grouping(film.release_year) release_year,
       grouping(film.rating) rating,
       film.release_year,
       film.rating,
       count(film.rating)
from
    film
group by
    grouping sets ((release_year, rating), (release_year), (rating), ())

select address.district,
       address.city_id,
       count(postal_code)
from
    address
group by
    CUBE (district, city_id)  --rollup if we want  bi hierarchy
order by
    district,
    city_id


WITH action_films AS (
    SELECT
        f.title,
        f.length
    FROM
        film f
            INNER JOIN film_category fc USING (film_id)
            INNER JOIN category c USING(category_id)
    WHERE
        c.name = 'Action'
)
SELECT * FROM action_films;


WITH cte_rental AS (
    SELECT
        staff_id,
        COUNT(rental_id) rental_count
    FROM
        rental
    GROUP BY
        staff_id
)
SELECT
    s.staff_id,
    first_name,
    last_name,
    rental_count
FROM
    staff s
        INNER JOIN cte_rental USING (staff_id);


WITH film_stats AS (
    -- CTE 1: Calculate film statistics
    SELECT
        AVG(rental_rate) AS avg_rental_rate,
        MAX(length) AS max_length,
        MIN(length) AS min_length
    FROM film
),
     customer_stats AS (
         -- CTE 2: Calculate customer statistics
         SELECT
             COUNT(DISTINCT customer_id) AS total_customers,
             SUM(amount) AS total_payments
         FROM payment
     )
-- Main query using the CTEs
SELECT
    ROUND((SELECT avg_rental_rate FROM film_stats), 2) AS avg_film_rental_rate,
    (SELECT max_length FROM film_stats) AS max_film_length,
    (SELECT min_length FROM film_stats) AS min_film_length,
    (SELECT total_customers FROM customer_stats) AS total_customers,
    (SELECT total_payments FROM customer_stats) AS total_payments;