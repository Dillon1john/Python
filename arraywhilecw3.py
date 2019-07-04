x=[ ]
while True:
    y=str(input("Enter name: "))
    x.append(y)
    print(x)
    name=y
    if name in x:
        m=x.pop(y)
        print("Registered already")
    if name not in x:
        
        
