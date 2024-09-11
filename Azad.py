from University import University , student_list
class Azad(University):
    
    def __init__(self, name, university_code):
        super().__init__(name, university_code)
        
    def shahriye(self):
        return ('20000000 RLS')

    def register_student(name,family,national_code,student_id):
        student_data = {'name' : name , 'family' : family , 'national_code' : national_code , 'student_id' : student_id , 'type' : 'azad'}
        student_list.append(student_data)
