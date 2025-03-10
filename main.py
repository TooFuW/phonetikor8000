from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys, os
import pystray
from PIL import Image

# pyinstaller --onefile --windowed --icon=image.png --name="Phonetikor8000" --add-data "image.png;." main.py

# Dynamic path
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Create the tray icon
icon_path = os.path.join(base_path, 'image.png')
image = Image.open(icon_path)

activate = True

def after_click(icon, query):
    global activate
    if str(query) == "Activer" or str(query) == "Désactiver":
        activate = not activate
        icon.menu = pystray.Menu(
            pystray.MenuItem("Activer" if not activate else "Désactiver", after_click),
            pystray.MenuItem("Fermer", after_click))
        icon.update_menu()
    elif str(query) == "Fermer":
        icon.stop()
        os._exit(0)

icon = pystray.Icon("Phonetikor8000", image, "Phonetikor8000", menu=pystray.Menu(
	pystray.MenuItem("Activer" if not activate else "Désactiver", after_click),
	pystray.MenuItem("Fermer", after_click)))

icon.run_detached()

# Initialize the keyboard controller
kboard = Controller()

# Function to be called when a key is pressed
def on_press(key):
    if activate:
        try:
            # If the key is one of the following
            match key.char:
                case "²":
                    kboard.tap(Key.backspace)
                    kboard.tap('ɛ')
                case "&":
                    kboard.tap(Key.backspace)
                    kboard.tap('ø')
                case "é":
                    kboard.tap(Key.backspace)
                    kboard.tap('ə')
                case '"':
                    kboard.tap(Key.backspace)
                    kboard.tap('ɔ')
                case "'":
                    kboard.tap(Key.backspace)
                    kboard.tap('ɑ')
                case "(":
                    kboard.tap(Key.backspace)
                    kboard.tap('æ')
                case "-":
                    kboard.tap(Key.backspace)
                    kboard.tap('ʌ')
                case "è":
                    kboard.tap(Key.backspace)
                    kboard.tap('ð')
                case "_":
                    kboard.tap(Key.backspace)
                    kboard.tap('ʃ')
                case "ç":
                    kboard.tap(Key.backspace)
                    kboard.tap('ʤ')
                case "à":
                    kboard.tap(Key.backspace)
                    kboard.tap('ʒ')
                case ")":
                    kboard.tap(Key.backspace)
                    kboard.tap('ŋ')
                case _:
                    return
        except:
            return

# Collect keyboard events until on_press returns False
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()