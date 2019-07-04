temp=70
humid=45
if(temp<60) or (temp>90) or (humid>50):
    print("Stay inside")
else:
    if (humid==100):
        print("It is raining outside")
    else:
        print("Do you want to take a walk?")
