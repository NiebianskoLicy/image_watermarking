import tkinter
from PIL import Image, ImageDraw, ImageFont

def open_image():
    pass

window = tkinter.Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=300)

label = tkinter.Label(window, text="Image for Watermark", font=("Arial", 18, "bold"))
label.pack()

button = tkinter.Button(window, text="Select Image", command=lambda: print("Button clicked"))
button.pack()

window.mainloop()
