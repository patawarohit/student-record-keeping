class Animal:

    def __init__(self, name, no_of_legs ):
        self.name=name
        self.no_of_legs = no_of_legs

    def get_name(self):
        return self.name
class Bird(Animal):

    def __init__(self, name, no_of_legs, can_fly):
        super().__init__(name,no_of_legs)
        self.can_fly= can_fly


duck = Bird("Tom", 4, True)
#print(duck.name)
print(duck.get_name())
print(duck.no_of_legs)
print(duck.can_fly)
    