##object oriented programming(OOP)##

#example1

class PartyAnimal:
    x = 0
    def party(self):
        self.x=self.x+1
        print('so far',self.x)
an = PartyAnimal()
an.party()
an.party()
an.party()

#example2

class PartyAnimal:
    x=0
    def party(self):
        self.x=self.x+1
        print('so far',self.x)
an = PartyAnimal()
print('Type',type(an))
print('Dir',dir(an))

#example3

class PartyAnimal:
    x=0
    def _init_(self):
        print('i am constructed')
    def party(self):
        self.x=self.x+1
        print('so far',self.x)
    def _del_(self):
        print('i am destructed',self.x)
an = PartyAnimal()
an.party()
an.party()
an=42
print('an contains',an)

#example4

class PartyAnimal:
    x = 0
    name = ''
    def _init_(self,z):
        self.name = z
        print(self.name,'constructed')
    def party(self):
        self.x=self.x+1
        print(self.name,'party count',self.x)
s = PartyAnimal('Sally')
j = PartyAnimal('Jim')
s.party()
j.party()
s.party()

#example5

class PartyAnimal:
    x=0
    name = ''
    def _init_(self,nam):
        self.name=nam
        print(self.name,'constructed')
    def party(self):
        self.x=self.x+1
        print(self.name,'party count',self.x)
    
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points= self.points +7
        self.party()
        print(self.name,'points',self.points)



