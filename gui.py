import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

filetypes = (
    ('Images', '*.png *.jpg *.jpeg *.webp'),
    ('All files', '*.*')
)

file_path = ""
img = None
test = None


def open_btn_click():
    global file_path, img, test
    file_path = filedialog.askopenfilename(filetypes=filetypes)
    if file_path:
        img = Image.open(file_path)
        test = ImageTk.PhotoImage(img)  
        print("Chosen file:", file_path)
        img = img.resize((200, 200))
        label.config(image=test) 
        label.image = test
        detect_btn.config(state="active")
    else:
        print("No file selected.")

def detect_btn_click():
    pass

root = tk.Tk()
root.title("DogDetect")

open_btn = tk.Button(root, text="Open Image", command=open_btn_click)
open_btn.pack(pady=20, side="left")

detect_btn = tk.Button(root, text="Detect breed", command=detect_btn_click, state="disabled")
detect_btn.pack(pady=20, side="right")

label = tk.Label(root)
label.pack()

root.mainloop()
