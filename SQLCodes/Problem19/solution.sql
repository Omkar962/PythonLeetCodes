-- Calculate Query Quality

-- The quality of a query is defined as the average of (rating / position).
-- AVG(rating * 1.0 / position) ensures floating-point division for accurate results.
-- ROUND(..., 2) rounds the result to two decimal places.
-- Calculate Poor Query Percentage

-- A query is "poor" if its rating < 3.
-- SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) counts poor queries per query_name.
-- COUNT(*) gets the total number of queries for that query_name.
-- We compute the percentage using (poor queries / total queries) * 100.
-- ROUND(..., 2) ensures the result is rounded to two decimal places.
-- Group by query_name to perform calculations for each unique query name.

SELECT 
    query_name, 
    ROUND(AVG(rating * 1.0 / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
