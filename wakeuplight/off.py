#!/usr/bin/python

from dotstar import Adafruit_DotStar

numpixels = 60 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin  = 10
clockpin = 11
strip    = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()           # Initialize pins for output
strip.setBrightness(0)

for x in range(0, numpixels):
	strip.setPixelColor(x, 0)
	strip.show()                     # Refresh strip

