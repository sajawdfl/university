from University import University , student_list


class Sarasari(University):
    
    def __init__ (self,name,university_code):
        super().__init__(name,university_code)

    def shahriye(self):
        return ('10000000 RLS')
    
    def register_student(name,family,national_code,student_id):
        student_data = {'name' : name , 'family' : family , 'national_code' : national_code, 'student_id' : student_id ,'type' : 'sarasari'}
        student_list.append(student_data)
        print(f'{name} {family} registered successfully!')
