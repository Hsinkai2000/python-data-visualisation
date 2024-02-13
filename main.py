import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import os
import time
import software_units_config
import dashboard

# Function to create the Matplotlib plots
def create_plots(frame):
    fig, axs = plt.subplots(2, 2, figsize=(10, 8))
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=False)
    
    return axs

def update_plots(axs, x_range):
    for i in range(2):
        for j in range(2):
            ax = axs[i, j]
            ax.clear()
            df = read_latest_csv()
            if df is not None:
                channel_data = df[f"Channel{i*2 + j + 1}"]

                ax.plot(x_range, channel_data, label=f"Channel {i*2 + j + 1}")
                ax.set_xlabel("Row")
                ax.set_ylabel("Value")
                ax.set_title(f"Channel {i*2 + j + 1} Data")
                ax.set_xlim(1, 100)  # Set initial x-axis limits from 1 to 1000
                ax.set_ylim(-3, 5)     # Set y-axis limits from -3 to 5
                ax.legend()
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)

def update_periodically(axs):
    x_range = list(range(1, 1001))  # Initial x-axis range from 1 to 10
    
    while True:
        update_plots(axs, x_range)
        time.sleep(1)  # Adjust the sleep time for slower scrolling
        if x_range[-1] < 1000:
            x_range.append(x_range[-1] + 100)  # Increment the x-axis range

# Function to read the latest CSV file and extract data
def read_latest_csv():
    data_dir = "./data"
    csv_files = [file for file in os.listdir(data_dir) if file.endswith('.csv')]
    if csv_files:
        latest_file = max(csv_files, key=lambda x: os.path.getmtime(os.path.join(data_dir, x)))
        csv_path = os.path.join(data_dir, latest_file)
        df = pd.read_csv(csv_path)
        return df
    else:
        return None

def on_click(button_id):
    if button_id == 1:  # Real Time button clicked
        draw_real_time_page()
    if button_id == 2:
        draw_dashboard()
    if button_id == 3:
        draw_hv_network_diagram()
    if button_id == 4:
        draw_sw_unit()
    else:
        print("Button", button_id, "clicked")

def create_button(canvas, x, y, width, height, button_id, text):
    button = canvas.create_rectangle(x, y, x + width, y + height, fill="lightblue")
    canvas.create_text((x + width / 2, y + height / 2), text=text, font=("Arial", 12), fill="black")
    canvas.tag_bind(button, "<Button-1>", lambda event, id=button_id: on_click(id))

def draw_real_time_page():
    # Clear canvas
    canvas.delete("all")
    
    # Create a frame for the plots
    plot_frame = tk.Frame(canvas)
    plot_frame.pack(expand=False)

    # Create and display the plots in the plot frame
    axs = create_plots(plot_frame)
    update_periodically(axs)
    # Set the title label
    title_label.config(text="Realtime")
    title_label.place(relx=0.5, rely=0.05, anchor="center")
    
    # Create the back button and place it on the canvas
    back_button = tk.Button(canvas, text="Back", command=draw_main_page)
    back_button.place(relx=0.1, rely=0.8)
    canvas.pack()

def software_back(frames,canvas):
    canvas.delete("all")
    for frame in frames:
        frame.pack_forget()
        frame.destroy()
    frames.clear()
    draw_main_page()

def draw_dashboard():
    # Title
    title_label.config(text="Dashboard")
    title_label.place(relx=0.5, rely=0.05, anchor="center")
    
    # Example elements for the Real Time page
    # You can add any specific elements you want for this page
    
    # Back button
    back_button = tk.Button(canvas, text="Back", command=lambda: software_back(frames,canvas))
    back_button.place(relx=0.1, rely=0.8)

    dashboard.draw_dashboard(canvas, frames)

def draw_hv_network_diagram():
    # Clear canvas
    canvas.delete("all")
    # Title
    title_label.config(text="HV Network Diagram")
    title_label.place(relx=0.5, rely=0.05, anchor="center")
    
    # Example elements for the Real Time page
    # You can add any specific elements you want for this page
    
    # Back button
    back_button = tk.Button(canvas, text="Back", command=draw_main_page)
    back_button.place(relx=0.1, rely=0.8)

def draw_main_page(framePlot=None):
    # Clear canvas
    canvas.delete("all")
    if framePlot:
        framePlot.pack_forget()
    # Title
    title_label.config(text="Welcome to Project HMI")
    title_label.place(relx=0.5, rely=0.05, anchor="center")
    
    # Recreate main page elements
    create_buttons()

def draw_sw_unit():

    # Title
    title_label.config(text="Software & Units Configuration")
    title_label.place(relx=0.5, rely=0.05, anchor="center")
    
    # Back button
    back_button = tk.Button(canvas, text="Back", command=lambda: software_back(frames,canvas))
    # back_button = tk.Button(canvas, text="Back", command=draw_main_page)
    back_button.place(relx=0.1, rely=0.8)

    software_units_config.draw_software_units_config(canvas,frames)

def create_buttons():
    # Calculate the center of the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = screen_width / 2
    center_y = screen_height / 2

    button_width = 250
    button_height = 150
    spacing = 20

    # Create four rectangle buttons arranged in a box shape with titles
    button_positions = [
        (center_x - button_width - spacing, center_y - button_height - spacing, "Real Time"),
        (center_x + spacing, center_y - button_height - spacing, "Dashboard"),
        (center_x - button_width - spacing, center_y + spacing, "HV Network Diagram"),
        (center_x + spacing, center_y + spacing, "Software and Units Configuration")
    ]

    for i, (x, y, title) in enumerate(button_positions):
        create_button(canvas, x, y, button_width, button_height, i+1, title)

frames = []
root = tk.Tk()
root.attributes("-fullscreen", True)
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)
title_label = tk.Label(canvas, text="", font=("Arial", 20),fg="black", bg="White")
title_label.place(relx=0.5, rely=0.05, anchor="center")
draw_main_page()

root.mainloop()
