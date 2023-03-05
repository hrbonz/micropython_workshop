"""NeoPixel utility functions

Module to load on the board

When defining colors, RGB values are defined as a ``list`` of ``int`` in a
range of 0 to 255.
"""

#: Sine color distribution to use to recreate a rainbow effect
#: see https://www.instructables.com/How-to-Make-Proper-Rainbow-and-Random-Colors-With-/
SINE_COLORS = [
  0,   0,   0,   0,   0,   1,   1,   2,
  2,   3,   4,   5,   6,   7,   8,   9,
 11,  12,  13,  15,  17,  18,  20,  22,
 24,  26,  28,  30,  32,  35,  37,  39,
 42,  44,  47,  49,  52,  55,  58,  60,
 63,  66,  69,  72,  75,  78,  81,  85,
 88,  91,  94,  97, 101, 104, 107, 111,
114, 117, 121, 124, 127, 131, 134, 137,
141, 144, 147, 150, 154, 157, 160, 163,
167, 170, 173, 176, 179, 182, 185, 188,
191, 194, 197, 200, 202, 205, 208, 210,
213, 215, 217, 220, 222, 224, 226, 229,
231, 232, 234, 236, 238, 239, 241, 242,
244, 245, 246, 248, 249, 250, 251, 251,
252, 253, 253, 254, 254, 255, 255, 255,
255, 255, 255, 255, 254, 254, 253, 253,
252, 251, 251, 250, 249, 248, 246, 245,
244, 242, 241, 239, 238, 236, 234, 232,
231, 229, 226, 224, 222, 220, 217, 215,
213, 210, 208, 205, 202, 200, 197, 194,
191, 188, 185, 182, 179, 176, 173, 170,
167, 163, 160, 157, 154, 150, 147, 144,
141, 137, 134, 131, 127, 124, 121, 117,
114, 111, 107, 104, 101,  97,  94,  91,
 88,  85,  81,  78,  75,  72,  69,  66,
 63,  60,  58,  55,  52,  49,  47,  44,
 42,  39,  37,  35,  32,  30,  28,  26,
 24,  22,  20,  18,  17,  15,  13,  12,
 11,   9,   8,   7,   6,   5,   4,   3,
  2,   2,   1,   1,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0,
  0,   0,   0,   0,   0,   0,   0,   0
]


def clear_all(np):
    """Clear all the LEDs, same as turning them off

    :param NeoPixel np: a NeoPixel instance
    """
    for i in range(np.n):
        np[i] = (0, 0, 0)
    np.write()


def set_all(np, color):
    """Set all LEDs to the same color

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    """
    for i in range(np.n):
        np[i] = color
    np.write()


def hline(np, color, n, geom=[8, 8]):
    """Draw a horizontal line at position n

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    :param int n: line position starting at 0
    :param list geom: LED geometry, horizontal & vertical counts
    """
    for h in range(geom[0]):
        np[h + n * geom[1]] = color
    np.write()


def vline(np, color, n, geom=[8, 8]):
    """Draw a vertical line at position n

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    :param int n: line position
    :param list geom: LED geometry, horizontal & vertical counts
    """
    for v in range(geom[1]):
        if (v % 2) == 0:
            pos = geom[0] * v + n
        else:
            pos = geom[0] * (v + 1) - (n + 1)
        np[pos] = color
    np.write()


def walk(np, color, wait=100):
    """Single dot walks through all the LEDs

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    :param int wait: waiting time between two LEDs color change in ms
    """
    for i in range(np.n):
        np[i] = color
        np.write()
        time.sleep_ms(wait)
        np[i] = (0, 0, 0)
        np.write()


def walk_bounce(np, color, wait=100):
    """Same as walk but comes back when reaching the end

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    :param int wait: waiting time between two LEDs color change in ms
    """
    for i in range(np.n):
        np[i] = color
        np.write()
        time.sleep_ms(wait)
        np[i] = (0, 0, 0)
        np.write()

    # start with one so we don't repeat the last LED when reversing
    for i in range(1, np.n):
        np[np.n - 1 - i] = color
        np.write()
        time.sleep_ms(wait)
        np[np.n - 1 - i] = (0, 0, 0)
        np.write()


def fill(np, color, wait=100):
    """Fill the LED square step by step

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    :param int wait: waiting time between two LEDs color change in ms
    """
    for i in range(np.n):
        np[i] = color
        np.write()
        time.sleep_ms(wait)


def fill_bounce(np, color, wait=100):
    """Same as walk but comes back when reaching the end

    :param NeoPixel np: a NeoPixel instance
    :param list color: a list of RGB values
    :param int wait: waiting time between two LEDs color change in ms
    """
    for i in range(np.n):
        np[i] = color
        np.write()
        time.sleep_ms(wait)

    # wait a tiny bit for visual effect purposes
    time.sleep_ms(wait)

    for i in range(np.n):
        np[np.n - 1 - i] = (0, 0, 0)
        np.write()
        time.sleep_ms(wait)


def sine_dot(np, pos, angle, dim=1, invert=False):
    """Same as walk but comes back when reaching the end

    :param NeoPixel np: a NeoPixel instance
    :param int pos: the position of the LED
    :param int angle: color angle (0 to 360)
    :param float dim: a dimming value between 0 and 1
    :param bool invert: invert the volor gradient
    """
    red = 255 - SINE_COLORS[(angle + 120) % 360]
    green = 255 - SINE_COLORS[angle % 360]
    blue = 255 - SINE_COLORS[(angle + 240) % 360]

    if invert is True:
        red = 255 - red
        blue = 255 - blue
        green = 255 - green

    np[pos] = (
        int(red * dim),
        int(green * dim),
        int(blue * dim),
    )
    np.write()
