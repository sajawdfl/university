from dao.StudentDAO import StudneDAO
from connectionUtils import connectionUtils
from models.University import University

class StudentDAOSQL(StudneDAO):
    def __init__(self) :
        connectionUtils.get_connection(self)
        
    def insert_student(self, student):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO dbo.[student](name,family,naional_code)VALUES (? , ? , ?)',student.__name,student.__family,student.__national_code)
        self.connection.commit()