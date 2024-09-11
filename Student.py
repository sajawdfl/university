from Azad import Azad 
from Sarasari import Sarasari



class Student:
    def __init__(self,name,family,national_code,student_id,university):
        self.name = name
        self.family = family
        self.national_code = national_code
        self.student_id = student_id
        self.university = university
    
    def __str__(self):
        return (f'{self.name} {self.family} . shomare daneshjooi : {self.student_id}')
    
    

