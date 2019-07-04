grades=[ ]
courses=[ ]
credits=[ ]
limit=int(input("How many courses did you take: "))
while len(courses) <limit:
        for course in range(0,limit):
            course=str(input("What course did you take: "))
            if course not in courses:
                courses.append(course)
                grade=float(input("What was your grade for this class:  "))
                if (grade>=93):
                    average=("A")
                    grade= 4.0
                elif (grade>=90):
                    average=("A-")
                    grade= 3.7
                elif (grade>=87):
                    average=("B+")
                    grade= 3.3 
                elif (grade>=83):
                    average=("B")
                    grade= 3.0
                elif (grade>=80):
                    average=("B-")
                    grade= 2.7
                elif (grade>=77):
                    average=("C+")
                    grade= 2.3
                elif (grade>=73):
                    average=("C")
                    grade= 2.0 
                elif (grade>=70):
                    average=("C-")
                    grade= 1.7
                elif (grade>=67):
                    average=("D+")
                    grade= 1.3
                elif (grade>=60):
                    average=("D")
                    grade= 1.0
                elif (grade<=59):   
                    average=("F")
                    grade= 0.0
                grades.append(grade)
                credit= float(input("How many credits did you get from this class: "))
                credits.append(credit)
                continue  
            else:
                print("Course already inputed, give a different course")
                continue
totalgrade=sum(grades)
totalcredit=sum(credits)
gpa=(totalgrade*totalcredit)/(totalcredit)
if len(courses)==limit:
    if (gpa>= 4.0):
        print("Your total gpa is 4.0.")
    else:
        print("Your total gpa is ",gpa,".")
        
