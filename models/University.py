from abc import ABC , abstractmethod

# student_list = []
class University(ABC):
    university_list = []
    student_list = []
    course_list = []
    def __init__(self):
        self.__name = ''
        self.__university_code = 0
        
    def __str__(self):
        print(f'{self.name} university')
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
        
    @name.deleter
    def name(self):
        del self.__name
        
    @property    
    def code(self):
        return self.__university_code
    
    @code.setter
    def code(self,code):
        self.__university_code = code
        
    @code.deleter    
    def code(self):
        del self.__university_code
        
            
        
    @abstractmethod
    def add_university(university_name,university_code):
        pass
        
    @abstractmethod
    def payment(self):
        pass
    
    @abstractmethod
    def register_student(name,family,national_code):
        pass
    
    @abstractmethod    
    def search_student(national_code):
        pass
            
    
    
    
    
    
    

        
        
                
    
        

        