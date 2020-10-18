class animal:
    def __init__(self,legs = 4, ears = 2, eyes = 2, mouthes = 1, noses = 1):
        self.legs = legs
        self.ears = ears
        self.eyes = eyes
        self.mouthes = mouthes
        self.noses = noses
        
    def info(self):
        print( "I have 4 legs, 2 eyes, 2 mouths, 1 nose and 1 mouth")

class dog(animal):
    def  sound(self):
        print('I Bark')
class cat(animal):
    def sound(self):
        print('I Purr')
class mouse(animal):
    def sound(self):
        print('I Squeak')
class hamster(animal):
    def sound(self):
        print('I Squeak')
class guinea_pig(animal):
    def sound(self):
        print('I Purr')
class rabbit(animal):
    def sound(self):
        print('I Squeak')
class turtle(animal):
    def sound(self):
        print('I Hiss') 
class horse(animal):
    def sound(self):
        print('I Whine')

tom = cat()
print(tom.legs, tom.ears)
tom.info()
tom.sound()
jerry = mouse()
jerry.info()
jerry.sound()
spike = dog()
spike.info()
spike.sound()


