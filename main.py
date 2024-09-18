from University import University
from Azad import Azad
from Sarasari import Sarasari ,student_list
import pandas as pd
from national_card import national_card
from CustomError import CustomError
from Course import Course



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


print('1 : register new student \n2 : create new university \n3 : search student \n4 : payment \n5 : add new course\n0: Exit\n-------------------------------')
while True:
    action = int(input('select one action :'))
    if action == 0:
        break
    if action == 1:
        name = input('write your name :')
        family = input ('write your family :')
        national_number = input ('write your national number :')
        university_type = int(input('1 : Azad   2 : Sarasari\nselect your university type:'))
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
        if university_type == 1:
            pass
    if action == 2:
        print('please write your personal info')
    if action == 3:
        print('please write your national number')
    if action == 4:
        print('please write your university type :')
    if action == 5:
        print('please write your course name')
    







