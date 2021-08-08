import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

delay = 5
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

print("Press s for starts")
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_run = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_run = False

    def run(self):

        i = 1

        while self.program_run:
            while self.running:
                start = time.time()
                mouse.click(self.button)
                time.sleep(self.delay)
                end = time.time()
                sure = end - start
                print("Another {seconds} seconds passed. Clicked {count} times.".format(seconds = int(sure), count= i))
                i += 1
            time.sleep(0.1)
mouse = Controller()
thread = ClickMouse(delay, button)
thread.start()


def on_press(key):
    if key == start_stop_key:
        if thread.running:
            print("Stopping")
            thread.stop_clicking()
        else:
            print("Starting")
            thread.start_clicking()
    elif key == exit_key:
        print("Exited")
        thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()