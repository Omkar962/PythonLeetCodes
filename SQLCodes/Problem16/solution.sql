-- Correct Join Condition: It joins Prices and UnitsSold on product_id, while also ensuring that purchase_date falls within the price validity period (start_date to end_date).
-- Correct Revenue Calculation: It calculates total revenue as SUM(p.price * u.units).
-- Correct Average Price Calculation: It divides total revenue by total units sold and rounds it to two decimal places.
-- Handles Missing Sales: Uses IFNULL(..., 0) to return 0 when a product has no sales.



-- Joins Prices with UnitsSold using product_id and purchase_date range.
-- Calculates total revenue as SUM(price * units).
-- Calculates total units sold as SUM(units).
-- Computes average price as total revenue / total units.
-- Uses ROUND(..., 2) for two decimal places.
-- Handles missing sales using IFNULL(..., 0).


SELECT
    p.product_id,
    IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
FROM
    Prices AS p
LEFT JOIN
    UnitsSold AS u
ON
    p.product_id = u.product_id
    AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY
    p.product_id;