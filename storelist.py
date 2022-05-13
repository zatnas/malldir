from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from store import Store


@dataclass
class StoreList:
    stores: list['Store']
