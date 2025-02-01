-- IF(COUNT(c.user_id) = 0, 0, ...): This ensures that if there are no confirmation requests for a user (i.e., COUNT(c.user_id) is 0), the confirmation rate will be 0 instead of NULL.

-- SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END): This counts the number of 'confirmed' actions for each user.

-- COUNT(c.user_id): This counts the total number of confirmation requests for each user.

-- ROUND(..., 2): Finally, it rounds the confirmation rate to two decimal places.

SELECT s.user_id,
       ROUND(
           IF(COUNT(c.user_id) = 0, 0, 
              SUM(CASE WHEN c.action = 'confirmed' THEN 1 ELSE 0 END) / COUNT(c.user_id)
           ), 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id;
