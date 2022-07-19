from machine import Pin

relay = Pin(22, Pin.OUT)

def status():
    return "on" if relay.value() == 1 else "off"

def set_status(status :str):
    if status != "on" and status != "off":
        return None
    
    relay.value(0 if status == "off" else 1)
    return status
    
def toggle():
    relay.value(0 if relay.value() else 1)
