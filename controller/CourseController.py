from models.Course import Course
from models.University import University
from models.Student import Student
from getInput import getInput
from dao.CourseDAOSQL import CourseDAOSQL

def createCourse():
    course = Course()
    return course
    
def getCourseName(course):
    name = getInput('please write course name :\n')
    course.__name = name
    
def getCourseUnit(course):
    unit = getInput('please write course unit :\n')
    course.__unit = unit

def getCourseId(course):
    id = getInput('please write course id :\n')
    course.__id = id
    
def confirmCourse(course):
    while True:
        confirmation = int(getInput(f'Do you want to add {course.__name} course with this course id : {course.__id} ? \n1: Yes 2:No\n '))
        if confirmation == 1:
            return True
        elif confirmation ==2:
            return False
        else:
            continue
dao = CourseDAOSQL()
def addCourse(course):
    course_data = {'name' : course.__name , 'unit' : course.__unit , 'id' : course.__id}
    course.course_list.append(course_data)
    dao.insert_course(course)
    print(f'{course.__name} course   added successfully .')


def showUniversityCourse():
    print(University.course_list)
    

def selectCourse():
    courseId = getInput('please write course id :\n')
    return courseId

def check_id(id,ls):
    for course in ls:
        if course['id'] == str(id) :
            return id
    print('course not found !!!')
    return False

def chooseCourse(selected_id):
    course_data  = {'id' : selected_id}
    Student.course_list.append(course_data)
    print(f'new course with id : {selected_id} added succesfully .')
    
def showStudentCourse():
    print(Student.course_list)
    