import configparser
import pyodbc


class connectionUtils:
    def __init__(self):
        self.connection = None
        


    def get_connection(self):
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
    