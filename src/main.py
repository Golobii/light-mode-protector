import numpy as np
import pyautogui
import time
import os


def main():
    running = True
    while running:
        image = np.array(pyautogui.screenshot())
        number_of_whites = len(np.argwhere(image == [255, 255, 255]))

        if number_of_whites > 1000000:
            os.system("xrandr --output eDP-1-1 --brightness 0.5")
        else:
            os.system("xrandr --output eDP-1-1 --brightness 1")

        time.sleep(0.5)


if __name__ == '__main__':
    main()
