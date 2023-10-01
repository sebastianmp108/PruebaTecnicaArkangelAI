from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
from PIL import ImageTk, Image
import csv
import tkcap



import read_img
import predictor

#   METHODS
def load_img_file(self):
    filepath = filedialog.askopenfilename(
        initialdir="/",
        title="Select image",
        filetypes=(
            ("DICOM", "*.dcm"),
            ("JPEG", "*.jpeg"),
            ("jpg files", "*.jpg"),
            ("png files", "*.png"),
        ),
    )
    if filepath:
        self.array, img2show = read_img.read_jpg_file(filepath)
        self.img1 = img2show.resize((48, 48), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.text_img1.image_create(END, image=self.img1)
        self.button1["state"] = "enabled"


def run_model(self):
    self.label = predictor.predict(self.array)
    self.text2.insert(END, self.label)


def delete(self):
    answer = askokcancel(
        title="Confirmación", message="Se borrarán todos los datos.", icon=WARNING
    )
    if answer:
        self.text2.delete(1.0, "end")
        self.text_img1.delete(self.img1, "end")
        showinfo(title="Borrar", message="Los datos se borraron con éxito")