from abc import ABC , abstractmethod


class University(ABC):
    def __init__(self,name,university_code):
        self.name = name
        self.university_code = university_code
        
    def __str__(self):
        print(f'daneshgahe {self.name}')
        
    @abstractmethod
    def shahriye(self):
        pass