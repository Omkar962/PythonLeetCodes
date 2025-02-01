-- Subquery (m):

-- SELECT managerId: We select the managerId for each employee.
-- WHERE managerId IS NOT NULL: We exclude employees without a manager.
-- GROUP BY managerId: We group by the managerId to get the count of employees reporting to each manager.
-- HAVING COUNT(*) >= 5: We only keep managers who have 5 or more direct reports.
-- Main Query:

-- JOIN: We join the original Employee table with the result of the subquery on the managerId column.
-- SELECT e.name: We select the names of the managers.
-- GROUP BY e.id: We group by e.id to ensure unique manager names.


SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
) m ON e.id = m.managerId
GROUP BY e.id;
