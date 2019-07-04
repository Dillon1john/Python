def pythagorasTheorem(o,a):
    hyp=(((o**2)+(a**2))**.5)
    c=("The value of c is: ",hyp)
    print(c)
def main():
       o=float(input("Enter value of opposite: "))
       a=float(input("Enter value of adjacent: "))
       pythagorasTheorem(o,a)
main()
