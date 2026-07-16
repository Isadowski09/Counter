# main.py
import time
import os
import threading
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.core.window import Window

PROGRESS_FILE = "/data/local/tmp/last_number.txt"  # Saved in a globally root-accessible folder on Android
DEFAULT_START = 3012

HID_MAPPING = {
    '0': 0x27, '1': 0x1e, '2': 0x1f, '3': 0x20, '4': 0x21,
    '5': 0x22, '6': 0x23, '7': 0x24, '8': 0x25, '9': 0x26
}
BACKSPACE_KEY = 0x2a

class HIDControllerApp(App):
    def build(self):
        Window.clearcolor = (0.07, 0.09, 0.16, 1)
        self.running = False
        self.current_number = DEFAULT_START
        self.thread_lock = threading.Lock()
        
        if os.path.exists(PROGRESS_FILE):
            try:
                with open(PROGRESS_FILE, "r") as f:
                    saved = f.read().strip()
                    if saved.isdigit():
                        self.current_number = int(saved) + 1
            except:
                pass

        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.title_label = Label(text="USB HID PHONE LINK", font_size='24sp', bold=True)
        self.status_label = Label(text="Ready over USB", font_size='18sp', color=(0.22, 0.74, 0.97, 1))
        
        self.start_btn = Button(text="START TRANSMISSION", background_color=(0, 0.7, 0.3, 1), font_size='16sp', bold=True)
        self.stop_btn = Button(text="STOP / PAUSE", background_color=(0.9, 0.1, 0.2, 1), font_size='16sp', bold=True, disabled=True)
        
        self.start_btn.bind(on_press=self.start_process)
        self.stop_btn.bind(on_press=self.stop_process)
        
        layout.add_widget(self.title_label)
        layout.add_widget(self.status_label)
        layout.add_widget(self.start_btn)
        layout.add_widget(self.stop_btn)
        
        Clock.schedule_interval(self.update_ui_text, 0.2)
        return layout

    def update_ui_text(self, dt):
        with self.thread_lock:
            if self.running:
                num_str = f"{self.current_number:04d}"
                self.status_label.text = f"Transmitting block: {num_str}"
                self.status_label.color = (0.22, 0.74, 0.97, 1)
            elif self.status_label.text.startswith("Transmitting"):
                self.status_label.text = "Transmission Paused"
                self.status_label.color = (0.9, 0.5, 0, 1)

    def write_to_hid_as_root(self, data_bytes, device="/dev/hidg0"):
        """Forces the app to write to /dev/hidg0 using Android root shell (su)"""
        # Converts byte arrays into an escaped hex string command, e.g., su -c 'echo -ne "\x00\x00\x2a..." > /dev/hidg0'
        hex_str = "".join([f"\\x{b:02x}" for b in data_bytes])
        os.system(f"su -c 'echo -ne \"{hex_str}\" > {device}'")

    def clear_previous_digits(self):
        for _ in range(4):
            # Press Backspace
            self.write_to_hid_as_root([0, 0, BACKSPACE_KEY, 0, 0, 0, 0, 0])
            time.sleep(0.10)
            # Full Release
            self.write_to_hid_as_root([0, 0, 0, 0, 0, 0, 0, 0])
            time.sleep(0.10)

    def send_full_block(self, num_str):
        try:
            for char in num_str:
                keycode = HID_MAPPING[char]
                # Press key
                self.write_to_hid_as_root([0, 0, keycode, 0, 0, 0, 0, 0])
                time.sleep(0.05)
                # Release key
                self.write_to_hid_as_root([0, 0, 0, 0, 0, 0, 0, 0])
                time.sleep(0.05)
            return True
        except:
            return False

    def hid_worker_loop(self):
        while True:
            with self.thread_lock:
                if not self.running:
                    break
                current = self.current_number

            if current >= 10000:
                self.running = False
                break

            num_str = f"{current:04d}"
            if len(set(num_str)) < 4:
                with self.thread_lock:
                    self.current_number += 1
                continue
            
            self.send_full_block(num_str)

            try:
                with open(PROGRESS_FILE, "w") as f:
                    f.write(str(current))
            except:
                pass

            time.sleep(0.80) # Visibility Buffer
            
            if current < 9999:
                self.clear_previous_digits()

            with self.thread_lock:
                self.current_number += 1

    def start_process(self, instance):
        if not self.running:
            self.running = True
            self.start_btn.disabled = True
            self.stop_btn.disabled = False
            threading.Thread(target=self.hid_worker_loop, daemon=True).start()

    def stop_process(self, instance):
        with self.thread_lock:
            self.running = False
        self.start_btn.disabled = False
        self.stop_btn.disabled = True

if __name__ == '__main__':
    HIDControllerApp().run()
