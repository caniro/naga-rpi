import spidev
from requests import get
from threading import Thread
from time import sleep
from config import SERVER_HOST, HOSTNAME

SMOKE_BOUNDARY = 450
SMOKE_INTERVAL = 1
SMOKE_SERVER_URL = 'http://' + SERVER_HOST + ':8000/sensor/smoke'
SMOKE_CHANNEL = 0

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def read_adc(adcnum):
    if adcnum < 0 or adcnum > 7:
        return -1

    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def check_smoke():
    while True:
        smoke_value = read_adc(SMOKE_CHANNEL)
        print(f"smoke sensor value: {smoke_value}")
        sleep(SMOKE_INTERVAL)
        if smoke_value > SMOKE_BOUNDARY:
            try:
                res = get(SMOKE_SERVER_URL + f'?camera={HOSTNAME}')
            except Exception as e:
                print('error:', e)

thread = Thread(target=check_smoke)
thread.start()
