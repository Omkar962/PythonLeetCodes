-- Find the First Order of Each Customer

-- We use a Common Table Expression (CTE) FirstOrders to get the earliest order_date for each customer_id.
-- Join with Original Table

-- We join Delivery with FirstOrders to get the full details of each customer's first order.
-- Calculate Immediate Order Percentage

-- Use CASE inside SUM to count the first orders where order_date = customer_pref_delivery_date (immediate orders).
-- Use COUNT(*) to get the total number of first orders.
-- Multiply by 100.0 to ensure floating point division.
-- Use ROUND(..., 2) to keep two decimal places.

SELECT 
    ROUND(
        100.0 * SUM(CASE 
                        WHEN d.order_date = d.customer_pref_delivery_date THEN 1 
                        ELSE 0 
                    END) 
        / COUNT(*), 2
    ) AS immediate_percentage
FROM Delivery d
JOIN FirstOrders f
ON d.customer_id = f.customer_id AND d.order_date = f.first_order_date;
