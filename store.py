from dataclasses import dataclass


@dataclass
class Store:
    name: str
    location: str
    image_url: str
    page_url: str