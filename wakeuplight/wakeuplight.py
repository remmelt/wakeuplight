#!/usr/bin/python

from dotstar import Adafruit_DotStar
import time

numpixels = 60
datapin = 10
clockpin = 11
strip = Adafruit_DotStar(numpixels, datapin, clockpin)
strip.begin()
strip.setBrightness(2)

multiplier = 255.0 / numpixels
for x in range(0, numpixels):
    color = '0x00{:02x}00'.format(int(multiplier * (x + 1)))
    rgb = 'FFA500'
    grb = int('0x' + rgb[2:4] + rgb[0:2] + rgb[4:], 16)

    # i = int(grb, 16)
    print rgb, grb
    strip.setPixelColor(x, grb)

strip.show()
