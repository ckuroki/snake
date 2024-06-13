import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

time.sleep(5)  # sleep for 5 seconds before start
print('Start!')
keyboard.press('x') # start game
time.sleep(0.2)
keyboard.release('x')

while True: 

    time.sleep(0.5)  # sleep for 500ms

    keyboard.press(Key.down)
    print('Down')
    time.sleep(0.2)
    keyboard.release(Key.down)

    time.sleep(0.5)  # sleep for 500ms

    keyboard.press(Key.right)
    print('Right')
    time.sleep(0.2)
    keyboard.release(Key.right)

