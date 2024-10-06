from models.University import University 
from models.Student import Student
from national_card import national_card
from errors.NationalNumberError import NationalNumberError
from errors.ValidationError import ValidationError


class Sarasari(University):
    
    def __init__ (self):
        super().__init__()

    def payment(self):
        return ('10000000 RLS')
    
    def add_university(university_name, university_code,type):
        new_university = Sarasari(university_name,university_code,type)
        university_data = {'university_name' : new_university.name , 'university_code' : new_university.university_code , 'university_type' :University.type}
        University.university_list.append(university_data)
        print(f'{new_university.name} university added successfully')
    
    
    def register_student(name,family,national_code):
        if national_code == national_card(national_code[:-1]):
            new_student = Student(name , family , national_code )
            student_data = {'name' : new_student.name , 'family' : new_student.family , 'national_code' : new_student.national_code , 'type' : 'sarasari'}
            University.student_list.append(student_data)
            print(f'{new_student.name} {new_student.family} registered successfully!')
        else:
            raise NationalNumberError
    
    def search_student(national_code):
        if national_code == national_card(national_code[:-1]):
            find_student = [student for student in University.student_list if student['national_code'] == national_code]
            if not find_student:
                raise ValidationError
        else:
            raise NationalNumberError#('Invalid national_code !!!')
        return find_student
