from models.Student import Student #, student_list
from national_card import national_card
from models.University import University
from errors import NationalNumberError , ValidationError
from getInput import getInput
from dao.StudentDAOSQL import StudentDAOSQL



def createStudent():
    new_student = Student()
    return new_student

def checkNationalNumber(student):
    while True:
        national_number = getInput('write your national_number :\n')
        if national_number != national_card(national_number[:-1]):
            print('invalid national number !!!')
            continue
        print('valid')
        student.__national_code = national_number
        return True
        


def getStudentName(student):

    name = getInput('write your name : ')
    student.__name = name
        
def getStudentFamily(student):
        family = getInput('write your family :')
        student.__family = family
        
def confirmStudent(student):
    while True:
        s = int(getInput(f'Do you want to register as {student.__name} {student.__family} with national code : {student.__national_code} ?\n1 : Yes 2 : No\n'))
        if s == 1:
            return True
        elif s == 2:
            return False
        else:
            continue

dao = StudentDAOSQL()        
def addStudent(student):
    student_data = {'name' : student.__name , 'family' : student.__family , 'national_code' : student.__national_code}
    student.student_list.append(student_data)
    dao.insert_student(student)
    # print(student_list)
    print(f'{student.__name} {student.__family} registered successfully .')
    
def search_student():
    national_code = getInput('please write your national number :\n')
    if national_code == national_card(national_code[:-1]):
        find_student = [student for student in University.student_list if student['national_code'] == national_code]
        if not find_student:
            print('student not found !!!')
    else:
        print('invalid national number !!!')
    return find_student
    
    
    

    
        
        

        
        