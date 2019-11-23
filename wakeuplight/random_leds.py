#!/usr/bin/python

from dotstar import Adafruit_DotStar
from random import randint
import time

numpixels = 60 # Number of LEDs in strip
datapin  = 10
clockpin = 11
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)
strip.begin()           # Initialize pins for output

strip.setBrightness(1)

rgb = "ff00ff"

grb = int("0x" + rgb[2:4] + rgb[0:2] + rgb[4:], 16)

states = [False]*(numpixels)

r = lambda: randint(0,255)
def generate_color(): 
	return int('0x%02X%02X%02X' % (r(),r(),r()), 16)

while True:
	x = randint(0, numpixels - 1)

	color = 0
	if states[x]:
		color = generate_color()

	states[x] = not states[x]

	strip.setPixelColor(x, color)
	strip.show()

	time.sleep(1.0 / 500)

