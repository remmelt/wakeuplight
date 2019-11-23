#!/usr/bin/python

from dotstar import Adafruit_DotStar

numpixels = 60 # Number of LEDs in strip
datapin  = 10
clockpin = 11
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)
strip.begin()           # Initialize pins for output

strip.setBrightness(1)

rgb = "ffbf00"
grb = "0x" + rgb[2:4] + rgb[0:2] + rgb[4:]

for x in range(0, numpixels):
	strip.setPixelColor(x, int(grb, 16))

strip.show()

