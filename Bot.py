#Victor-Foscarini

#abra o terminal na pasta que contém o código
#instale o pip caso não tenha : 'sudo apt-get install pip'
#instale a biblioteca pynput: 'pip install pynput'
#rode o código python
#aperte 's' (start) para começar, a letra 'a' começará a ser imprimida pelo seu teclado, seguida de enter após alguns segundos
#aperte 'e' (end) para parar
#se quiser ir mais rápido ou devagar, altere a variável delay (em segundos)


import time
import threading
from pynput.mouse import Button
from pynput.keyboard import Listener, KeyCode, Controller, Key
from random import randint


delay = 1 #tempo de espera entre um clique e outro
button1 = KeyCode(char='g')
button2 = Key.enter
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button1, button2):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button1 = button1
        self.button2 = button2
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                keyboard.press(self.button1)
                keyboard.release(self.button1)
                keyboard.press(self.button2)
                keyboard.release(self.button2)
                time.sleep(self.delay)
            time.sleep(5)


keyboard = Controller()
click_thread = ClickMouse(delay, button1, button2)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
