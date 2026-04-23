#1. Heart Reactions on Posts
Find all posts which were reacted to with a heart 

FROM facebook_posts p
JOIN facebook_reactions r
    ON p.post_id = r.post_id
WHERE r.reaction = 'heart';

#2. Oscar Nominations Count
Count how many movies Abigail Breslin was nominated for at the Oscars


select  count(movie) from oscar_nominees
where nominee = 'Abigail Breslin';


#3. Wine Description Filter
Find all wineries whose wine descriptions mention plum, cherry, rose, or hazelnut (but not their plural forms)

SELECT DISTINCT winery
FROM winemag_p1
WHERE
  description ILIKE '%plum%'
  OR description ILIKE '%cherry%'
  OR description ILIKE '%rose%'
  OR description ILIKE '%hazelnut%'
  AND description NOT ILIKE '%plums%'
  AND description NOT ILIKE '%cherries%'
  AND description NOT ILIKE '%roses%'
  AND description NOT ILIKE '%hazelnuts%';

#4. Facebook Comments Count
Find total comments per user between Jan 12 and Feb 10, 2020 — only users with at least 1 comment

  SELECT
  user_id,
  SUM(number_of_comments) AS total_comments
FROM fb_comments_count
WHERE created_at BETWEEN '2020-01-12' AND '2020-02-10'
GROUP BY user_id
HAVING SUM(number_of_comments) > 0;


#5.Customer Order Totals
Find total order cost per customer, sorted alphabetically by first name

SELECT
  c.id,
  c.first_name,
  SUM(o.total_order_cost) AS total_order_cost
FROM customers c
JOIN orders o ON c.id = o.cust_id
GROUP BY c.id, c.first_name
ORDER BY c.first_name ASC;