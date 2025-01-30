from email.mime import image
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=350)

watermark_label = Label(window, text="Image for Watermark", font=("Arial", 18, "bold"))
watermark_label.place(x=120, y=10)

sel_img_label = Label(window, text="Write text to watermark", font=("Arial", 12))
sel_img_label.place(x=170, y=60)

text = Text(window, height=8, width=35, font=("Arial", 12))
text.focus()
text.place(x=85, y=90)

label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 70, height = 3,
                            fg = "blue")
label_file_explorer.place(x=0, y=250)

filename = filedialog.askopenfilename(initialdir="/",
                                      title="Select a File",
                                      filetypes=(
                                          ("Image Files", "*.jpg *.png *.gif *.img"),
                                          ("All Files", "*.*")
                                      ))
label_file_explorer.configure(text="File Opened: " + filename)

def watermark_image():
    # opening image to work with
    opened_image = Image.open(filename)
    # selecting width and height at image resolution
    image.width, image.height = opened_image.size
    draw = ImageDraw.Draw(opened_image)

    font_size = int(opened_image.width / 8)
    font = ImageFont.truetype("arial.ttf", font_size)

    x,y = int(opened_image.width / 2), int(opened_image.height / 2)

    draw.text((x, y), text.get("1.0", END), font=font, fill="red")
    opened_image.show()


select_button = Button(window, text="Select Image", command=watermark_image)
select_button.place(x=215, y=310)

window.mainloop()
