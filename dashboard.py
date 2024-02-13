import colorsys
import tkinter as tk
from tkinter import Image, ttk
from tkinter.tix import IMAGETEXT
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle, Wedge, Rectangle
import numpy as np
import pandas as pd
import os
import plotly.graph_objs as go
import plotly.io as pio
from PIL import ImageTk

def draw_gauge(canvas, data):
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=data,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Value"},
        gauge={
            'axis': {'range': [-3, 5]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [-3, 0], 'color': "lightgray"},
                {'range': [0, 3], 'color': "gray"},
                {'range': [3, 5], 'color': "lightgray"}],
        }))
    fig.update_layout(width=200, height=150, margin=dict(l=20, r=20, t=30, b=20))

    # Save the figure as an image file
    pio.write_image(fig, "gauge_chart.png", format="png")

    # Load the saved image
    img = ImageTk.PhotoImage(file="gauge_chart.png")

    # Display the image on the canvas
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img

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
    
def Switch(switcher,switch_state):      
    if switch_state[0]:
        switcher.config(image = maxIcon)
        switch_state[0] = False
    else:
        switcher.config(image = minIcon)
        switch_state[0] = True

def draw_dashboard(canvas, frames):
    canvas.delete("all")
    df = read_latest_csv()
    # global min_icon, max_icon  # Keep references to images globally

    # # Load the images
    # min_icon = tk.PhotoImage(file="assets/Min_icon.png")
    # max_icon = tk.PhotoImage(file="assets/Max_icon.png")
    # switch_state = [True]  # Using a list to store the switch state

    # switcher = tk.Button(canvas, bd=0, image = minIcon)
    # switcher.config(command=lambda: Switch(switcher,switch_state))
    # # switcher.place(relx=0.8, rely=0.8, anchor="center")

    # switcher.pack(pady = 50)

    data = [df["Channel1"].max(), df['Channel2'].max(), df['Channel3'].max(), df['Channel4'].max()]



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

    for i in range (len(frames)):
        draw_gauge(frames[i], data[i])
