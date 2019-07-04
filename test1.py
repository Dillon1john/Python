list=[ ]
while True:
    name=str(input("Enter your name"))
    if name in list:
       print("Name in list try again")
    if name not in list:
        list.append(name)
        print(list)
