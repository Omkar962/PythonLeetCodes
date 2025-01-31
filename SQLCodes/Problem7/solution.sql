-- LEFT JOIN ensures that all visits are included, even if there is no matching transaction.
-- WHERE t.transaction_id IS NULL filters out visits that have transactions.
-- GROUP BY v.customer_id groups the remaining visits by customer.
-- COUNT(v.visit_id) counts the number of visits per customer without transactions.

SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
