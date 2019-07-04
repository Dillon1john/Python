#Does multiplication table for inputed range
x=int(input("Enter minimum value: "))
y=int(input("Enter maximum value: "))
for i in range(x,y):
    for j in range(x,y):
        print(i*j,end='\t')
    print('')
