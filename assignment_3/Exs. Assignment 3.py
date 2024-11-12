'''1. Create a Course class, where each course has a name, a description and a list of enrolled students. You'll need to implement the next methods:
Add a student to the course.
Remove a student from the course.
Show all students in the course.'''


class Course:  #Create the class course
    def __init__(self, name, course_type):  #Define the class with the attributes name, course_type
        self.name=name
        self.course_type=course_type
        self.student_list=[]  #Initialize the list course.student_list
    def add_student(self,student):  #Method to add student to the course
        self.student_list.append(student)  #I add student to the list student.course_list
        student.course_list.append(self)  #I add student to the list course.student_list 
    def remove_student(self,student):  #Method to remove student from the course if the student takes that course(student in the list course.student _list)
        if student in self.student_list:
            self.student_list.remove(student)
            student.course_list.remove(self)
        else:
            pass
    def show_student(self):  #Method to show all students in the course
        l=set()
        for student in self.student_list:
            l.add(student.name)
        print(self.name,':',l)


'''2. Create a Student class, where each student has a name, ID number, address and a list of enrolled courses with the following methods:
Enroll in a course.
Drop a course.
Show all registered student courses.'''



class Student: #Create the class student
    def __init__(self, name, student_id,student_address):  #Define the class with the attributes name, student_id, student_address
        self.name=name
        self.studentid=student_id
        self.address=student_address
        self.course_list  #Initialise the list student.course_list
    def enroll(self, course):  #Method to enroll a student in a course
        self.course_list.append(course)  #I add course to the list student.course _list
        course.student_list.append(self)  #I add student to the course.student_list
    def drop(self, course):  #Method to drop a course for a student if the student is already enrolled in that course(course in the list student.course_list)
        if course in self.course_list:
            self.course_list.remove(course)
            course.student_list.remove(self)
        else:
            pass
    def show_course(self):  #Method to show all registered student courses
        l=set()
        for course in self.course_list:
            l.add(course.name)
        print(self.name,':',l)


'''3. Create a central class that manages courses and students, Registration class, where you have a list of students and a list of courses, and methods:
Enroll in a course.
Drop a course.
Show all the enrolled courses.
Show all the students.'''


class Registration:  #Create the class registration
    def __init__(self):
        self.students=[]  #Initialise two lists, one for classes one for students
        self.courses=[]
    def add_student(self,student):  #Method to add a student
        if student not in self.students:  #I add the student to the students list if it’s not already in
            self.students.append(student)
    def drop_student(self,student):  #Method to drop a student
         if student in self.students:  #I remove a student from the students list, if it’s in
            self.students.remove(student)
    def enroll_course(self,student,course):  #Method to enroll a student in a course 
        if self in self.students and course in self.courses:  #I enroll a student in a course if it is in the students list and the course in the courses list
            student.enroll(course)
    def drop_course(self, student, course):  #Method to drop a student from a course
        if self in self.students and course in self.courses:  #I drop a student from a course if it is in the students list and the course in the courses list
            student.drop(course)
    def show_all_students():  #Method to show all students
        if self.students:
            l=set()
            for student in self.students:
                l.add(student.name)
                print(l)
    def show_all_courses():  #Method to show all courses
        if self.courses:
            l=set()
            for course in self.courses:
                l.add(course.name)
                print(l)


'''4. Let's add grades to each student's course and create method that yields the GPA given a student name or ID.'''


class Student:
    def __init__(self, name, student_id,student_address):
        self.name=name
        self.studentid=student_id
        self.address=student_address
        self.course_list=[]
        self.grades  #Initialise a dictionary for grades
    def enroll(self, course):
        self.course_list.append(course)
        course.student_list.append(self)
    def drop(self, course):
        if course in self.course_list:
            self.course_list.remove(course)
            course.student_list.remove(self)
    def assign_grades(self, course_name, grade):  #Method of class student to assign grades
        for course in self.course_list:  #each course in student.course_list become a value in the dictionary student.grades with the grade(attribute of the method) as the key 
            if course.name==course_name:
                self.grades[course]=grade
            else:
                print(f'{self.name}is not enrolled in {course_name}')
    def calculate_gpa(self):  #Method of class student to calculate gpa
        if not self.grades:
            return 0.0
        total_points=0
        total_courses=len(self.course_list)
        grade_points={
            'A':4.0,
            'B':3.0,
            'C':2.0,
            'D':1.0,
            'F':0.0
        }
        for grade in self.grades.values():
            total_points += grade_points[grade]
        gpa= total_points/total_courses
        return round(gpa,2)    
        
class Course:
    def __init__(self, name, course_type):
        self.name=name
        self.course_type=course_type
        self.student_list=[]
    def add_student(self,student):
        self.student_list.append(student)
        student.course_list.append(self)
    def remove_student(self,student):
        if student in self.student_list:
            self.student_list.remove(student)
            student.course_list.remove(self)
        else:
            pass
