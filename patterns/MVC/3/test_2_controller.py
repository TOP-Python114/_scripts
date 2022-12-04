import mvc


my_items = [
    {'name': 'bread', 'price': 0.5, 'quantity': 20},
    {'name': 'milk', 'price': 1.0, 'quantity': 10},
    {'name': 'wine', 'price': 10.0, 'quantity': 5},
]


def test_update_data():
    ctrl = mvc.Controller(mvc.ModelBasic(my_items), mvc.View())
    test_dict = {
        'name': 'bread',
        'price': 45.00,
        'quantity': 20
    }
    ctrl.update_item(**test_dict)
    assert test_dict in mvc.storage.items
