import pyautogui
import time
import os
import matplotlib.pyplot as plt
from PIL import Image


dimensions = {'16x9': (408, 231), '9x16': (231, 408), '1x1': (),}
offset = [0, 260, 520, 780, 1040]

def SS(rows, lastCol, size, willReachBot):
    time.sleep(3)
    pyautogui.PAUSE = 0.4
    columns = 5
    for row in range(rows):
        offsetX = 0
        if row == rows - 1:
            columns = lastCol
        for col in range(columns):
            if row == 19:
                pyautogui.moveTo(120 + offsetX, 560, 0.3)
            else:
                pyautogui.moveTo(120 + offsetX, 376, 0.3)
            time.sleep(0.2)
            pyautogui.move(1, 1)
            with pyautogui.hold("Win"):
                pyautogui.hotkey('shift', 's')
            pyautogui.move(27, 27, 0.2)
            pyautogui.dragRel(dimensions[size], 0.3)
            time.sleep(2)
            if willReachBot and row == rows - 1 and col == 3:
                time.sleep(4)
                pyautogui.click(1866, 906, 1, 0.3)
            offsetX += 260
        pyautogui.moveTo(120, 376, 0.3)
        pyautogui.scroll(-244)

def SS(rows, lastCol, size, willReachBot, startCol):
    time.sleep(3)
    pyautogui.PAUSE = 0.4
    columns = 5
    pointer = startCol - 1
    for col in range(startCol, 5 + 1):
        pyautogui.moveTo(120 + offset[pointer], 376, 0.3)
        time.sleep(0.2)
        pyautogui.move(1, 1)
        with pyautogui.hold("Win"):
            pyautogui.hotkey('shift', 's')
        pyautogui.move(27, 27, 0.2)
        pyautogui.dragRel(dimensions[size], 0.3)
        time.sleep(2)
        pointer += 1
    pyautogui.moveTo(120, 376, 0.3)
    pyautogui.scroll(-244)

    for row in range(rows - 1):
        pointer = 0
        if row == rows - 2:
            columns = lastCol
        for col in range(columns):
            if willReachBot and row == rows - 2:
                pyautogui.moveTo(120 + offset[pointer], 560, 0.3)
            else:
                pyautogui.moveTo(120 + offset[pointer], 376, 0.3)
            time.sleep(0.2)
            pyautogui.move(1, 1)
            with pyautogui.hold("Win"):
                pyautogui.hotkey('shift', 's')
            pyautogui.move(27, 27, 0.2)
            pyautogui.dragRel(dimensions[size], 0.3)
            time.sleep(2)
            if willReachBot and row == rows - 2 and col == 3:
                time.sleep(4)
                pyautogui.click(1866, 906, 1, 0.3)
            pointer += 1
        pyautogui.moveTo(120, 376, 0.3)
        pyautogui.scroll(-244)

