def salary(wrkhrs,payrate):
    finalpay=wrkhrs*payrate
    print("Your salary for this week is",finalpay)
def overtimesalary(wrkhrs,payrate):
    overtimepay=(wrkhrs+2)*payrate
    print("Your salary for this week is",overtimepay)
def main():
    wrkhrs=int(input("Enter your work hours: "))
    payrate=int(input("Enter your payrate: "))
    if wrkhrs>=40:
        overtimesalary(wrkhrs,payrate)
    else:
        salary(wrkhrs,payrate)
main()
 
