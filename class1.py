class Test:
    attr1 = 10
    attr2 = 'BBB'

    def attr3():
        print('C3')

print(f'{Test = }\n{type(Test) = }\n')
print(f'{Test.__mro__}\n')
print(dir(Test), end='\n\n')

for attr in dir(Test):
    if not attr.startswith('__'):
        obj = getattr(Test, attr)
        print(f'\t{attr}: {type(obj)}, {obj}\n')

Test.attr3()

