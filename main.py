from University import University
from Azad import Azad
from Sarasari import Sarasari ,student_list
from Student import Student
import pandas as pd


university1 = Sarasari('shahid beheshti',23432)
university2 = Azad('tehran markaz',57621)

student1 = Student('Faraz','Yazdani',123459,65432,university1)
student2 = Student('Ahmad','Mohsen',432156,32432,university2)

# student_list.clear()
new_student1 = Sarasari.register_student('sajad','fallah','0022926968','3434223')
new_student2 = Azad.register_student('faraz','yazdani','123456789','8878786')
print(pd.DataFrame(student_list))