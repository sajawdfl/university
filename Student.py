class Student:
    def __init__(self,name,family,national_code):
        self.name = name
        self.family = family
        self.national_code = national_code
    
    def __str__(self):
        return (f'{self.name} {self.family} . student_number : {self.student_id}')
    
    

