class Fruit:
    def __init__(self, color, flavor) -> None:
        self.color = color
        self.flavor = flavor
    def __str__(self) -> str:
        return "Color: {} , Flavor{}".format(self.color, self.flavor)
    
        

class Apple(Fruit):
    pass


class Grape(Fruit):
    pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")


print(granny_smith)
print(carnelian)