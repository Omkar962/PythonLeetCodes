-- Subquery (first_sales):
-- This subquery selects the product_id and the earliest year (MIN(year)) for each product_id from the Sales table. This represents the first year that each product was sold.
-- Main Query:
-- We join the Sales table (s) with the result of the subquery (first_sales) based on both product_id and the year being the first year for that product.
-- We then select the required columns: product_id, year (as first_year), quantity, and price.


SELECT 
    s.product_id, 
    s.year AS first_year,
    s.quantity,
    s.price
FROM 
    Sales s
JOIN 
    (SELECT product_id, MIN(year) AS first_year
     FROM Sales
     GROUP BY product_id) first_sales
ON 
    s.product_id = first_sales.product_id
    AND s.year = first_sales.first_year;
