# module for sensor readings
# Here a random number generator is used as sensory inputs but can be later
# swapped for actual readings like from like a DS18B20 or Arduino

import random

def get_temp():
    return round(random.uniform(20,30),2) # temp in °C