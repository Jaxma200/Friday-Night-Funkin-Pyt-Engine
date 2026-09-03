import os
import tkinter as tk
import platform
from tkinter import messagebox
import psutil
import time
from tkinter import messagebox
import sys
from PIL import Image, ImageTk
messagebox.showinfo("Pyt Engine", "to run Pyt engine. make sure you install psutil with pip install psutil")

root = tk.Tk()
root.title("Friday Night Funkin' Pyt Engine")
root.geometry("1200x600")
print("loaded-menu")

import subprocess

current_folder = os.path.dirname(os.path.abspath(__file__))
fps_script_path = os.path.join(current_folder, "fps.py")

subprocess.Popen(["python", fps_script_path])


# Get the folder where this python script is saved
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(script_dir, "py.png")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Load image using the absolute path built from the script's location
img = tk.PhotoImage(file=img_path)

label = tk.Label(root, image=img, bg="black", bd=0, highlightthickness=0)
label.grid(row=0, column=0, sticky="nsew")



# Set background to black
root.configure(bg="black")

# This finds the exact folder where your script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "py.png")

try:
    icon = tk.PhotoImage(file=image_path)
    root.wm_iconphoto(False, icon)
except tk.TclError as e:
    print(f"Error loading icon: {e}")
print("loaded-icon")






root.attributes('-fullscreen', False)

# Bind Escape key to exit fullscreen easily
root.bind("<F11>", lambda event: root.attributes('-fullscreen', True))
print("loaded-fullscreen")

# Bind Escape key to exit fullscreen easily
root.bind("<Escape>", lambda event: root.attributes('-fullscreen', False))



# Updated to target 'crash64x.py' instead of 'crash64.py'
PLUGIN_PATH = os.path.join(
    os.getcwd(), "plugins", "crash-handler64x", "crash64x.py"
)


def run_crash_handler(error_message=None):
    """Launches the external crash handler script, optionally passing the error."""
    try:
        args = [sys.executable, PLUGIN_PATH]
        if error_message:
            args.append(error_message)

        # Launches the script as an independent process
        subprocess.Popen(args)
    except Exception as e:
        print(f"Failed to launch crash handler: {e}")


if __name__ == "__main__":
    try:
        # --- YOUR EXISTING PYT ENGINE INITIALIZATION & LOOP HERE ---
        print("Friday Night Funkin' Pyt Engine is running...")

    except Exception as error:
        import traceback

        error_details = traceback.format_exc()
        print(f"Engine crashed:\n{error_details}")

        # Run the handler with error logs if a crash happens
        run_crash_handler(error_message=error_details)

root.mainloop()