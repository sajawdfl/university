from abc import ABC , abstractmethod

student_list = []
university_list = []
class University(ABC):
    def __init__(self,name,university_code):
        self.name = name
        self.university_code = university_code
        
    def __str__(self):
        print(f'daneshgahe {self.name}')
        
    @abstractmethod
    def shahriye(self):
        pass
    
    @abstractmethod
    def register_student(self,name,family,national_code):
        student_data = {'name' : self.name , 'family' : self.family , 'national_code' : self.national_code}
        student_list.append(student_data)
        print(f'{self.name} {self.family} registered successfully!')
                
    
        

        