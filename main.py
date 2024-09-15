from University import University
from Azad import Azad
from Sarasari import Sarasari ,student_list
import pandas as pd
from national_card import national_card
from CustomError import CustomError


university1 = Sarasari('shahid beheshti',23432)
university2 = Azad('tehran markaz',57621)


student_list.clear()
new_student1 = Sarasari.register_student('sajad','fallah','0022926968')
new_student2 = Azad.register_student('faraz','yazdani','123456789')
new_student3 =University.register_student('parham','ebrahimi','875465')


try:
    f = University.search_student('0022926968')
    print(pd.DataFrame(f))
except CustomError as e:
    e.print()



