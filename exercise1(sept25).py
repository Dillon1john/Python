name=str(input("What is your name: "))
payrate=int(input("What is your hourly rate of pay: "))
workhours=int(input("How many hours did you work this week: "))
if workhours<40:
    totalpay= workhours*payrate
    print (name," your payment this week is","$",totalpay)
else:
    if workhours>=40:
        overtime=str(input("Are you paid overtime(yes/no): "))
        if overtime =="yes":
            overtimehours=workhours-40
            totalpay= (40*payrate)+(overtimehours*payrate*1.5)
            print (name," your payment this week is","$",totalpay)
        else:
                if overtime =="no":
                    totalpay= workhours*payrate
                    print (name," your payment this week is","$",totalpay)
