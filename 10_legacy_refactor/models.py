from item import Item
from typing import Protocol
from utils import decrease_item_quality, increase_item_quality


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


class ConjureUpdater(DefaultItemUpdater):
    def update_quality(self, item: Item) -> None:
        decrease_item_quality(item, 2)
        if item.sell_in < 0:
            decrease_item_quality(item, 2)
