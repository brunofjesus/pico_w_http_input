import time
import network

wlan = network.WLAN(network.STA_IF)
        
def active(enable :bool):
    wlan.active(enable)

def is_active():
    return wlan.active()

def ifconfig():
    return wlan.ifconfig()

def is_connected():
    return wlan.isconnected()
    
def connect(ssid :str, password: str, debug = False):
    active(True)
    wlan.connect(ssid, password)

    # Wait for connect or fail
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        if debug:
            print('waiting for connection...')
        time.sleep(1)

    # Handle connection error
    if wlan.status() != 3:
        raise RuntimeError('network connection failed')
    elif debug:
        print('connected')
        status = wlan.ifconfig()
        print( 'ip = ' + status[0] )

