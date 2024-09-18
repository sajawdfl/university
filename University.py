from abc import ABC , abstractmethod

student_list = []
university_list = []
class University(ABC):
    def __init__(self,name,university_code):
        self.name = name
        self.university_code = university_code
        
    def __str__(self):
        print(f'{self.name} university')
        
    @abstractmethod
    def payment(self):
        pass
    
    @abstractmethod
    def register_student(name,family,national_code):
        pass
    
    @abstractmethod    
    def search_student(national_code):
        pass
            
    

        
        
                
    
        

        