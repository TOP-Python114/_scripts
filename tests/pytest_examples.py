from numbers import Real


def adder(a: Real, b: Real):
    return a + b

def subber(a: Real, b: Real):
    return a - b


global_var = 10


def test_adder():
    assert adder(global_var, 5) == 0

def test_subber():
    assert subber(global_var, 6) == 4


print('Завершение работы скрипта')
