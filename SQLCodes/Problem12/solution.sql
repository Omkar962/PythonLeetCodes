-- Generate All Student-Subject Pairs:

-- Using CROSS JOIN between Students and Subjects ensures that every student is paired with every subject.
-- Count Exam Attendances:

-- LEFT JOIN with Examinations ensures we keep all students and subjects, even if they have no recorded exams.
-- COUNT(e.subject_name): Counts the number of times a student has taken an exam in a given subject.
-- If there is no match in Examinations, e.subject_name will be NULL, and COUNT(NULL) returns 0.
-- Sorting for Output Format:

-- ORDER BY s.student_id, sub.subject_name: Ensures the results are sorted as required.


SELECT s.student_id, s.student_name, sub.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN Examinations e 
ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
GROUP BY s.student_id, s.student_name, sub.subject_name
ORDER BY s.student_id, sub.subject_name;
