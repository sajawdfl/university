from UnitError import UnitError


course_list = []
class Course:
    def __init__(self):
        self.__name = ''
        self.__unit = 0
        
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
    def unit(self):
        return self.__unit
    
    @unit.setter
    def unit(self,unit):
        if 3 >= unit > 0:
            self.__unit = unit
        else:
            raise UnitError
        
    @unit.deleter
    def unit(self):
        del self.__unit    
    
        
    def __str__(self):
        return (f'course name : {self.name} . unit : {self.unit}')
    
    
    
    def new_course(self,name,unit):
        new_course = Course(name,unit)
        course_data = {'course_name' : new_course.name , 'course_unit' : new_course.unit}
        course_list.append(course_data)        
        print(f'{new_course.name} with {new_course.unit} units added to course_list successfully')
        
    
    