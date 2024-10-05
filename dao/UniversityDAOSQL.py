import pyodbc
import configparser
from dao import UniversityDAO


# cursor = conn.cursor()

class UniversityDAOSQL(UniversityDAO):
    def __init__(self,server,database,uid,pwd):
        config = configparser.ConfigParser()
        config.read('config.ini')
        driver = config['default']['driver']
        server = config['default']['server']
        database = config['default']['database']
        uid = config['default']['uid']
        pwd = config['default']['pwd']
        trusted_connection = config['default']['trusted_connection']
        connection_string = f'{driver};{server};{database};{uid};{pwd};{trusted_connection}'
        self.connection = pyodbc.connect(connection_string)
        
    def insert_university(self,university):
        cursor = self.connection.cursor()
        cursor.execute('INSERT INTO dbo.[university](name,university_code)VALUES (? , ?)',university.university_list[0]['name'],university.university_list[0]['code'])
        self.connection.commit()
        