class Dog:
    kind ='canine'
    def __init__(self, name, weight):
        self.name= name
        self.weight= weight
    def bark(self,num):
        if (self.weight< 4):
            sound = "yip "*num
        else:
            sound = "ruff "*num
        return(sound)
d= Dog('Fido',10)
g= Dog('Fifi',2)
print (d.name+":",d.bark(3))
print (g.name+":",g.bark(6))
print (d.name+" is a "+d.kind+" and so is "+g.name+".")
