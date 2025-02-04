-- DATEDIFF('2019-07-27', activity_date) < 30 AND DATEDIFF('2019-07-27', activity_date) >= 0:

-- This condition ensures that the activity_date is within the last 30 days ending on 2019-07-27 inclusively.
-- The DATEDIFF('2019-07-27', activity_date) returns a positive value if activity_date is before 2019-07-27, and we check if it's less than 30 days to get the last 30 days.
-- COUNT(DISTINCT user_id): Counts the number of distinct users who were active on each day.

-- GROUP BY activity_date: Groups the result by activity_date to count active users for each day.


SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM 
    Activity
WHERE 
    DATEDIFF('2019-07-27', activity_date) < 30 AND DATEDIFF('2019-07-27', activity_date)>=0
GROUP BY 1