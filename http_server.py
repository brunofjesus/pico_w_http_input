import socket
import re

def serve(handler, debug = False):
    
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    if debug:
        print('listening on', addr)

    while True:
        try:
            cl, addr = s.accept()
            if debug:
                print('client connected from', addr)
            request = cl.recv(1024)
            request = str(request)
            
            pattern = ".*? \/(\w+)"
            
            path = re.search(pattern, request).group(1)

            response = handler(path)

            cl.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
            cl.send(response)
            cl.close()

        except OSError as e:
            cl.close()
            print('connection closed')
