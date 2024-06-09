#polys

class vehical:
    brand="honda"
    chechisno=10
    def details(self,m):
        self.brand=m
        print(f"Car name is {self.brand}")

    def details(self,c):
        self.chechisno=c
        print(f"Car chechis number is {self.chechisno}")

v=vehical()
v.details("suzuki")
v.details(1020)
