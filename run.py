from ops import *
from gen import *
import time

for i in range(100):
    if info()['step'] != 0:
        step2([])
    if info()['balance'] < 50:
        refill()
    cards = step1(50)
    tuples = api_to_hand(cards)
    drops = what_to_drop(tuples)
    exchange = drop_to_index(cards, tuples)
    print cards["hand"]
    print drops
    res = step2(exchange)
    print "%i %i" % (res['payout'], res['balance'])
    time.sleep(0.5)


