def quadraticPlus(a,b,c):
    x=((-b)+(((b**2)-4*a*c)**.5))/(2*a)
    value=("answer 1: ",x)
    print(value)
def quadraticMinus(a,b,c):
    x=((-b)-(((b**2)-4*a*c)**.5))/(2*a)
    value=("answer 2: ",x)
    print(value)
def main():
    a= int(input("Enter the value of a: "))
    b=int(input("Enter the value of b: "))
    c= int(input("Enter the value of c: "))
    quadraticPlus(a,b,c)
    quadraticMinus(a,b,c)
main()
