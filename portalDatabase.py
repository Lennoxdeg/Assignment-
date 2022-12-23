import mysql.connector
from mysql.connector import Error


class Database():
    # Constructor function to initialize the objects' attributes
    def __init__(self,
                 host="localhost",
                 port="3306",
                 database="teachers_portal",
                 user='root',
                 password='P@ssword123'):

        self.host       = host
        self.port       = port
        self.database   = database
        self.user       = user
        self.password   = password
        self.connection = None
        self.cursor     = None
        self.connect()

    def connect(self):
        """
            create a connection to MySQL server database teachers_portal running at localhost port 3306
            using the provided login credentials ('root','password')
       """
        try:
            self.connection = mysql.connector.connect(
                host         = self.host,
                port         = self.port,
                database     = self.database,
                user         = self.user,
                password     = self.password)
            
            if self.connection.is_connected():
                return
        # Catch any exceptions and print an error message in case of an error
        except Error as e:
            print("Error while connecting to MySQL", e)
    

    def getAllStudents(self):
        """
          check if connection is established and retrieve the result of the stored procedure in the database
        """
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            self.cursor.callproc("studentsWithGrade")
            records = self.cursor.stored_results()
            return records

    def addStudent(self, name, courseID,grade=0):
        """
            Insert a new student's name, courseID, and grade
        """
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            add_student = ("INSERT INTO students "
            "(studentName, enrolledInCourseID, grade) "
            "VALUES (%s, %d, %f)")
            data_student = (name, courseID, grade)

            try:
                self.cursor.execute(add_student, data_student)
                self.connection.commit()
            except:
                # Rolling back in case of error
                self.connection.rollback()

    def addCourse(self, name):
        ''' function to insert a new course to the courses database'''
        if self.connection.is_connected():
            self.cursor= self.connection.cursor();
            add_course = ("INSERT INTO courses "
            "(courseName) "
            "VALUES (%s)")
            data_course = (name)

            try:
                self.cursor.execute(add_course, data_course)
                self.connection.commit()
            except:
                
                self.connection.rollback()
        
    
    def modifyGrade(self, studentID, grade):
        '''Function updates the grade of a provided studentID'''

        grade_update = '''UPDATE students SET grade = <grade> WHERE studentID = <studentID> '''

        try:
            # Execute the SQL command
            self.cursor.execute(grade_update)
            # Commit changes in the database
            self.connection.commit()

        except:
            # Rollback in case there is any error
            self.connection.rollback()
        