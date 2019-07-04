x=float(input("Enter minimum: "))
y=float(input("Enter maximum: "))
while x<=y:
    a=2**x
    b=x**2
    c=2*x
    d=x**(1/2)
    print(x,"\t",a,"\t",b,"\t",c,"\t",d,'\n')
    x=x+1
