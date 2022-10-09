from typing import Callable, Any


def decorator_generator(arg1, arg2) -> Callable:
    print('это генератор декораторов')
    print('он принял аргументы:', arg1, arg2)

    def parametrized_decorator(function_object: Callable) -> Callable:
        print('\tэто декоратор')
        print('\tон видит аргументы, переданные в генератор:', arg1, arg2)

        def _wrapper(*args: Any, **kwargs: Any) -> Any:
            print('\t\tэто обёртка декорируемой функции')
            print('\t\tона также видит аргументы, переданные в генератор', arg1, arg2)
            ret = function_object(*args, **kwargs)
            print(f'\t\tэто возвращаемое значение декорируемой функции: {ret}')
            return ret

        return _wrapper

    return parametrized_decorator


def test():
    print('\t\t\tэто декорируемая функция')
    print('\t\t\tона видит только аргументы, переданные непосредственно ей')

decorator = decorator_generator(3.14, 'ПАРАМ-ПАМ-ПАМ')
test = decorator(test)
# test = decorator_generator(3.14, 'ПАРАМ-ПАМ-ПАМ')(test)
test()

print('\n')

@decorator_generator((1, 2, 3), True)
def test2():
    print('\t\t\tэто декорируемая функция 2')
    print('\t\t\tона видит только аргументы, переданные непосредственно ей')

test2()
