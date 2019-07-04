#example of input list
name=[ ]
ssn=[ ]
age= [ ]
while True:
    Last_name=input("Enter your last name: ")
    if Last_name in name:
        print("Your name already in the list")
    else:
        name.append(Last_name)
        print("I just got your registered")
        Social= input("Enter your SSN: ")
        if Social in ssn:
            print("Your social already in list")
        else:
            ssn.append(Social)
            print("SSN registered")
            Age=input("Enter your age: ")
            age.append(Age)
            print(name,'\t',ssn,'\t',age)
