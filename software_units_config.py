import tkinter as tk
from tkinter import ttk

def draw_software_units_config(canvas, frames):
    # Clear canvas
    canvas.delete("all")
    # Example elements for the Real Time page
    # You can add any specific elements you want for this page
    frame1 = tk.Frame(canvas, width=600, height=150, bg="gray")
    frame1.place(relx=0.35, rely=0.35, anchor="center")
    frames.append(frame1)
    frame1Label = tk.Label(frame1, text="Channel 1",font=("Arial", 20),fg="black", bg="gray")
    frame1Label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    frame2 = tk.Frame(canvas, width=600, height=150, bg="gray")
    frame2.place(relx=0.6, rely=0.35, anchor="center")
    frames.append(frame2)
    frame2Label = tk.Label(frame2, text="Channel 2",font=("Arial", 20),fg="black", bg="gray")
    frame2Label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    frame3 = tk.Frame(canvas, width=600, height=150, bg="gray")
    frame3.place(relx=0.35, rely=0.6, anchor="center")
    frames.append(frame3)
    frame3Label = tk.Label(frame3, text="Channel 3",font=("Arial", 20),fg="black", bg="gray")
    frame3Label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    frame4 = tk.Frame(canvas, width=600, height=150, bg="gray")
    frame4.place(relx=0.6, rely=0.6, anchor="center")
    frames.append(frame4)
    frame4Label = tk.Label(frame4, text="Channel 4",font=("Arial", 20),fg="black", bg="gray")
    frame4Label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    # Add dropdown menus to each frame
    for frame in frames:
        for i in range(6):
            label = tk.Label(frame, text=f"Parameter {i+1}")
            label.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            create_dropdown(frame, row=i, column=2)


def create_dropdown(parent, row, column):
    values = ["Field 1", "Field 2", "Field 3"]

    dropdown = ttk.Combobox(parent, values=values, state="readonly", width=10)
    dropdown.current(0)
    dropdown.grid(row=row, column=column, padx=5, pady=5)

