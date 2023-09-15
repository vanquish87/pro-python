from typing import Iterable
from item import Item


"""Strings are converted into CONSTANTS to avoid typos n 
have more readability n scalability"""


# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    if item.name != SULFURAS:
        item.sell_in = item.sell_in - 1

    if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
        if item.quality > 0:
            if item.name != SULFURAS:
                item.quality = item.quality - 1
    else:
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.name == BACKSTAGE_PASSES:
                if item.sell_in < 10:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.sell_in < 5:
                    if item.quality < 50:
                        item.quality = item.quality + 1
    if item.sell_in < 0:
        if item.name != AGED_BRIE:
            if item.name != BACKSTAGE_PASSES:
                if item.quality > 0:
                    if item.name != SULFURAS:
                        item.quality = item.quality - 1
            else:
                item.quality = item.quality - item.quality
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
