#This code loops and terminates
pin=1234
count=0
limit=3
while True:
    x=float(input("Enter pin: "))  
    if x!=pin:
        count=count+1
        print("Try again")
        if count>=limit:
           print("No more tries")
           break
    if x==pin:
        print("Valid User")
        break 
   
  
