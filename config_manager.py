import io
import json

    
def read():
    file = open("config.json", 'r')
    content = json.load(file)
    file.close()
    return content

def write(prop, value):
    configs = read()
    configs[prop] = value
    
    file = open("config.json", 'w')
    json.dump(configs, file)
    file.close()
