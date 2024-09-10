from Azad import Azad 
from Sarasari import Sarasari



class Student:
    def __init__(self,name,family,student_id,university):
        self.name = name
        self.family = family
        self.student_id = student_id
        self.university = university
    
    def __str__(self):
        return (f'{self.name} {self.family} . shomare daneshjooi : {self.student_id}')
    
    
university1 = Sarasari('shahid beheshti',23432)
university2 = Azad('tehran markaz',57621)

student1 = Student('Faraz','Yazdani',123459,university1)
student2 = Student('Ahmad','Mohsen',432156,university2)


print(student1.university.shahriye())
print(student2.university.shahriye())
print(student1)