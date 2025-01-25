#imports
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import string
import requests
import json
import random
import threading
import base64
#initializing this shitty ass gui
root = tk.Tk()
root.title("Yecalapse")

#properties
root.geometry("700x400")
root.configure(bg="white")

#defining the gifs
gifPath = "goatgif.gif"
goatGif = Image.open(gifPath)


#making the frames thingy
frames = []
for frame in ImageSequence.Iterator(goatGif):
    frame = frame.convert("RGBA")
    white_bg = Image.new("RGBA", frame.size, "WHITE")
    white_bg.paste(frame, (0, 0), frame)
    frames.append(ImageTk.PhotoImage(white_bg))

#setting the left gif#
goatedGifLeft = tk.Label(root)
goatedGifLeft.pack()

#setting the right gif
goatedGifRight = tk.Label(root)
goatedGifRight.pack()

#defining the actual playback of the gif
def update_frameLeft(index):
    frame = frames[index]
    goatedGifLeft.configure(image=frame, bg="white")
    root.after(500, update_frameLeft, (index + 1) % len(frames))

#defining the playback of the right gif
def update_frameRight(index):
    frame = frames[index]
    goatedGifRight.configure(image=frame, bg="white")
    root.after(500, update_frameRight, (index + 1) % len(frames))

#these play the gif
update_frameLeft(0)
update_frameRight(0)
goatedGifLeft.place(x=-100, y=-30)
goatedGifRight.place(x=330, y=-30)

#defining the actual logo
Logo = tk.Label(root, width=8, height=1, text="Yecalapse", font=("Arial", 32), bg="white")
Logo.place(x=255, y=50)

#the text that tells you what to do
subText = tk.Label(root, width=8, height=1, text="User ID:", font=("Arial", 10), bg="white")
subText.place(x=300, y=110)

#making convert text function
def encode_text():
    input_text = textBox.get("1.0", tk.END).strip() 
    encoded_text = base64.b64encode(input_text.encode()).decode().replace("=", "") 
    result_label.config(text=encoded_text)

#copy to clipboard function
def copy_to_clipboard():
    root.clipboard_clear() 
    root.clipboard_append(result_label.cget("text")) 
    root.update()

#creating the text box
textBox = tk.Text(root, width=20, height=1, font=("Helvetica", 16))
textBox.place(x=250, y= 150)

#creating the convert button
convert_button = tk.Button(root, text="Convert", command=encode_text)
convert_button.place(x=250, y=200)

#making the result text
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.place(x=250, y=250)

#copy button
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()