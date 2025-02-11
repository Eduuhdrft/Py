#automação com pyautogui

import pyautogui as pa
import time
pa.PAUSE=1


pa.press('win')
pa.write('chrome')
pa.press('enter')
pa.write('Youtube.com')
pa.press('ENTER')
pa.click(x=648, y=939)

time.sleep(5)
print(pa.position())