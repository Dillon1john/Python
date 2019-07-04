#This program loops with break
age=float(input("Enter your age: "))
while True:
    if age<=17:
        age=int(input("Too young, enter age again: "))
        print(age)
        continue
    if age>=18:
        ssn=int(input("Enter last 4 digits of your SSN: "))
        print("Your age is,",age,",and your SSN is,",ssn)
        break
        
        
        
        
    
    
