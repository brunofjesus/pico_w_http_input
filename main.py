from wlan import WLAN
import config_manager
import http_server
import relay
import internal_led
import console
import _thread

wlan_connection = None

def http_handler(path :str):
    if path == "status":
        status = relay.status()
    else:
        status = relay.set_status(path)
        if status == None:
            return """{"error": "cannot handle '%s'"}""" % path

    return """{"status": %s}""" % status

def console_handler(command :str):
    try:
        if command.startswith("set:ssid:"):
            config_manager.write("ssid", command[9:])
            print("set ssid to ", command[9:])
        elif command.startswith("set:pass:"):
            config_manager.write("pass", command[9:])
        elif command.startswith("set:debug:"):
            config_manager.write("debug", 1 if command[10:] == "1" else 0)
        elif command.startswith("relay:"):
            action = command[6:]
            if action == "on":
                relay.set_status(1)
            elif action == "off":
                relay.set_status(0)
            elif action == "status":
                print(relay.status())
        elif command == "ifconfig":
            print("Connection status")
            if wlan_connection:
                ifconfig = wlan_connection.ifconfig()
                print("IP: ", ifconfig[0])
                print("Subnet Mask: ", ifconfig[1])
                print("Gateway: ", ifconfig[2])
                print("DNS: ", ifconfig[3])
            else:
                print("Not connected")
    except Exception as e:
        if config_manager.read()['debug'] == 1:
            print(e)
        else:
            print("Unkown error")

if __name__ == "__main__":
    try:
        _thread.start_new_thread(console.start, (console_handler,))
        config = config_manager.read()
        if config['debug'] == 1:
            print(config)
        wlan_connection = WLAN(config['ssid'], config['password'], config['debug'] == 1)
        wlan_connection.connect()
        http_server.serve(handler=http_handler, debug=config['debug'] == 1)
    except Exception as e:
        print(e)
        internal_led.flash()
    
