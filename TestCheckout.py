from checkout import Checkout
import pytest

@pytest.fixture(scope="function", autouse = True)
def checkout_instance():
    instance = Checkout()
    yield instance

def test_AddItemPrice(checkout_instance):
    checkout_instance.add_item_price("i", 5)


def test_AddItem(checkout_instance):
    checkout_instance.add_item("shoe")


def test_CalculateTotal(checkout_instance): 
    checkout_instance.add_item_price("shoe", 5)
    checkout_instance.add_item_price("bag", 6)
    total = checkout_instance.calculate_total()

    assert total == 11

def test_CalculateTotalWithMultipleItems(checkout_instance): 
    checkout_instance.add_item_price("shoe", 5)
    checkout_instance.add_item_price("bag", 6)
    checkout_instance.add_item("house")
    checkout_instance.add_item("battery")
    total = checkout_instance.calculate_total()

    assert total == 11
