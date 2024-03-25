import pytest
from typing import List


class Card:
    """Одна карта, только цвет и число, без специальных карт."""
    COLORS = ['r', 'b', 'g', 'y']
    NUMBERS = list(range(10)) + list(range(1, 10))

    def __init__(self,color: str, number: int):
        self.color: str = color
        self.number: int = number

    def __repr__(self) -> str:
        return f'{self.color}{self.number}'

    def __eq__(self, other):
        """ Равен self карте other?"""
        if self.color == other.color and self.number == other.number:
            return True
        else:
            return False

    def can_paly_on(self, other) -> bool:
        """Проверяет, можно ли играть карту self на карту other. Тогда возвращает True."""
        if self.color == other.color or self.number == other.number:
            return True
        else:
            return False

    @staticmethod
    def create(text: str):
        """ Из строки text='b2' возвращает карту Card('b', 2)"""
        # c = Card.create('b2')
        col = text[0]       # b
        num = int(text[1])  # 2
        tmp = Card(col, num)
        return tmp

    @staticmethod
    def all_cards(colors: List[str] = None, numbers: List[int] = None):
        if colors is None:
            colors = Card.COLORS
        if numbers is None:
            numbers = Card.NUMBERS
        a = []
        for col in colors:
            for n in numbers:
                c = Card(col, n)
                print(c)
                a.append(c)
        return a

test_deck = Card.all_cards(['r', 'g'], [5, 6, 7])
full_deck = Card.all_cards()



