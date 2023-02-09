class Animal:
    def __init__(self,name) -> None:
        self.name = name
    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')

class Cat(Animal):
    def talk(self):
        print('Meow!')


a = Cat('cat')
a.talk()