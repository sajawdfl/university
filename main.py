from University import University, university_list
from Azad import Azad
from Sarasari import Sarasari ,student_list
import pandas as pd
from national_card import national_card
from CustomError import CustomError
from Course import Course , course_list
from UnitError import UnitError 



# university1 = Sarasari('shahid beheshti',23432)
# university2 = Azad('tehran markaz',57621)

# # student_list.clear()
# new_student1 = Sarasari.register_student('sajad','fallah','0022926968')
# new_student2 = Azad.register_student('faraz','yazdani','123456789')
# new_student3 =Sarasari.register_student('parham','ebrahimi','875465')

# # course1  = Course()
# # course1.name = 'computer science'
# # course1.name = 'math'
# # course1.unit = 3
# # print(course1.name)
# # print(course1.unit)

# try:
#     f = Sarasari.search_student('0022926968')
#     print(pd.DataFrame(f))
# except CustomError as e:
#     e.print()


print('1 : register new student \n2 : create new university \n3 : search student \n4 : add new course\n0: Exit\n-------------------------------')
while True:
    action = int(input('select one action :'))
    if action == 0:
        break
    elif action == 1:
        name = input('write your name :')
        family = input ('write your family :')
        national_number = input ('write your national number :')
        university_type = int(input('1 : Azad   2 : Sarasari 0 : Exit\nselect your university type:'))
        if university_type == 1:
            try:
                new_student = Azad.register_student(name,family,national_number)
                print(student_list)
            except CustomError as e:
                e.print()
        elif university_type ==2:
            try:
                new_student = Sarasari.register_student(name,family,national_number)
                print(student_list)
            except CustomError as e:
                e.print()
        elif university_type == 0:
            break
        if university_type == 1:
            pass
    elif action == 2:
        university_name  = input('write university_name :')
        university_code = input('write university_code :')
        university_type = int(input('1 : Azad   2 : Sarasari 0 : Exit\nselect your university type:'))
        if university_type == 1:
            Azad.add_university(university_name,university_code)
        elif university_type == 2:
            Sarasari.add_university(university_name,university_code)
        elif university_type == 0:
            break
                
    elif action == 3:
        university_type = int(input('1 : Azad   2 : Sarasari 0 : Exit\nselect your university type:'))
        student = input('please write national_code :')
        if university_type == 1:
            try:
                find_student = Azad.search_student(student)
                print(find_student)
            except CustomError as e:
                e.print()
        elif university_type == 2 :
            try:
                find_student = Sarasari.search_student(student)
                print(find_student)
            except CustomError as e:
                e.print()
        elif university_type == 0 :
            break
            
    if action == 4:
        course_name = input('please write course name :')
        unit = int(input('please write course unit :'))
        try:
            new_course = Course.add_course(course_name,unit)
        except CustomError as e:
            e.print()
        
        