import class1

TestClass = class1.Test

tc1 = TestClass()

# TestClass.__new__() -> создаёт объект экземпляра self
# объект экземпляра self -> TestClass.__init__(self)

print(f'{tc1 = }\n{type(tc1) = }\n')
print('type(tc1) is TestClass')
print(type(tc1) is class1.Test is TestClass is tc1.__class__, end='\n\n')

for attr in dir(tc1):
    if not attr.startswith('__'):
        obj = getattr(tc1, attr)
        print(f'\t{attr}: {type(obj)}, {obj}')

print(f'\n{tc1.__dict__ = }\n')

print('tc1.attr1 is TestClass.attr1')
print(tc1.attr1 is TestClass.attr1)
print('tc1.attr2 is TestClass.attr2')
print(tc1.attr2 is TestClass.attr2)
print('tc1.attr3 is TestClass.attr3')
print(tc1.attr3 is TestClass.attr3)

tc1.attr4 = [1, 2, 3, 4]
tc1.attr5 = True
print(f'\n{tc1.__dict__ = }\n')

tc2 = TestClass()
print(f'{tc2.__dict__ = }\n')
