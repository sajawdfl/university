from dao.UniversityDAO import UniversityDAO
from connectionUtils import connectionUtils
# cursor = conn.cursor()

class UniversityDAOSQL(UniversityDAO):
    def __init__(self):
        connectionUtils.get_connection(self)
        
    def insert_university(self,university):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM dbo.[university] WHERE name = ? AND code = ? AND type = ?',university.university_list[0]['name'],university.university_list[0]['code'],university.university_list[0]['type'])
        if cursor.fetchone() is None :
            cursor.execute('INSERT INTO dbo.[university](name,code,type)VALUES (? , ? , ?)',university.university_list[0]['name'],university.university_list[0]['code'],university.university_list[0]['type'])
            self.connection.commit()
        