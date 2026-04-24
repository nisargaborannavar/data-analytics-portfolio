#Q1 Find athletes who have represented more than one country in the Olympics, and return all their competition records.

select  name,
    team AS country,
    games,
    sport,
    medal from olympic_games_athletes
where name IN (
SELECT name
    FROM olympic_games_athletes
    GROUP BY name
    HAVING COUNT(DISTINCT team) > 1
)
ORDER BY name, games;

#Q2How many unique users were active each day across both mobile and web platforms?
SELECT 
  log_date,
  COUNT(DISTINCT user_id) AS num_users
FROM (
    SELECT log_date, user_id FROM mobile_logs
    UNION
    SELECT log_date, user_id FROM web_logs
) AS combined
GROUP BY log_date;

#Q3 Which books generate the highest engagement (lifetime value), considering only books with more than 10 copies
WITH book_lifetime AS (
    SELECT 
        b.book_id,
        b.title,
        b.num_copies,
        SUM(c.return_date - c.checkout_date) AS lifetime_value
    FROM library_books b
    JOIN library_checkouts c
        ON b.book_id = c.book_id
    WHERE c.return_date IS NOT NULL
        AND b.num_copies > 10
    GROUP BY b.book_id, b.title, b.num_copies
),

ranked_books AS (
    SELECT *,
           DENSE_RANK() OVER (ORDER BY lifetime_value DESC) AS rnk
    FROM book_lifetime
)

SELECT 
    title,
    num_copies,
    lifetime_value
FROM ranked_books
WHERE rnk <= 3;