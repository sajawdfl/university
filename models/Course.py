from errors.UnitError import UnitError


class Course:
    course_list = []
    def __init__(self):
        self.__name = ''
        self.__unit = 0
        self.__id = 0
        
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
        
    @property    
    def id(self):
        return self.__id

    @id.setter
    def id(self,id):
        self.__id = id
        
    @id.deleter
    def id(self):
        del self.__id
    
        
    def __str__(self):
        return (f'course name : {self.name} . unit : {self.unit}')
    
    
    
    # def add_course(name,unit):
    #     new_course = Course()
    #     new_course.name = name
    #     new_course.unit = unit
    #     course_data = {'course_name' : new_course.name , 'course_unit' : new_course.unit}
    #     Course.course_list.append(course_data)        
    #     print(f'{new_course.name} with {new_course.unit} units added to course list successfully')
        
    
    