from dao.CourseDAO import CourseDAO
from connectionUtils import connectionUtils


class CourseDAOSQL(CourseDAO):
    def __init__(self) :
        connectionUtils.get_connection(self)
        
    def insert_course(self,course):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM dbo.[course] WHERE name = ? AND unit = ? AND id = ?',course.course_list[0]['name'],course.course_list[0]['unit'],course.course_list[0]['id'])
        if cursor.fetchone() is None:
            cursor.execute('INSERT INTO dbo.[course](name,unit,id) VALUES (? , ? , ?)',course.course_list[0]['name'],course.course_list[0]['unit'],course.course_list[0]['id'])
            self.connection.commit()