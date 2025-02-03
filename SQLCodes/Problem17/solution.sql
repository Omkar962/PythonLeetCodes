-- Join the Project and Employee tables on employee_id:

-- This allows us to get the experience_years for each employee working on a project.
-- Use AVG(e.experience_years) to compute the average experience of employees in each project.

-- Use ROUND(..., 2) to round the result to two decimal places, as required.

-- Group by project_id to calculate the average experience per project.


SELECT 
    p.project_id, 
    ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e 
ON p.employee_id = e.employee_id
GROUP BY p.project_id;
