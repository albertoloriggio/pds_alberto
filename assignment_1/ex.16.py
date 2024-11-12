students_grades={'Alex':[6,7,4],'Anna':[9,7,9],'Antony':[8,7,6]}
def average_grades(students):
    for i in students:
        average=(sum(students[i])/len(students[i]))
        print(average)    
average_grades(students_grades)   
