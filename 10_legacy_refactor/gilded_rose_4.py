from typing import Iterable
from item import Item


"""Created two helper func
decrease_item_quality() n increase_item_quality()
to help clean code n indentation"""


# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)


def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(max_quality, item.quality + amount)


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    if item.name != SULFURAS:
        item.sell_in = item.sell_in - 1

    if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
        if item.name != SULFURAS:
            decrease_item_quality(item)
    else:
        increase_item_quality(item)
        if item.name == BACKSTAGE_PASSES:
            if item.sell_in < 10:
                increase_item_quality(item)
            if item.sell_in < 5:
                increase_item_quality(item)
    if item.sell_in < 0:
        if item.name != AGED_BRIE:
            if item.name != BACKSTAGE_PASSES:
                if item.name != SULFURAS:
                    decrease_item_quality(item)
            else:
                item.quality = 0
        else:
            increase_item_quality(item)
