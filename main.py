from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

def open_image():
    pass

window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=350)

watermark_label = Label(window, text="Image for Watermark", font=("Arial", 18, "bold"))
watermark_label.place(x=110, y=10)

sel_img_label = Label(window, text="Write text to watermark", font=("Arial", 12))
sel_img_label.place(x=160, y=60)

text = Text(window, height=8, width=35, font=("Arial", 12))
text.focus()
text.place(x=85, y=90)

def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(
                                              ("Image Files", "*.jpg *.png *.gif *.img"),
                                              ("All Files", "*.*")
                                          ))
    label_file_explorer.configure(text="File Opened: " + filename)

label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 70, height = 3,
                            fg = "blue")
label_file_explorer.place(x=0, y=250)

select_button = Button(window, text="Select Image", command=browse_files)
select_button.place(x=83, y=310)

watermark_button = Button(window, text="Add Watermark", command=browse_files)
watermark_button.place(x=310, y=310)

window.mainloop()
