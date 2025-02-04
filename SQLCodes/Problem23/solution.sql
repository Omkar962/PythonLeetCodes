-- COUNT(DISTINCT subject_id): This counts the distinct subject_id values for each teacher. Since a teacher might teach the same subject in different departments, we only want to count that subject once per teacher.

-- GROUP BY teacher_id: We group the results by teacher_id so that we can get the count of unique subjects for each teacher.



SELECT teacher_id, COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
