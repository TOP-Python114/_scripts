from pprint import pprint


class Cat:
    def meow(self):
        return 'мяу'

class Dog:
    @staticmethod
    def bark():
        return 'гав'

class Human:
    @staticmethod
    def speak():
        return 'привет'

class Car:
    @staticmethod
    def move(speed: int = 60):
        return 'вр' + 'у'*(speed//20) + 'м'


class Adapter:
    def __init__(self, obj, **methods):
        self.obj = obj
        self.__dict__.update(methods)

    def __getattr__(self, item):
        return getattr(self.obj, item)


cat = Cat()
dog = Dog()
pers = Human()
car = Car()

cat_adapted = Adapter(cat, make_noise=cat.meow)
dog_adapted = Adapter(dog, make_noise=dog.bark)
pers_adapted = Adapter(pers, make_noise=pers.speak)
car_adapted = Adapter(car, make_noise=car.move)

global_namespace = globals().items()
adapted = [
    obj
    for name, obj in global_namespace
    if name.endswith('adapted')
]
for obj in adapted:
    pprint(obj.__dict__)
    print(f'{obj.make_noise()}\n')
