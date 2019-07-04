#This program calculates the weekly pay check for a user
name=input("What is your name? ")
payrate=float(input("How much are you paid per hour? "))
work_hour=int(input("How many hours did you work this week? "))

if work_hour<=40:
    grosspay= payrate*work_hour
    tax= (10/100)*grosspay
    weekly_earn= grosspay-tax
    print("My weekly pay is ",weekly_earn)
else:
    OT= input("Does your employer pay over time rate? YES or NO ")
    if OT == "YES":
        over_time_hr= work_hour-40
        over_time_pay= over_time_hr*1.5*payrate
        ot_tax= (12/100)*over_time_pay
        tax=(10/100)*(40*payrate)
        weekly_earned = ((40*payrate)-tax)+(over_time_pay-ot_tax)
        print("My weekly pay is ",weekly_earned)
    else:
        over_time_hr= work_hour-40
        over_time_pay= over_time_hr*payrate
        ot_tax= (12/100)*over_time_pay
        tax=(10/100)*(40*payrate)
        weekly_earned = ((40*payrate)-tax)+(over_time_pay-ot_tax)
        print("My weekly pay is ",weekly_earned)

        
    
