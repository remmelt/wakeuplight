from driver import apa102
from random import choice
from time import sleep

STAR_COLORS=[0x010000, 0x0b0000, 0x8B0000, 0xFF4500, 0xFF8C00]
BRIGHTNESS = 10
SLEEP_BETWEEN_STARS = 3
SLEEP_BETWEEN_CYCLES = 1
SLEEP_AFTER = 15 * 60 # 15 min

NUM_LEDS = 60
ORDER = 'rgb'

def glow_state(strip, state, color, brightness):
    for i in range(0, NUM_LEDS):
        if not i in state:
            strip.set_pixel_rgb(i, color, bright_percent=brightness)
    strip.show()

def random_stars(strip, color, brightness):
    state = list(range(0, NUM_LEDS))
    while len(state) > 0:
        state.remove(choice(state))
        glow_state(strip, state, color, brightness)
        sleep(SLEEP_BETWEEN_STARS)

strip = apa102.APA102(num_led=NUM_LEDS, order=ORDER)
strip.clear_strip()

random_stars(strip, 0x010000, 1)
sleep(SLEEP_BETWEEN_CYCLES)

for color in STAR_COLORS:
    print(color)
    random_stars(strip, color, BRIGHTNESS)
    sleep(SLEEP_BETWEEN_CYCLES)

for brightness in [20, 30, 40, 50, 80, 100]:
    print(brightness)
    random_stars(strip, STAR_COLORS[-1], brightness)
sleep(SLEEP_BETWEEN_CYCLES)

sleep(SLEEP_AFTER)
strip.clear_strip()
strip.cleanup()

