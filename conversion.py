import tkinter as tk
from tkinter import ttk, messagebox

# Funciones de conversión
def metros_a_kilometros(x):
    return x / 1000

def pulgadas_a_metros(x):
    return x * 0.0254

def kilogramos_a_gramos(x):
    return x * 1000

def libras_a_kilogramos(x):
    return x * 0.453592

def segundos_a_minutos(x):
    return x / 60

def horas_a_dias(x):
    return x / 24

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
            funcion, unidad = self.conversiones[tipo]
            resultado = funcion(valor)
            self.resultado.config(text="Resultado: " + "{:.4f}".format(resultado) + " " + unidad)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

class AppPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Login con tkinter")
        self.ventana.geometry("300x300")
        self.ventana.resizable(False, False)
        self.ventana.config(bg="#ffe6f0")

        encabezado = tk.Label(self.ventana, text="Escoja su opción", bg="#ffb6c1", fg="#800040", font=("Arial", 12, "bold"))
        encabezado.pack(fill="x", pady=10)

        self.boton("Longitud", self.abrir_longitud).pack(pady=10)
        self.boton("Masa", self.abrir_masa).pack(pady=10)
        self.boton("Tiempo", self.abrir_tiempo).pack(pady=10)

        self.ventana.mainloop()

    def boton(self, texto, comando):
        return tk.Button(self.ventana, text=texto, command=comando, bg="#ff69b4", fg="white",
                         font=("Arial", 12), width=20, height=2, relief="flat")

    def abrir_longitud(self):
        conversiones = {
            "Metros → Kilómetros": (metros_a_kilometros, "km"),
            "Pulgadas → Metros": (pulgadas_a_metros, "m")
        }
        VentanaConversion("Longitud", conversiones, "#ff69b4")

    def abrir_masa(self):
        conversiones = {
            "Kilogramos → Gramos": (kilogramos_a_gramos, "g"),
            "Libras → Kilogramos": (libras_a_kilogramos, "kg")
        }
        VentanaConversion("Masa", conversiones, "#ff69b4")

    def abrir_tiempo(self):
        conversiones = {
            "Segundos → Minutos": (segundos_a_minutos, "min"),
            "Horas → Días": (horas_a_dias, "d")
        }
        VentanaConversion("Tiempo", conversiones, "#ff69b4")

if __name__ == "__main__":
    AppPrincipal()




