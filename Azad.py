from University import University , student_list
from Student import Student
from national_card import national_card
class Azad(University):
    
    def __init__(self, name, university_code):
        super().__init__(name, university_code)
        
    def shahriye(self):
        return ('20000000 RLS')

    def register_student(name,family,national_code):
        new_student = Student(name , family , national_code )
        student_data = {'name' : new_student.name , 'family' : new_student.family , 'national_code' : new_student.national_code , 'type' : 'azad'}
        student_list.append(student_data)
        print(f'{new_student.name} {new_student.family} registered successfully!')
        
    def search_student(national_code):
        if national_code == national_card(national_code[:-1]):
            find_student = [student for student in student_list if student['national_code'] == '0022926968']
        else:
            raise ValueError('Invalid national_code !!!')
            return find_student
