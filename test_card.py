from uno.card import Card


def test_create_card():
    c = Card('b', 2)
    assert c.color == 'b'
    assert c.number == 2

def test_card_print():
    c = Card('b', 2)
    assert repr(c) == 'b2'

def test_play_on():
    top = Card('b', 2)
    c1 = Card('b', 8)   # color
    c2 = Card('g', 2)   # number
    c3 = Card('b', 2)
    c4 = Card('y', 9)   # нельзя играть

    assert c1.can_paly_on(top)
    assert c2.can_paly_on(top)
    assert c3.can_paly_on(top)
    assert not c4.can_paly_on(top)

def test_create_from_str():
    c = Card.create('b2')
    assert c.color == 'b'
    assert c.number == 2

def test_negative_create():
    # TODO что делать и как проверить???
    c = Card('q', 123)

def test_equal():
    c1 = Card('b', 8)   # color
    c2 = Card('g', 2)   # number
    c3 = Card('b', 2)
    c = Card('b', 8)
    assert c1 != c2
    assert c1 != c3
    assert c1 == c

def test_all_cards():
    deck = Card.all_cards(['b', 'y'], [5, 6, 7])
    print(deck)
    assert deck[0] == Card('b', 5)
    assert deck[1] == Card('b', 6)
    assert deck[2] == Card('b', 7)

    assert deck[3] == Card('y', 5)
    assert deck[4] == Card('y', 6)
    assert deck[5] == Card('y', 7)


