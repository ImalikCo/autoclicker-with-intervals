import PySimpleGUI as sg
import time
import threading
import random
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

if __name__ == '__main__':
    layout = [[sg.Text("super coole autoclicker 100% no ban rate jamflex lol")],
            [sg.Text('Schakelaar', size=(18, 1)), sg.InputText('[', key='-START_KEY-')],
            [sg.Text('Close Program Key', size=(18, 1)), sg.InputText(']', key='-END_KEY-')],
            [sg.Text('Kliksnelheid (s)', size=(18, 1)), sg.InputText(key='-CLICK_SPEED-')],
            [sg.Text('Intervallen tussen 0 en', size=(18, 1)), sg.InputText(key='-INTERVALS-')],
            [sg.Button('Submit'), sg.Button('Cancel')]]

    window = sg.Window('Simple Data Entry Window', layout)
    event, values = window.read(close=True)
    
    start_key = values['-START_KEY-'] 
    end_key = values['-END_KEY-']
    click_speed = values['-CLICK_SPEED-']   
    intervals = values['-INTERVALS-'] 
    interval = int(float(intervals))

    if event == 'Submit':
        delay_s = click_speed
        delay = int(float(delay_s))
        button = Button.left
        start_stop_key = KeyCode(char=start_key)
        exit_key = KeyCode(char=end_key)
        
    
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
                while self.program_run:
                    while self.running:
                        rand_interval = random.uniform(0, interval)
                        mouse.click(self.button)
                        time.sleep(self.delay)
                        time.sleep(rand_interval)
                        print(rand_interval)
                    time.sleep(0.1)
        

        mouse = Controller()
        thread = ClickMouse(delay, button)
        thread.start()

        
        
        def on_press(key):
            if key == start_stop_key:
                if thread.running:
                    thread.stop_clicking()
                else:
                    thread.start_clicking()
            elif key == exit_key:
                thread.exit()
                listener.stop()
        
        with Listener(on_press=on_press) as listener:
            listener.join()

    else:
        print('User cancelled')

        