-- Join Condition:

-- We join the Sales table (s) with the Product table (p) on the product_id column, which is common in both tables.
-- Select the Columns:

-- From the joined result, we select product_name from the Product table, and year and price from the Sales table.
-- Return the Result:

-- The result will contain the product_name, year, and price for each sale from the Sales table.

SELECT 
    p.product_name,
    s.year,
    s.price
FROM 
    Sales s
JOIN 
    Product p
ON 
    s.product_id = p.product_id;
