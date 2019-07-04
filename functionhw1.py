#This is by Dillon John(13)
def cylinder(h,r,π):
    v=π*(r**2)*h
    volume=("The volume of cylinder: ",v)
    print(volume)
def circle(h,r,π):
    v=π*(r**2)
    volume=("The volume of circle: ",v)
    print(volume)
def cone(h,r,π):
    v=π*(r**2)*(h/3)
    volume=("The volume of cone: ",v)
    print(volume)
def sphere(h,r,π):
    v=(4/3)*π*(r**3)
    volume=("The volume of sphere: ",v)
    print(volume)
def main():
    h=int(input("Enter height: "))
    r=int(input("Enter radius: "))
    π=3.14159265359
    cylinder(h,r,π)
    circle(h,r,π)
    cone(h,r,π)
    sphere(h,r,π)
main()
