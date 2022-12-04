from pathlib import Path
from sys import path
from json import load as jload

from collections.abc import Iterable


class A:
    @staticmethod
    def valid_input() -> bool:
        return input(' > ').isalpha()

a = A()

assert a.valid_input(), 'input should contain only letters'
print('\n1st test passed\n')

assert a.__class__ is type(a)
# if not (a.__class__ is type(a)):
#     raise AssertionError
print('\n2nd test passed\n')


script_dir = Path(path[0])

def read_data(data_path: Path):
    assert data_path.is_file()
    with open(data_path, encoding='utf-8') as filein:
        data = jload(filein)
    return data

def recursive_container_check(container: Iterable):
    if isinstance(container, dict):
        for key, val in container.items():
            if isinstance(val, str):
                assert bool(val), f"{key!r} should not contain an empty string"
            elif isinstance(val, Iterable):
                assert bool(val), f"{key!r} should not contain an empty container"
                recursive_container_check(val)
    elif isinstance(container, list):
        for elem in container:
            if isinstance(elem, str):
                assert bool(elem), f"{elem!r} should not be an empty string"
            elif isinstance(elem, Iterable):
                assert bool(elem), f"{elem!r} should not be an empty container"
                recursive_container_check(elem)
    return True


for taxon in read_data(script_dir / 'parameters.json').values():
    assert recursive_container_check(taxon)

