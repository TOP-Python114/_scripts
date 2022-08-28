from random import shuffle

class Test:
    cls_attr1 = 10
    cls_attr2 = 'abc'
    
    def __init__(self, alphanum_t: tuple):
        self.inst_attr1 = 0.001
        self.inst_attr2 = alphanum_t
    
    def shuf(self):
        q = list(self.inst_attr2)
        shuffle(q)
        self.inst_attr2 = tuple(q)


t1 = Test(('Z1', 'Y2', 'X3'))
print(f'\nпространство имён\n{t1.__dict__ = }')
scope = [name for name in dir(t1) if not name.startswith("__")]
print(f'\nобласть видимости\n{scope = }')

# Test(*args, **kwargs)
# Test.__new__() -> создаёт объект экземпляра
# объект экземпляра -> self 
# Test.__init__(self, *args, **kwargs)

t1.shuf()
print(f'\n{t1.inst_attr2 = }')

# метод осуществляет подмену вызова

# Пример:
#   t1.shuf() -> Test.shuf(t1)

# Общий вид:
#   inst_obj.method() -> ClsObj.function(inst_obj)

t2 = Test(('Я1', 'Ю2', 'Э3'))
t2.shuf()
print(f'\n{t2.inst_attr2 = }')
