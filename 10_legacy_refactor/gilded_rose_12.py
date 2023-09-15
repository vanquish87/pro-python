from typing import Iterable
from item import Item
from models import AgedBrieUpdater, BackstagePassesUpdater, SupfurasUpdater, DefaultItemUpdater

"""Cleaned up code into 3 files
models.py n utils.py
"""

# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


ITEM_UPDATER = {AGED_BRIE: AgedBrieUpdater(), BACKSTAGE_PASSES: BackstagePassesUpdater(), SULFURAS: SupfurasUpdater()}


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    item_updater = ITEM_UPDATER.get(item.name, DefaultItemUpdater())

    item_updater.update_sell_in(item)
    item_updater.update_quality(item)
