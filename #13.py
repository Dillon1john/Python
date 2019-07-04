grades = []  # This section makes empty lists to fill
courses = []
Credits = []
cont= True
cont= False
totalgpa= 0
while True:
    course = str(input("What course did you take: "))  # Section adds course to courses list
    if course not in courses:
        courses.append(course)
        grade = float(input("What was your grade for this class:  "))  # Section adds grade to grades list
        if (grade >= 93):  # Section assigns grade to 4.0 scale
            average = ("A")
            grade = 4.0
        elif (grade >= 90):
            average = ("A-")
            grade = 3.7
        elif (grade >= 87):
            average = ("B+")
            grade = 3.3
        elif (grade >= 83):
            average = ("B")
            grade = 3.0
        elif (grade >= 80):
            average = ("B-")
            grade = 2.7
        elif (grade >= 77):
            average = ("C+")
            grade = 2.3
        elif (grade >= 73):
            average = ("C")
            grade = 2.0
        elif (grade >= 70):
            average = ("C-")
            grade = 1.7
        elif (grade >= 67):
            average = ("D+")
            grade = 1.3
        elif (grade >= 60):
            average = ("D")
            grade = 1.0
        elif (grade <= 59):
            average = ("F")
            grade = 0.0
        grades.append(grade)
        credit = float(input("How many credits did you get from this class: "))  # Section adds credit to credits list
        Credits.append(credit)
        totalgpa= totalgpa+ (grade*credit)
        finalgpa= totalgpa/sum(Credits)
        print("Your total gpa is ", finalgpa, ".") 
        cont=str(input("Would you like to add another course y/n: "))
        if cont== "n": 
            break
        else:
            continue
    else:
        print("Course already inputed, give a different course")  # Section keeps courses from repeating
    
