import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageConverter:
    def __init__(self, root):
        self.root = root
        self.image_path = None

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.convert_button = tk.Button(root, text="Select Image and Convert", command=self.convert_image)
        self.convert_button.pack()

    def convert_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", ".jpg .jpeg .png .bmp")])

        if self.image_path:
            original_image = Image.open(self.image_path)
            grayscale_image = original_image.convert("L")

            original_image_tk = ImageTk.PhotoImage(original_image)
            self.image_label.config(image=original_image_tk)
            self.image_label.image = original_image_tk

            grayscale_image.save("grayscale_image.jpg")

            grayscale_image_tk = ImageTk.PhotoImage(Image.open("grayscale_image.jpg"))
            grayscale_label = tk.Label(self.root, image=grayscale_image_tk)
            grayscale_label.image = grayscale_image_tk
            grayscale_label.pack()

root = tk.Tk()
root.title("Image Converter")
image_converter = ImageConverter(root)
root.mainloop()
