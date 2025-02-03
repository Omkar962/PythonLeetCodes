-- Count the number of unique users (COUNT(DISTINCT r.user_id)) who registered in each contest.
-- Divide by the total number of users (SELECT COUNT(*) FROM Users) to calculate the percentage of users who participated in each contest.
-- Multiply by 100.0 to get the percentage instead of a fraction.
-- Use ROUND(..., 2) to round the percentage to two decimal places.
-- Group by contest_id to calculate the percentage for each contest separately.
-- Order the results:
-- By percentage in descending order (ORDER BY percentage DESC).
-- If percentages are the same, order by contest_id in ascending order (ORDER BY contest_id ASC).


SELECT 
    r.contest_id, 
    ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC;
