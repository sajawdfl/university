from abc import ABC,abstractmethod

class CourseDAO(ABC):
    
    @abstractmethod
    def insert_course(self,course):
        pass