import requests

BASE = "http://172.23.218.41:5000/video_poker/api/"
TOKEN = "bf4ddaefdg12e322d311"

def info():
    r = requests.get(BASE + "team/" + TOKEN)
    return r.json()

def refill():
    r = requests.get(BASE + "refill/" + TOKEN)
    return r.json()


def step1(bet):
    if info()['step'] != 0:
        raise RuntimeError("Not good step")
    r = requests.post(BASE + "game/" + TOKEN, data={'bet':bet})
    return r.json()

def step2(exchange):
    if info()['step'] != 1:
        raise RuntimeError("Not good step")
    ex = "".join(map(lambda x: str(x), exchange))
    r = requests.post(BASE + "game/" + TOKEN, data={'exchange':ex})
    return r.json()
