# Pico W HTTP Relay

Control a relay (or any other output) via HTTP

# HTTP Endpoints

 - **/on**: turns the input on
 - **/off**: turns the input off
 - **/status**: outputs the status

 As of now you can use any method (POST, GET, PUT), they will all do the same.


# Configuration

This program gets the configs from the `config.json` file in the pico, you can either place a configured one or you can just connect to your machine USB port and configure it via the serial connection (with minicom, cutecom or similar).

The following commands are supported via serial:
 - **set:ssid:** *your_ssid*: set wifi SSID to connect to
 - **set:pass:** *your_password*: set wifi password
 - **set:debug:** *1/0*: activate debug messages
 - **set:relay:** *on/off/status*: same as the HTTP endpoints
 - **ifconfig**: print network information

The pin is hardcoded to GP22 on `relay.py`, I will maybe add that to the configs.


# Limitations

Right now this only supports 1 input, I'll probably change this in order to support more inputs if I feel the need for it.
