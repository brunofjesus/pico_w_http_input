import sys
from utime import sleep

def start(handler):
    stmt = ""
    while True:
        char = None
        while char != chr(10):
            char = str(sys.stdin.buffer.read(1), 'utf-8')
            stmt = stmt + char
            sleep(0.1)
        handler(stmt[:-1])
        stmt = ""
        sleep(1)
