class vehical:
    brand="honda"
    def p(self):
        print("Hello Car lover !Whats up ")

class car(vehical):
     def details(self,mod):
         self.model=mod
         print(f"{self.brand}"+" "+f"{self.model}")


#object c
c=car()
c.p()
c.details("shiba")