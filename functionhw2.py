#This is by Dillon John(13)
def main():
    x1=int(input("Enter x1: "))
    x2=int(input("Enter x2: "))
    y1=int(input("Enter y1: "))
    y2=int(input("Enter y2: "))
    distance(x1,x2,y1,y2)
def distance(x1,x2,y1,y2):
    d=(((x1-x2)**2)+((y2-y1)**2))**(1/2)
    value=('The distance is: ',d)
    print(value)
main()
    
    
    
