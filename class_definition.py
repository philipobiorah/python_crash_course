class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self) -> str:
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
        



jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)