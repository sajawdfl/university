from abc import ABC ,abstractmethod

class StudentDAO(ABC):
    
    @abstractmethod
    def insert_student(self,student):
        pass