from abc import ABC


class Fruit(ABC):
    def draw(self, visitor: 'FruitVisitor'):
        visitor.visit(self)

class Apple(Fruit):
    pass

class Pear(Fruit):
    pass

class Pineapple(Fruit):
    pass


class FruitVisitor:
    def visit(self, fruit: Fruit):
        methods = {
            Apple: self.draw_apple,
            Pear: self.draw_pear
        }
        method = methods.get(fruit.__class__, self.draw_unknown)
        return method()

    @staticmethod
    def draw_apple():
        print('яблоко')

    @staticmethod
    def draw_pear():
        print('груша')

    @staticmethod
    def draw_unknown():
        print('фрукт')


fv = FruitVisitor()

apple = Apple()
apple.draw(fv)

pear = Pear()
pear.draw(fv)

pa = Pineapple()
pa.draw(fv)
