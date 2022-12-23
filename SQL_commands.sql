CREATE DATABASE teachers_portal;

USE teachers_portal;

CREATE TABLE students (
  studentId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  studentName VARCHAR(45) NOT NULL,
  enrolledinCourseID INT DEFAULT 1,
  grade FLOAT NULL
);

CREATE TABLE courses (
  courseId INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  courseName VARCHAR(45) NOT NULL
);

INSERT INTO students (studentName, enrolledinCourseID, grade)
VALUES ('Maria Josef', 1, 90), ('Linda Jones', 2, 89), ('John McGrail', 1, 98), ('Patty Luna', 2, 78);

INSERT INTO courses (courseName)
VALUES ('Database design'), ('Calculus'), ('physics I');