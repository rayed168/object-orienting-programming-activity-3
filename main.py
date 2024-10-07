class Bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("My name is",self.name)
        print("My age is",self.age)
parrot=Bird("parrot",34)
parrot.display()
bird=Bird("Bird",35)
bird.display()