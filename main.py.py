import tkinter as tk
from tkinter import messagebox, ttk

def convert_temperature():
    try:
        val = float(entry_val.get())
        src = choice_var.get()
        
        if src == "Celsius to Fahrenheit":
            res = (val * 9/5) + 32
            result_label.config(text=f"Result: {res:.2f} °F")
        elif src == "Fahrenheit to Celsius":
            res = (val - 32) * 5/9
            result_label.config(text=f"Result: {res:.2f} °C")
        elif src == "Celsius to Kelvin":
            res = val + 273.15
            result_label.config(text=f"Result: {res:.2f} K")
        elif src == "Kelvin to Celsius":
            res = val - 273.15
            result_label.config(text=f"Result: {res:.2f} °C")
            
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric value.")

# Setup main window
root = tk.Tk()
root.title("Temperature Converter GUI")
root.geometry("320x250")
root.resizable(False, False)

# Styling frame
frame = ttk.Frame(root, padding=15)
frame.pack(fill=tk.BOTH, expand=True)

# Input Field
ttk.Label(frame, text="Enter Temperature:").pack(anchor="w", pady=2)
entry_val = ttk.Entry(frame, width=25)
entry_val.pack(pady=5)

# Dropdown for selection
ttk.Label(frame, text="Select Conversion:").pack(anchor="w", pady=2)
choice_var = tk.StringVar(value="Celsius to Fahrenheit")
options = [
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Celsius to Kelvin",
    "Kelvin to Celsius"
]
dropdown = ttk.OptionMenu(frame, choice_var, options[0], *options)
dropdown.pack(fill=tk.X, pady=5)

# Convert Button
btn_convert = ttk.Button(frame, text="Convert", command=convert_temperature)
btn_convert.pack(pady=10)

# Output Label
result_label = ttk.Label(frame, text="Result: ", font=("Arial", 11, "bold"))
result_label.pack(pady=5)

# Run application
root.mainloop()
