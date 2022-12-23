CREATE DEFINER=`root`@`localhost` PROCEDURE `studentsWithGrade`()
BEGIN
SELECT students.studentname, students.studentId,courses.courseName,grade
FROM students
LEFT JOIN courses
ON students.enrolledIncourseID = courses.courseId;
END