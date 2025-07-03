from typing import TypedDict

class Movie(TypedDict):
    name: str
    year: int


movie= Movie(name="Inception", year=2010)