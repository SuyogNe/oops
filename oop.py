class birds:
    species="Bird"
    def __init__(self, name, color):
        self.name=name
        self.color=color

par=birds("Parrot","Green")
spa=birds("Sparrow","Brown")

print("Par is a {} and is of color {}".format(par.name,par.color))
print("Spa is a {} and is of color {}".format(spa.name,spa.color))
print("Both are of species {}".format(birds.species))