-- We use LEFT JOIN to ensure that all employees from the Employees table are included in the result, 
-- even if they do not have a matching record in EmployeeUNI.
-- If an employee has a corresponding unique_id in EmployeeUNI, we retrieve it.
-- If there is no matching unique_id, the query will return NULL for that column.
-- The result can be returned in any order as per the problem statement.

SELECT en.unique_id,e.name
FROM Employees e 
LEFT JOIN EmployeeUNI en
on e.id=en.id