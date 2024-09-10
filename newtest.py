from abc import ABC ,abstractmethod

class University(ABC):
    def __init__(self,name,university_code):
        self.name = name
        self.university_code = university_code
        
    def __str__(self):
        print(f'daneshgahe {self.name}')
        
    @abstractmethod
    def shahriye(self):
        pass

        
class Sarasari(University):
    def shahriye(self):
        return ('10000000 RLS')

class Azad(University):
    def shahriye(self):
        return ('20000000 RLS')

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



