-- Self-Join on recordDate

-- w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY) ensures that w1 represents the current day and w2 represents the previous day.
-- Compare Temperatures

-- w1.temperature > w2.temperature filters out only those records where today's temperature is higher than yesterday's.

SELECT w1.id 
FROM Weather w1
JOIN Weather w2 
ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature;
