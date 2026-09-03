import tkinter as tk
import time
import psutil
import pygetwindow as gw

# !!! CHANGE THIS to match the exact title bar text of your main window !!!
TARGET_WINDOW_TITLE = "Friday Night Funkin' Pyt Engine" 

class FPSRAMOverlay:
    def __init__(self):
        self.root = tk.Tk()
        
        # Configure window: borderless, always on top, and slightly transparent
        self.root.overrideredirect(True)
        self.root.wm_attributes("-topmost", True)
        self.root.attributes("-alpha", 0.85)  # 85% opacity
        
        # Set background to black and text to green (classic gaming HUD style)
        self.root.configure(bg='black')
        
        # Make the window click-through (Windows only)
        # This ensures the overlay doesn't steal focus or clicks from your game
        try:
            self.root.wm_attributes("-transparentcolor", "black")
        except tk.TclError:
            pass 

        # UI Setup
        self.label = tk.Label(
            self.root, 
            text="FPS: -- | RAM: -- MB", 
            font=("Consolas", 12, "bold"), 
            fg="#FFFFFF", # Neon Green
            bg="black",
            padx=5,
            pady=2
        )
        self.label.pack()

        # Performance tracking variables
        self.process = psutil.Process()
        self.frame_count = 0
        self.last_time = time.time()
        
        # Start the update loops
        self.update_metrics()
        self.snap_to_target_window()
        
        self.root.mainloop()

    def update_metrics(self):
        """Calculates performance and schedules the next update."""
        self.frame_count += 1
        current_time = time.time()
        elapsed = current_time - self.last_time

        # Update text every 0.5 seconds to keep it highly readable
        if elapsed >= 0.5:
            fps = self.frame_count / elapsed
            
            # Fetch total system RAM percentage
            # (Change this to self.process.memory_info().rss / (1024 * 1024) to track just this monitor script instead)
            ram_pct = psutil.virtual_memory().percent
            
            self.label.config(text=f"FPS: {fps:.1f} | RAM: {ram_pct:.1f}%")
            
            self.frame_count = 0
            self.last_time = current_time

        # Run this function again in 16ms (~60 updates per second)
        self.root.after(16, self.update_metrics)

    def snap_to_target_window(self):
        """Finds the main window and positions the overlay just below the title bar."""
        try:
            # Look for your main window by its title
            windows = gw.getWindowsWithTitle(TARGET_WINDOW_TITLE)
            if windows:
                target = windows[0] # Grab the first matching window instance
                
                # Only move if the window is currently visible/active
                if not target.isMinimized:
                    # x: 10px padding from the left edge
                    # y: Pushed down 35px from the top edge to clear the window title bar
                    x = target.left + 10
                    y = target.top + 35
                    
                    self.root.geometry(f"+{x}+{y}")
        except Exception:
            pass # Fail silently if the window closes or isn't found yet

        # Re-check and re-snap every 100ms so it follows the window if you move it
        self.root.after(100, self.snap_to_target_window)

if __name__ == "__main__":
    print(f"Overlay started. Looking for a window titled: '{TARGET_WINDOW_TITLE}'")
    FPSRAMOverlay()
