-- Extract the Month (month)

-- We use DATE_FORMAT(trans_date, '%Y-%m') to extract the year and month from trans_date in YYYY-MM format.
-- Count Total Transactions (trans_count)

-- COUNT(id) gives the total number of transactions for each month and country.
-- Count Approved Transactions (approved_count)

-- We use SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END), which:
-- Adds 1 for approved transactions.
-- Adds 0 for declined transactions.
-- The sum gives the total count of approved transactions.
-- Total Amount of Transactions (trans_total_amount)

-- SUM(amount) gives the total amount of all transactions in that month and country.
-- Total Amount of Approved Transactions (approved_total_amount)

-- SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END), which:
-- Adds transaction amount if it's approved.
-- Adds 0 if it's declined.
-- Group by month and country

-- We group the data by month and country to ensure the calculations are done per group.


SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(id) AS trans_count,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
