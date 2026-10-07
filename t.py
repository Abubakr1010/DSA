class Drive:

    def __init__(self, name):
        self.name = name

    def car(self):
        print(self.name)

    def __str__(self):
        return(f"{self.name}")


c = Drive("vx")
c.car()

print(str(c))



