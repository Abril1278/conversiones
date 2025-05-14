import tkinter as tk
from tkinter import ttk, messagebox

class VentanaConversion:
    def __init__(self, tipo, conversiones, color):
        self.ventana = tk.Toplevel()
        self.ventana.title("Conversión de " + tipo)
        self.ventana.config(bg="#ffe6f0")

        tk.Label(self.ventana, text="Seleccione tipo de conversión:", bg="#ffe6f0", fg="#c71585").pack(pady=(10, 0))
        self.combo = ttk.Combobox(self.ventana, values=list(conversiones.keys()), state="readonly")
        self.combo.current(0)
        self.combo.pack(pady=5)

        tk.Label(self.ventana, text="Ingrese valor:", bg="#ffe6f0", fg="#c71585").pack()
        self.entrada = tk.Entry(self.ventana)
        self.entrada.pack(pady=5)

        tk.Button(self.ventana, text="Convertir", command=self.convertir, bg="#ff69b4", fg="white").pack(pady=5)

        self.resultado = tk.Label(self.ventana, text="Resultado: ", bg="#ffe6f0", fg="#c71585", font=("Arial", 11))
        self.resultado.pack(pady=10)

        self.conversiones = conversiones

    def convertir(self):
        tipo = self.combo.get()
        try:
            valor = float(self.entrada.get())
            conversion_result, unidad = self.conversiones[tipo](valor)
            self.resultado.config(text="Resultado: " + "{:.4f}".format(conversion_result) + " " + unidad)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

def metros_a_kilometros(x):
    return x / 1000, "km"

def pulgadas_a_metros(x):
    return x * 0.0254, "m"

def kilogramos_a_gramos(x):
    return x * 1000, "g"

def libras_a_kilogramos(x):
    return x * 0.453592, "kg"

def segundos_a_minutos(x):
    return x / 60, "min"

def horas_a_dias(x):
    return x / 24, "d"

class AppPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Login con tkinter")
        self.ventana.geometry("300x300")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#ffe6f0")

        encabezado = tk.Label(self.ventana, text="Escoja su opción", bg="#ffb6c1", fg="#800040", font=("Arial", 12, "bold"))
        encabezado.pack(fill="x", pady=10)

        self.boton("Longitud", self.abrir_longitud)
        