from abc import ABC,abstractmethod

class UniversityDAO(ABC):
    
    @abstractmethod
    def insert_university(self,university):
        pass