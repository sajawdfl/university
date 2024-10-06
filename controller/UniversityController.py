from models.Sarasari import Sarasari
from models.Azad import Azad
from models.University import University
from getInput import getInput
import configparser
import pyodbc
from dao.UniversityDAOSQL import UniversityDAOSQL


# config = configparser.ConfigParser()
# config.read('config.ini')
# driver = config['default']['driver']
# server = config['default']['server']
# database = config['default']['database']
# uid = config['default']['uid']
# pwd = config['default']['pwd']
# trusted_connection = config['default']['trusted_connection']
# connection_string = f'{driver};{server};{database};{uid};{pwd};{trusted_connection}'
# conn = pyodbc.connect(connection_string)
# cursor = conn.cursor()


dao =UniversityDAOSQL()


new_university = None
def getUniversityType():
    while True:
        university_type = int(getInput('1 : Azad   2 : Sarasari 0 : Exit\nselect your university type:'))
        if university_type==1:
            new_university=Azad()
            new_university.type = 'azad'
        elif university_type==2:
            new_university=Sarasari()
            new_university.type = 'sarasari'
        else:
            continue
        
        return new_university

def getUniversityName(university):
    university.__name   = getInput('write university name :')
    
    
def getUniversityCode(university):
    university.__code = getInput('write university code :')
    
def confirmUniversity(university):
    while True:
        a = int(getInput(f'Do you want to add {university.__name} university with university code : {university.__code} ?\n1 : Yes 2 : No\n'))
        if a == 1 :
            return True
        if a == 2 :
            return False
        else:
            continue

def addUniversity(university):
    university_data = {'name' : university.__name , 'code' : university.__code , 'type' : university.type}
    university.university_list.append(university_data)
    dao.insert_university(university)
    
    print(f'university {university.__name} with university code ; {university.__code} added successfully .')
    

            

# def VALIDATE():
#     while :
#         try:
#              university_name  = input('write university_name :')
#              #validate input
#              if(quit)
#              break
#             new_university.name=university_name
#         except:
#             continue    


# def getInformation(university_name, university_code):
#     while():
#         try:
            

#             university_code = input('write university_code :')
            
#             university_data = {'university_name' : new_university.name , 'university_code' : new_university.university_code , 'university_type' :'sarasari'}
#             university_list.append(university_data)
#             print(f'{new_university.name} university added successfully')
#         except:
            
#             con
        
# def print():
#     print(new_university)
# def askforconfirm():
    
#     if(A==1){
#         university_list.append(new_university)
#     }else{
        
#     }