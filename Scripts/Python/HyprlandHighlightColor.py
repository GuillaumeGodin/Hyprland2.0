import subprocess
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# Paths
HOME = Path.home()
CONFIG_FILE = HOME / ".config/hypr/currentVariables"
UPDATE_SCRIPT = HOME / "Hyprland2.0/Scripts/Bash/updateConfigs"

def get_current_color():
    """Source Hyprland config and get currentColor variable."""
    cmd = f"source {CONFIG_FILE} && echo $currentColor"
    result = subprocess.run(['bash', '-c', cmd], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()

def pick_color():
    """Run hyprpicker and extract hex code."""
    try:
        output = subprocess.check_output("hyprpicker | tail -c 7", shell=True, text=True)
        color = output.strip()
        print(f"Picked color: {color}")
        hex_color.set(color)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to run hyprpicker:\n{e}")

def apply_color(event=None):
    """Apply selected color and update config."""
    color = hex_color.get().strip()

    if not color:
        messagebox.showwarning("Missing Color", "Please enter or select a color.")
        return

    try:
        # Update via bash script
        subprocess.run([str(UPDATE_SCRIPT), "updateColors", color], check=True)

        # Update config file directly
        subprocess.run([
            "sed", "-i",
            f's/currentColor="{current_color}"/currentColor="{color}"/g',
            str(CONFIG_FILE)
        ], check=True)

        root.quit()

    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to apply color:\n{e}")

def create_widgets(window):
    """Construct the UI layout."""
    pane = tk.Frame(window, bg="#222222")
    pane.pack(fill="x", expand=True, padx=5, pady=5)  # less padding here

    pane.grid_columnconfigure(1, weight=1)

    # Header
    tk.Label(
        pane, text="Hyprland Highlight Color", bg="orange",
        fg="white", font="SegoeUI 14", width=55
    ).grid(row=0, column=0, columnspan=3, sticky="nsew", pady=(0, 5))

    # Label
    tk.Label(pane, text="Color Hex Code:", bg="#222222", fg="white", font="Arial")\
        .grid(row=3, column=0, sticky="e", padx=3, pady=0)

    # Entry Field
    entry = tk.Entry(pane, font="Arial", textvariable=hex_color, bg="#EEEEFF", fg="black", insertbackground="white")
    entry.insert(0, current_color)
    entry.grid(row=3, column=1, sticky="nsew", padx=3, pady=0, ipady=0)

    entry.focus_set()
    entry.select_range(0, 'end')

    # Enable copy-paste shortcuts
    entry.bind("<Control-a>", lambda e: entry.select_range(0, 'end'))

    # Bind Enter to Set Color
    entry.bind("<Return>", apply_color)
    window.bind("<Return>", apply_color)
    entry.bind("<KP_Enter>", apply_color)
    window.bind("<KP_Enter>", apply_color)

    # Bind Escape to close window
    window.bind("<Escape>", lambda e: window.destroy())


    def custom_paste(event):
        try:
            clipboard = event.widget.clipboard_get()
            hex_color.set(clipboard.strip())
            return "break"
        except tk.TclError:
            return "break"

    entry.bind("<Control-v>", custom_paste)

    # Hyprpicker Button
    tk.Button(
        pane, text="Hyprpicker", bg="bisque", font="Arial",
        command=pick_color, relief="groove"
    ).grid(row=3, column=2, sticky="nsew", padx=3, pady=0, ipady=0)

    # Set Color Button
    tk.Button(
        pane, text="Set Color", bg="bisque", font="Arial",
        command=apply_color, relief="groove"
    ).grid(row=4, column=1, padx=150, pady=(5, 0), sticky="ew")

def main():
    global root, hex_color, current_color

    current_color = get_current_color()

    root = tk.Tk()
    root.title("Hyprland Highlight Color")
    root.config(background="#222222")
    root.resizable(False, False)

    hex_color = tk.StringVar()

    create_widgets(root)
    root.mainloop()

if __name__ == "__main__":
    main()