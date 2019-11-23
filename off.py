from driver import apa102

NUM_LEDS = 60
ORDER = 'rgb'

strip = apa102.APA102(num_led=NUM_LEDS, order=ORDER)
strip.clear_strip()
strip.cleanup()

