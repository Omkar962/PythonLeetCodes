-- LEFT JOIN:
-- Ensures that all employees from the Employee table are included, even if they do not have a bonus.
-- If an employee does not have a corresponding entry in Bonus, b.bonus will be NULL.

-- WHERE Clause:
-- b.bonus < 1000: Selects employees with a bonus less than 1000.
-- b.bonus IS NULL: Ensures that employees without a bonus record are also included.


SELECT e.name,b.bonus
FROM Employee e 
LEFT JOIN Bonus b
on e.empid=b.empid
WHERE b.bonus<1000 OR b.bonus IS NULL