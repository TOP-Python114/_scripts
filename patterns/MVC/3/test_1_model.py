from decimal import Decimal as dec
import mvc


def test_init_product_type():
    model = mvc.ModelBasic([])
    assert model.item_type == 'product'


def test_create_item():
    model = mvc.ModelBasic([])
    test_dict = {
        'name': 'Bread',
        'price': dec('45.00'),
        'qasdntity': 20,
    }
    model.create_item(**test_dict)
    assert test_dict in mvc.storage.items
