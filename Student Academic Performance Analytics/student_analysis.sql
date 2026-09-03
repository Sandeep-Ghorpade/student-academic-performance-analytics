-- ============================================================
-- Student Academic Performance Analytics
-- SQL Analysis
-- ============================================================

USE student_analytics;


-- 1. Total Number of Students

SELECT COUNT(*) AS Total_Students
FROM students;


-- 2. Student Count by Department

SELECT Department,
       COUNT(*) AS Total_Students
FROM students
GROUP BY Department;


-- 3. Average Final Score by Department

SELECT Department,
       ROUND(AVG(Final_Score), 2) AS Average_Final_Score
FROM students
GROUP BY Department;


-- 4. Average Attendance by Department

SELECT Department,
       ROUND(AVG(Attendance), 2) AS Average_Attendance
FROM students
GROUP BY Department;


-- 5. Gender Distribution

SELECT Gender,
       COUNT(*) AS Total_Students
FROM students
GROUP BY Gender;


-- 6. Top 10 Performing Students

SELECT First_Name,
       Last_Name,
       Department,
       Final_Score
FROM students
ORDER BY Final_Score DESC
LIMIT 10;


-- 7. Students with Attendance Below 75%

SELECT COUNT(*) AS Low_Attendance_Students
FROM students
WHERE Attendance < 75;


-- 8. Average Study Hours by Department

SELECT Department,
       ROUND(AVG(Study_Hours_per_Week), 2) AS Average_Study_Hours
FROM students
GROUP BY Department;


-- 9. Grade Distribution

SELECT Grade,
       COUNT(*) AS Total_Students
FROM students
GROUP BY Grade
ORDER BY Grade;


-- 10. Average Final Score by Stress Level

SELECT Stress_Level,
       ROUND(AVG(Final_Score), 2) AS Average_Final_Score
FROM students
GROUP BY Stress_Level
ORDER BY Stress_Level;