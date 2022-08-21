from typing import Callable


def decor(func_obj: Callable) -> Callable:
    def _wrapper(*args, **kwargs):
        # ...
        ret = func_obj(*args, **kwargs)
        # ...
        return ret
    return _wrapper


@decor
def test_func(a) -> None:
    print(f'{a!r}\n{a!s}')


class A:
    def __repr__(self):
        return super().__repr__()
    
    def __str__(self):
        return '!A!'


test_func(A())
