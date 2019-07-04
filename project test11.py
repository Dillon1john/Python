course = []
credit = []
grade = []
a = "true"
b = "true"
totalgpa = 0
while a != "no":# While a is true it will run program, if a is no program will not run
    x = input("enter your course: ")
    if x in course:
        print("you already entered your course")
    else:
        course.append(x)
        z = int(input("enter your credit: "))
        credit.append(z)
        v = float(input("enter your grade: "))
        grade.append(v)
        print(course,'\t',credit,'\t',grade,'\t')
        #assign list to varible 
        if v>=93:
            g = 4.0
            print("A")
        elif v>=90:
            g = 3.7
            print("A-")
        elif v>=87:
            g = 3.3
            print("B+")
        elif v>=83:
            g = 3.0
            print("B")
        elif v>=80:
            g = 2.7
            print("B-")
        elif v>=77:
            g = 2.3
            print("C+")
        elif v>=70:
            g = 2.0
            print("C")
        elif v>=60:
            g = 0.7
            print("D")
        else:
            g = 0.0
            print("F")
            continue
        totalgpa = totalgpa + (g * z)
        b = input("would you like to enter another course: ")
        if b == "no":
            totalgpa = totalgpa/sum(credit)
            print("your gpa is",totalgpa)
            break
        #program finish running
