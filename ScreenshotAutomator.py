import pyautogui
import time


time.sleep(5)
pyautogui.scroll(-244)
# for row in range(20):
#     offsetX = 0
#     for col in range(5):
#         pyautogui.PAUSE = 0.2
#         pyautogui.moveTo(120 + offsetX, 376, 1)
#         time.sleep(0.2)
#         pyautogui.move(1, 1)
#         with pyautogui.hold("Win"):
#             pyautogui.hotkey('shift', 's')
#         pyautogui.move(30, 30, 0.2)
#         pyautogui.dragRel(420, 240, 1)
#         time.sleep(3)
#         offsetX += 260
#     pyautogui.moveTo(120, 376, 0.5)
#     pyautogui.scroll(-250)