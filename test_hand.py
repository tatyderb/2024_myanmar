from uno.card import Card
from uno.hand import Hand
from uno.card import Card


def test_init():
    h = Hand()
    assert h.cards == []

def test_repr():
    h = Hand()
    h.cards.append(Card('b', 2))
    h.cards.append(Card('y', 7))
    assert repr(h) == 'b2 y7'

def test_add():
    h = Hand()
    c = Card('b', 2)
    h.add(c)
    c = Card('y', 7)
    h.add(c)
    c = Card('g', 0)
    h.add(c)

    # вариант 1 проверки
    assert h.cards[0] == Card('b', 2)
    assert h.cards[1] == Card('y', 7)
    assert h.cards[2] == Card('g', 0)

    # вариант 2 проверки
    assert repr(h.cards[0]) == 'b2'
    assert repr(h.cards[1]) == 'y7'
    assert repr(h.cards[2]) == 'g0'

    # вариант 3 проверки
    assert repr(h) == 'b2 y7 g8'

