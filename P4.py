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
                grades.append(grade)
                credit= float(input("How many credits did you get from this class: "))
                credits.append(credit)
                continue 
                totalgrade=sum(grades)
                totalcredit=sum(credits)
            else:
                print("Course already inputed, give a different course")
                continue
            score=0.0
            if (grade>=93):
                average=("A")
                grade= score+ 4.0
            elif (grade>=90):
                average=("A-")
                grade= score+ 3.7
            elif (grade>=87):
                average=("B+")
                grade= score+ 3.3 
            elif (grade>=83):
                average=("B")
                grade= score+ 3.0
            elif (grade>=80):
                average=("B-")
                grade= score+ 2.7
            elif (grade>=77):
                average=("C+")
                grade= score+ 2.3
            elif (grade>=73):
                average=("C")
                grade= score+ 2.0 
            elif (grade>=70):
                average=("C-")
                grade= score+ 1.7
            elif (grade>=67):
                average=("D+")
                grade= score+ 1.3
            elif (grade>=60):
                average=("D")
                grade= score+ 1.0
            elif (grade<=59):   
                average=("F")
                grade=score
totalgrade=sum(grades)
totalcredit=sum(credits)
gpa=(totalgrade*totalcredit)/(totalcredit)
if len(courses)==limit:
    print("Your total gpa is ",gpa,".")
  
