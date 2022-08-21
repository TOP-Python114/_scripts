from typing import Callable


def decor(func_obj: Callable) -> Callable:
    
    # print(locals(), end='\n\n')
    
    def _wrapper():
        print('декоратор: до вызова функции')
        func_obj()
        print('декоратор: после вызова функции')
    
    # print(locals(), end='\n\n')
    
    return _wrapper


def test_func() -> None:
    print('функция: вызов функции')


res = decor(test_func)

# >>> res
# <function decor.<locals>._wrapper at 0x000002437700E560>
# >>>
# >>> type(res)
# <class 'function'>
# >>>
# >>> res()
# декоратор: до вызова функции
# функция: вызов функции
# декоратор: после вызова функции

test_func = decor(test_func)


@decor
def test_func2() -> None:
    """Вторая демонстрационная функция."""
    print('функция 2: вызов функции')


print(f'{test_func2.__name__ = }')
print(f'{test_func2.__doc__ = }')
