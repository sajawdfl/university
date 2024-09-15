from abc import ABC , abstractmethod
from Student import Student
from national_card import national_card
from CustomError import CustomError
from validation_error import validationError

student_list = []
university_list = []
class University(ABC):
    def __init__(self,name,university_code):
        self.name = name
        self.university_code = university_code
        
    def __str__(self):
        print(f'{self.name} university')
        
    @abstractmethod
    def shahriye(self):
        pass
    
    @abstractmethod
    def register_student(name,family,national_code):
        new_studnet = Student(name,family,national_code)
        student_data = {'name' : new_studnet.name , 'family' : new_studnet.family , 'national_code' : new_studnet.national_code , 'type' : 'unknown'}
        student_list.append(student_data)
        print(f'{new_studnet.name} {new_studnet.family} registered successfully!')
    
    @abstractmethod    
    def search_student(national_code):
        if national_code == national_card(national_code[:-1]):
            find_student = [student for student in student_list if student['national_code'] == national_code]
            if find_student :
                pass
            else:
                raise validationError
        else:
            raise CustomError
        
        return find_student
            
    

        
        
                
    
        

        