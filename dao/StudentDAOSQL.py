from dao.StudentDAO import StudentDAO
from connectionUtils import connectionUtils

class StudentDAOSQL(StudentDAO):
    def __init__(self) :
        connectionUtils.get_connection(self)
        
    def insert_student(self, student):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM dbo.[student] WHERE name = ? AND family = ? AND national_code = ? ',student.student_list[0]['name'],student.student_list[0]['family'],student.student_list[0]['national_code'])
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO dbo.[student](name,family,national_code)VALUES (? , ? , ? )',student.student_list[0]['name'],student.student_list[0]['family'],student.student_list[0]['national_code'])
            self.connection.commit()