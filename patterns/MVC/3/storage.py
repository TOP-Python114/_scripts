"""Реализация CRUD операций."""

from decimal import Decimal as dec

class ItemNotStored(Exception):
    pass

class ItemAlreadyStored(Exception):
    def __init__(self, item_name: str):
        super().__init__(f'"{item_name}" already stored!')


# хранилище
items: list[dict] = []


def create_item(name: str, price: dec, quantity: int):
    global items
    results = tuple(filter(
        lambda item: item['name'] == name,
        items
    ))
    if not results:
        items.append({'name': name, 'price': price, 'quantity': quantity})
    else:
        raise ItemAlreadyStored(name)


def create_items(items_to_add: list[dict]):
    global items
    items = items_to_add


def read_item(name):
    global items
    results = tuple(filter(
        lambda item: item['name'] == name,
        items
    ))
    if results:
        return results[0]
    else:
        raise ItemNotStored(f'Can\'t read "{name}" because it\'s not stored')


def read_items():
    global items
    return [item for item in items]


def update_item(name: str, price: dec, quantity: int):
    global items
    indexed_items = tuple(filter(
        lambda i_item: i_item[1]['name'] == name,
        enumerate(items)
    ))
    if indexed_items:
        i = indexed_items[0][0]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise ItemNotStored(f'Can\'t update "{name}" because it\'s not stored')


def delete_item(name):
    global items
    indexed_items = tuple(filter(
        lambda i_item: i_item[1]['name'] == name,
        enumerate(items)
    ))
    if indexed_items:
        i = indexed_items[0][0]
        del items[i]
    else:
        raise ItemNotStored(f'Can\'t delete "{name}" because it\'s not stored')


if __name__ == '__main__':
    my_items = [
        {'name': 'bread', 'price': dec('0.5'), 'quantity': 20},
        {'name': 'milk', 'price': dec('1.0'), 'quantity': 10},
        {'name': 'wine', 'price': dec('10.0'), 'quantity': 5},
    ]

    # CREATE
    create_items(my_items)
    create_item('beer', price=dec('3.0'), quantity=15)
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ items')
    print(read_items())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ bread')
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=dec('2.0'), quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())
