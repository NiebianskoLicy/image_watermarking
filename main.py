from email.mime import image
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

window = Tk()
window.title("Image Watermarking")
window.minsize(width=500, height=350)

# function that watermark image
def watermark_image(name_of_file):

    # opening image to work with
    opened_image = Image.open(name_of_file)
    opened_image = opened_image.convert("RGBA")
    # selecting width and height at image resolution
    image.width, image.height = opened_image.size

    # adding overlay to image
    overlay = Image.new('RGBA', opened_image.size, (255,255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    font_size = int(opened_image.width / 8)
    font = ImageFont.truetype("arial.ttf", font_size)

    x, y = int(opened_image.width / 2), int(opened_image.height / 2)

    # drawing text with input from text variable
    draw.text((x, y), text.get("1.0", "end-1c"),
              font=font, fill=(255,255,255,120),stroke_width=2, anchor="ms", stroke_fill=(0,0,0,50))

    # adding alpha composite to image
    # without it text cant be drawn
    watermarked_image = Image.alpha_composite(opened_image, overlay)
    watermarked_image.show()

# another function is made in class
# helps with passing filename without running watermark_image function
# prevents from double opening file explorator
class ImageWatermarking:
    def __init__(self):
        self.filename = ""

    def select_img(self):
        # opening file explorator to select an image
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select a File",
                                              filetypes=(
                                                  ("Image Files", "*.jpg *.png *.gif *.img"),
                                                  ("All Files", "*.*")
                                              ))
        label_file_explorer.configure(text="File Opened: " + filename)
        self.filename = filename


file = ImageWatermarking()

# overall structure of GUI
watermark_label = Label(window, text="Image for Watermark", font=("Arial", 18, "bold"))
watermark_label.place(x=120, y=10)

sel_img_label = Label(window, text="Write text to watermark", font=("Arial", 12))
sel_img_label.place(x=170, y=60)

text = Text(window, height=7, width=35, font=("Arial", 12))
text.focus()
text.place(x=85, y=90)

label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 70, height = 3,
                            fg = "blue")
label_file_explorer.place(x=0, y=240)

select_button = Button(window, text="Select Image", command=file.select_img)
select_button.place(x=82, y=305)

#lambda for passing argument to function
add_watermark_button = Button(text="Add Watermark", command=lambda:watermark_image(file.filename))
add_watermark_button.place(x=309, y=305)


window.mainloop()
