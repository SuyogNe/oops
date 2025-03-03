class Parrot:
    species="Bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
    
blu=Parrot("Panda",10)
print(blu.sing("Happy"))
print(blu.dance())