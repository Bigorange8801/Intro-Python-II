# Implement a class to hold room information. This should have name and
# description attributes.

class Player :
    def __init__(self,name,age,char):
        self.name = name
        self.age = age
        self.char = char

p1 = Player("Sonic", 29 , "Hedgehog")

print(p1.name)
print(p1.age)
print(p1.char)
