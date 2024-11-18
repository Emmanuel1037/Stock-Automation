import pyautogui
import time


time.sleep(5)

for row in range(20):
    offsetX = 0
    for col in range(5):
        pyautogui.PAUSE = 0.4
        if row == 19:
            pyautogui.moveTo(120 + offsetX, 560, 1)
        else:
            pyautogui.moveTo(120 + offsetX, 376, 1)
        time.sleep(0.2)
        pyautogui.move(1, 1)
        with pyautogui.hold("Win"):
            pyautogui.hotkey('shift', 's')
        pyautogui.move(27, 27, 0.2)
        pyautogui.dragRel(408, 231, 0.5)
        time.sleep(1)
        if row == 19 and col == 3:
            time.sleep(4)
            pyautogui.click(1866, 906, 1, 0.3)
        offsetX += 260
    pyautogui.moveTo(120, 376, 0.5)
    pyautogui.scroll(-244)