from typing import Iterable
from item import Item
from models import AgedBrieUpdater, BackstagePassesUpdater, SupfurasUpdater, DefaultItemUpdater, ConjureUpdater

"""Adding 1 more Item
CONJURED
"""

# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"
CONJURED = "Conjured Mana Cake"

ITEM_UPDATER = {AGED_BRIE: AgedBrieUpdater(), BACKSTAGE_PASSES: BackstagePassesUpdater(), SULFURAS: SupfurasUpdater(), CONJURED: ConjureUpdater()}


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    item_updater = ITEM_UPDATER.get(item.name, DefaultItemUpdater())

    item_updater.update_sell_in(item)
    item_updater.update_quality(item)
