#Display any number of sum problems with a function.
#Handle keyboard input separately
def sumProblem(x, y):
    sum= x+y
    sentence= ("The sum of x and y is", sum)
    print (sentence)
def main():
    sumProblem(2, 3)
    sumProblem(1234567890123,535790269358)
    a=input("Enter an integer: ")
    b=input("Enter another integer: ")
    sumProblem(a, b)
main()
