students = []  # list
courses = []   # list
marks = {} 

class Student():
    def __init__(self,name,id,dob):
        self.__name = name
        self.__id = id
        self.__dob = dob

    def get_name(self):
        return self.__name
    def get_id(self):
        return  self.__id
    def get_dob(self):
        return self.__dob
    
    

    def __str__(self):
        return f"Name: {self.__name} | Id: {self.__id} | Dob: {self.__dob}"
    
class Course():
    def __init__(self,id,name):
        self.__id = id
        self.__name = name

    def get_name(self):
        return self.__name
    def get_id(self):
        return  self.__id
    
    def __str__(self):
        return f"ID: {self.id} | Name Course: {self.name}"
        

def input_number_student():
    print("Enter the nb of student: ")
    nb_student = int(input())
    for i in range(nb_student):
        print("Student ", i+1)
        input_info_student()
        print("-------------")

def input_info_student():
    students.append(Student(input("Name: "), input("Id: "), input("Dob: ")))

def input_nb_course():
    nb_course = int(input("Input the nb of course: "))
    for i in range(nb_course):
        input_info_course()
        print("-------------")

def input_info_course():
    courses.append(Course(input("ID: "),input("Name: ")))



def list_students():
    print("------STUDENTS-------")
    for s in students:
        print(f"ID: {s.get_name()} || Name: {s.get_id()} || DoB: {s.get_dob()}")
def list_course():
    print("-----COURSE---------")
    for c in courses:
        print(f"ID: {c.get_id()} || Name: {c.get_name()}")


def input_mark(): 
    print("---INPUT MARK---")
    cid = input("Enter id of course to input marks: ")
    for course in courses:
        if cid == course.get_id():
            for student in students:
                sid = student.get_id()
                marks[(sid,cid)] = float(input(f"Enter mark of {student.get_name()} :"))
def show_mark():
    cid = input("Enter course ID to show marks: ")
    for s in students:
        sid = s.get_id()
        key = (sid,cid)
        if key in marks:
            print(f"{s.get_name()} : {marks[key]}")   
        else:
            print(f"{s.get_name()}: no mark")

input_number_student()    
input_nb_course()
input_mark()

list_students()
list_course()
