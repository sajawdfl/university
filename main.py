from models.Azad import Azad
from models.Sarasari import Sarasari 
from models.Course import Course
from models.Student import Student
from errors.CustomError import CustomError
from getInput import getInput
import pandas as pd
from national_card import national_card
from controller.UniversityController import getUniversityType,getUniversityName,getUniversityCode,confirmUniversity,addUniversity
from controller.StudentController import checkNationalNumber , createStudent , getStudentFamily ,getStudentName,confirmStudent,addStudent,search_student
from controller.CourseController import createCourse,getCourseName,getCourseUnit,getCourseId,confirmCourse,addCourse,showUniversityCourse,selectCourse,check_id,chooseCourse,showStudentCourse
from models.University import University



# while True:
#     print('1 : register new student \n2 : create new university \n3 : search student \n4 : add new course\n0: Exit\n-------------------------------')
#     action = int(input('select one action :'))
#     if action == 0:
#         break
#     elif action == 1:

#         new_student = createStudent()
#         checkNationalNumber(new_student)
#         getStudentName(new_student)
#         getStudentFamily(new_student)
#         if confirmStudent(new_student):
#             addStudent(new_student)
#             print(University.student_list)
            
        
#     elif action == 2:
        
#         new_university = getUniversityType()
#         getUniversityName(new_university)
#         getUniversityCode(new_university)
#         if confirmUniversity(new_university):
#             addUniversity(new_university)
            
#     elif action == 3:
#         print(search_student())
            
#     if action == 4:
#         new_course = createCourse()
#         getCourseName(new_course)
#         getCourseUnit(new_course)
#         if confirmCourse(new_course):
#             addCourse(new_course)
#             showCourse()
            
while True:
    print('---------------------------------------')
    print('1 : University 2 : Student 3 :Course ')
    print('---------------------------------------')
    section = getInput('select one action :\n')
    if section == '2':
        print('1 : Register new student 2 : Add course ')
        action = getInput('select one action:\n')
        if action == '1':
            new_student = createStudent()
            checkNationalNumber(new_student)
            getStudentName(new_student)
            getStudentFamily(new_student)
            if confirmStudent(new_student):
                addStudent(new_student)
                print(new_student.student_list)
        elif action == '2':
            showUniversityCourse()
            course_id = selectCourse()
            confirmed_id = check_id(course_id,University.course_list)
            if confirmed_id:
                chooseCourse(confirmed_id)
                showStudentCourse()
            
            
    elif section == '1':
        print('1 : Add new universty 2 : Add new course 3 : Search student ')
        action = getInput('select one action:\n')
        if action == '1':
            new_university = getUniversityType()
            getUniversityName(new_university)
            getUniversityCode(new_university)
            if confirmUniversity(new_university):
                addUniversity(new_university)
        elif action == '2':
            new_course = createCourse()
            getCourseName(new_course)
            getCourseUnit(new_course)
            getCourseId(new_course)
            if confirmCourse(new_course):
                addCourse(new_course)
        elif action == '3':
            print(search_student())

