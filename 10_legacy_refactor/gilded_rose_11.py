from typing import Iterable, Protocol
from item import Item


"""Adding abstraction to scale up the Items with
DefaultItemUpdater, AgedBrieUpdater, BackstagePassesUpdater, SupfurasUpdater
"""

# Item types
AGED_BRIE = "Aged Brie"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
SULFURAS = "Sulfuras, Hand of Ragnaros"


class ItemUpdater(Protocol):
    def update_quality(self, item: Item) -> None:
        ...

    def undate_sell_in(self, item: Item) -> None:
        ...


class DefaultItemUpdater:
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item)
        if item.sell_in < 0:
            decrease_item_quality(item)

    def update_sell_in(self, item: Item) -> None:
        item.sell_in = item.sell_in - 1


class AgedBrieUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 0:
            increase_item_quality(item)


class BackstagePassesUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        increase_item_quality(item)
        if item.sell_in < 10:
            increase_item_quality(item)
        if item.sell_in < 5:
            increase_item_quality(item)
        if item.sell_in < 0:
            item.quality = 0


class SupfurasUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        pass

    def update_sell_in(self, item: Item) -> None:
        pass


ITEM_UPDATER = {AGED_BRIE: AgedBrieUpdater(), BACKSTAGE_PASSES: BackstagePassesUpdater(), SULFURAS: SupfurasUpdater()}


def decrease_item_quality(item: Item, amount: int = 1) -> None:
    item.quality = max(0, item.quality - amount)


def increase_item_quality(item: Item, amount: int = 1, max_quality: int = 50) -> None:
    item.quality = min(max_quality, item.quality + amount)


def update_quality(items: Iterable[Item]):
    for item in items:
        update_quality_single(item)


def update_quality_single(item: Item):
    item_updater = ITEM_UPDATER.get(item.name, DefaultItemUpdater())

    item_updater.update_sell_in(item)
    item_updater.update_quality(item)
