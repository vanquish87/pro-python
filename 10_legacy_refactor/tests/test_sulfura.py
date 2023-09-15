from gilded_rose import update_quality
from item import Item

SULFURAS = "Sulfuras, Hand of Ragnaros"


def test_item_sulfuras_sell_in_doesnt_decrease():
    item = Item(SULFURAS, 1, 0)
    update_quality([item])
    assert 1 == item.sell_in


def test_item_sulfuras_quality_doesnt_decrease():
    item = Item(SULFURAS, 0, 0)
    update_quality([item])
    assert 0 == item.quality
