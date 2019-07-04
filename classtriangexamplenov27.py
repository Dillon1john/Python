import math
class Triangle:
    kind ='right angle'
    def __init__(self, adjacent, opposite):
        self.opposite= opposite
        self.adjacent= adjacent 
    def hypo(self):
        hypotenus=((self.opposite**2)+(self.adjacent**2))**0.5
        return hypotenus
    def angle(self):
        theta= math.degrees(math.atan((self.opposite)/(self.adjacent)))
        return theta
side_a= int(input("Please enter the length of the side of the triangle: "))
side_b= int(input("Please enter the length of the other side: "))
hyp= Triangle(side_a, side_b)
#ang= Triangle(side_a, side_b, hyp)
print("The hypotenus of this ", hyp.kind, hyp.hypo())
print("Thr angle between hypotenus and adjacent of his ", hyp.kind, hyp.angle())
