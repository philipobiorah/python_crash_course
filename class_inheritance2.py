class Animal:
    sound = ""
    def __init__(self, name) -> None:
        self.name = name
    def speak(self):
        print("{sound} I'am {name}! {sound}".format(name = self.name, sound= self.sound))

class Piglet(Animal):
    sound = "Oink!"


hamlet = Piglet("Hamlet")
hamlet.speak()


class Cow(Animal):
    sound = "Moooo"

milky = Cow("Milky White")
milky.speak()