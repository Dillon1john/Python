#remember that list placement always starts with 0 so if the list is[A,B,C,D] "A" is 0 "B" is 1 "C" is 2 "D" is 3
x=[3,5,100,7,3]
print(x)
c=x.append(50)#adds 50 to end of list
print(x)

y=[1,20]
d=x.extend(y)#extends list to end of list
print(x)

w=2
v=4
i=x.insert(2,4)#inserts "4" into the second spot
print(x)

t=x.sort(reverse=True)#sorts list in order
print(x)

p=x.pop(1)#removes the number thats in the first placement
print(x)

num=x.count(3)#counts how many times 3 repeats in list
print(num)

ma=max(x)#prints final number in list
print(ma)

mi=min(x)#prints out first number in list
print(mi)
