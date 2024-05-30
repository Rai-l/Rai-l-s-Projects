import tkinter as tk
import pygame
import shutil
from tkinter import filedialog
import os
import pygame.mixer
import json
import time

y_position = 50


def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {}

def print_coordinates(event):
    x = event.x
    y = event.y
    print(f"Mouse clicked at coordinates: ({x}, {y})")


def play_audio(audio_path):
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()


def open_file(audio_path):
    if audio_path:
        play_audio(audio_path)


def button_add_click():
    def submit_name():
        song_name = name.get()
        file_path = direct.get()
        playlist[song_name] = file_path
        save_data_to_file(playlist, 'data.json')
        print(playlist)
        #create_container(canvas, y_position, name, direct)
        #y_position += 50

    popup = tk.Toplevel(window)
    popup.title("Add song")

    base = tk.Canvas(popup, width=325, height=300, bg='#222426')
    base.pack()

    popup.focus_set()

    input_text = tk.StringVar()

    input_text1 = tk.StringVar()

    name = tk.Entry(base, textvariable=input_text)
    name.place(x=50, y=100)

    direct = tk.Entry(base, textvariable=input_text1)
    direct.place(x=50, y=150)

    label_name = tk.Label(base, text="Name:")
    label_name.place(x=50, y=75)

    label_direct = tk.Label(base, text="Directory:")
    label_direct.place(x=50, y=125)

    button_name = tk.Button(base, text="submit", command=submit_name)
    button_name.place(x=65, y=175)

    popup.mainloop()
    pass


def create_container(canvas, y_position, name, direct):
    container = tk.Frame(canvas, padx=10, pady=5)
    container.pack()

    name_label = tk.Label(container, text=f"Name: {name}")
    name_label.pack()

    age_label = tk.Label(container, text=f"direct: {direct}")
    age_label.pack()

    canvas.create_window(10, y_position, window=container, anchor="nw")

    button_play = tk.Button(container, text="Play Audio", command=lambda: open_file(direct))
    button_play.pack()


def button_loop():
    for name, direct in playlist.items():
        play_audio(direct)
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        print("Audio finished:", direct)



window = tk.Tk()
window.title("Current Playlist")

# Create canvas
canvas = tk.Canvas(window, width=450, height=600, bg='#222426')
canvas.pack()

#rect=tk.create_Re

button_add = tk.Button(canvas, text="add a song", command=button_add_click)
button_add.place(x=340, y=12)

button_loop= tk.Button(canvas, text= "Loop all", command=button_loop)
button_loop.place(x=50, y=12)

window.bind("<Button-1>", print_coordinates)


pygame.init()
#pygame.mixer.music.load(".mp3")
playlist = load_data_from_file('data.json')

for name, direct in playlist.items():
    create_container(canvas, y_position, name, direct)
    y_position += 100

#conf78734381
window.mainloop()
