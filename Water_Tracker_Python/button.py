# button.py
import tkinter as tk
from PIL import ImageTk, Image

class ImageButtonApp(tk.Frame):
    """
    Image Button Class that programs and designs the buttons in the pop up windows
    """
    def __init__(self, parent, image_paths, drink_water_command, **kwargs):
        super().__init__(parent, **kwargs)
        self.image_paths = image_paths
        self.image_index = 0

        self.drink_water_button = tk.Button(self, text="I Drank Water", fg='#FFCCCB', bg='#CB3737', font=("Times New Roman Bold", 18), command=drink_water_command)
        self.drink_water_button.pack()
        self.drink_water_button.place(relheight=.12, relwidth=0.2, relx=0.90, rely=0.5, anchor='center')

    def next_image(self):
        """
        cycles through a list of images to display the images in Tkinter and updates the displayed image in response to inputs and clicks from the user in terrarium.py
        """
        self.image_index = (self.image_index + 1) % len(self.image_paths)
        self.img = ImageTk.PhotoImage(Image.open(self.image_paths[self.image_index]))
        self.label.configure(image=self.img)
        self.label.image = self.img
