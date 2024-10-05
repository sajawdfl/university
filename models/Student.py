student_list = []
class Student:
    course_list = []
    def __init__(self):
        self.__name = ''
        self.__family = ''
        self.__national_code = 0
        
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
    def family(self):
        return self.__family
    
    @family.setter
    def family(self,family):
        self.__family = family
        
    @family.deleter    
    def family(self):
        del self.__family
        
    @property    
    def national_code(self):
        return self.__national_code
    
    @national_code.setter
    def national_code(self,national_code):
        self.__national_code = national_code
        
    @national_code.deleter
    def national_code(self):
        del self.__national_code
        
    
    def __str__(self):
        return (f'{self.name} {self.family} . student_number : {self.student_id}')
    
    

