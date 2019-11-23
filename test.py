from driver import apa102
from random import choice
from time import sleep

STAR_COLOR_1 = 0xFF8C00
STAR_COLOR_2 = 0xFFD700
STAR_COLOR_3 = 0xFFFFFF
BRIGHTNESS_1 = 1
BRIGHTNESS_2 = 10
BRIGHTNESS_3 = 100
SLEEP_BETWEEN_STARS = 0.05
SLEEP_BETWEEN_CYCLES = 1
SLEEP_AFTER = 5 * 60 # 5 min

NUM_LEDS = 60
ORDER = 'rgb'

def glow_state(strip, state, color, brightness):
    for i in range(0, 59):
        if not i in state:
            strip.set_pixel_rgb(i, color, bright_percent=brightness)
    strip.show()

def random_stars(strip, color, brightness):
    state = list(range(0, 60))
    while len(state) > 0:
        state.remove(choice(state))
        glow_state(strip, state, color, brightness)
        sleep(SLEEP_BETWEEN_STARS)

strip = apa102.APA102(num_led=NUM_LEDS, order=ORDER)
strip.clear_strip()
random_stars(strip, STAR_COLOR_1, BRIGHTNESS_1)
sleep(SLEEP_BETWEEN_CYCLES)
random_stars(strip, STAR_COLOR_2, BRIGHTNESS_2)
sleep(SLEEP_BETWEEN_CYCLES)
random_stars(strip, STAR_COLOR_3, BRIGHTNESS_3)

sleep(SLEEP_AFTER)
strip.clear_strip()
strip.cleanup()
