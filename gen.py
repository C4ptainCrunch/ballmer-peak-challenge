DECK = list(range(2, 15))
COLORS = ["diamond", "heart", "spade", "club"]

def hands():
    pairs = {frozenset([(num, c),(num, c2)]) for num in DECK for c in COLORS for c2 in COLORS if c2 != c}

    two_pairs = {p1.union(p2) for p1 in pairs for p2 in pairs if len(p1.union(p2)) == 4}

    triples = {frozenset([(num, c),(num, c2), (num, c3)]) for num in DECK for c in COLORS for c2 in COLORS if c2 != c for c3 in COLORS if c3 not in (c, c2)}
    quadr = {frozenset([(num, c) for c in COLORS]) for num in DECK}

    flush = {
        frozenset([
            (n1, c),
            (n2, c),
            (n3, c),
            (n4, c),
            (n5, c),
        ])
        for c in COLORS
        for n1 in DECK
        for n2 in DECK if n2 != n1
        for n3 in DECK if n3 not in (n1, n2)
        for n4 in DECK if n4 not in (n1, n2, n3)
        for n5 in DECK if n5 not in (n1, n2, n3, n4)
    }

    fh = {
        p.union(t)
        for p in pairs
        for t in triples
        if list(p)[0][0] != list(t)[0][0]
    }

    straight = {
        frozenset([
            (start, c1),
            (start+1, c2),
            (start+2, c3),
            (start+3, c4),
        ])
        for start in DECK[:-4]
        for c1 in COLORS
        for c2 in COLORS
        for c3 in COLORS
        for c4 in COLORS
    }

    straight_flush = {
        frozenset([
            (start, c),
            (start+1, c),
            (start+2, c),
            (start+3, c),
            (start+4, c),
        ])
        for start in DECK[:-5]
        for c in COLORS
    }

    royal_flush = {
        frozenset([
            (10, c),
            (10+1, c),
            (10+2, c),
            (10+3, c),
            (10+4, c),
        ])
        for c in COLORS
    }

    return [
        royal_flush,
        straight_flush,
        quadr,
        fh,
        flush,
        straight,
        triples,
        two_pairs
    ]

HANDS_TYPES = hands()

def api_to_hand(j):
    return frozenset([
        (card['rank'], card['suit']) for card in j['hand']
    ])

def what_to_drop(my_hand):
    for i, tp in enumerate(HANDS_TYPES):
        for hand in tp:
            diff = hand - my_hand
            if len(diff) <= 1:
                return my_hand - hand

    for i, tp in enumerate(HANDS_TYPES):
        for hand in tp:
            diff = hand - my_hand
            if len(diff) <= 2:
                return my_hand - hand

    for i, tp in enumerate(HANDS_TYPES):
        for hand in tp:
            diff = hand - my_hand
            if len(diff) <= 3:
                return my_hand - hand

    return my_hand


def drop_to_index(hand, drop):
    indexes = []
    for card in hand['hand']:
        if (card['rank'], card['suit']) in drop:
            indexes.append(card['index'])

    return indexes
