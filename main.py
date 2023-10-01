from tkinter import *
from tkinter import ttk, font, filedialog, Entry

# -----------------------------
import methods


class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Herramienta para la detección de emociones")

        #   BOLD FONT
        fonti = font.Font(weight="bold")

        self.root.geometry("815x560")
        self.root.resizable(0, 0)

        #   LABELS
        self.lab1 = ttk.Label(self.root, text="Imagen", font=fonti)
        self.lab2 = ttk.Label(self.root, text="Resultado:", font=fonti)

        #   TWO STRING VARIABLES TO CONTAIN ID AND RESULT

        self.result = StringVar()

        #   TWO IMAGE INPUT BOXES
        self.text_img1 = Text(self.root, width=31, height=15)
        self.text2 = Text(self.root)

        #   BUTTONS
        self.button1 = ttk.Button(
            self.root, text="Predecir", state="disabled", command=methods.run_model
        )
        self.button2 = ttk.Button(
            self.root, text="Cargar Imagen", command=methods.load_img_file
        )
        self.button3 = ttk.Button(self.root, text="Borrar", command=methods.delete)

        #   WIDGETS POSITIONS
        self.lab1.place(x=110, y=65)
        self.lab2.place(x=545, y=65)

        self.button1.place(x=220, y=460)
        self.button2.place(x=70, y=460)
        self.button3.place(x=670, y=460)

        self.text2.place(x=610, y=350, width=90, height=30)
        self.text_img1.place(x=65, y=90)

        #  se reconoce como un elemento de la clase
        self.array = None

        #   RUN LOOP
        self.root.mainloop()


def main():
    my_app = App()
    return 0