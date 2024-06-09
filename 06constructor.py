class vehical:
    aa=0
    bb=0
    def __init__(self):
        self.aa=15
        self.bb=14

    def p(self,c,d):
        print(self.bb)
        print(self.aa)
        sum=c+d
        return sum
v=vehical()
result = v.p(10,20)
print(result)
#output 
# 14
# 15
# 30
#the self parameter is a reference to the instance of the class, 
# allowing access to its attributes and methods