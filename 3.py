# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid:
    def __init__(self, a_side, b_side, c_side):
        self.a_side = a_side
        self.b_side = b_side
        self.c_side = c_side

    def getSurface(self):
        #   TSA= 2(ab + bc +ca)
        return 2*(self.a_side*self.b_side + self.b_side*self.c_side + self.c_side*self.a_side)

    def getVolume(self):
        # V = a * b* c
        return self.a_side * self.b_side * self.c_side


teglalap = Cuboid(10,5,4)
print(teglalap.getSurface())
print(teglalap.getVolume())
