import tkinter as tk
from tkinter import messagebox
from tkinter import *

class Producto:
    nombre: StringVar
    precio: float
    stock: int
    
    def __init__(self, nombre: StringVar, precio: float, stock: int):
        self.nombre = tk.StringVar(self)
        self.precio = precio
        self.stock = stock

def calcular_valor_total():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        total = num1 * num2
        messagebox.showinfo("Total", f"Total del Stock del producto: {total}")
    except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")

def mostrar_detalles():
    try:
        nombre = str(entry_nombre.get())
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        total = num1 * num2
        messagebox.showinfo("Detalles", f"Nombre: {nombre} \n Precio: {num2} \n Stock: {num1} \n Precio total: {total}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa datos válidos.")


ventana = tk.Tk()
ventana.title("Bienvenido al almacen")
ventana.geometry("600x500")
nombre = StringVar()
etiqueta = tk.Label(ventana, text="Productos en el almacen", bg="blue", fg="white", font=("Arial", 14, "bold"), relief="groove")
etiqueta.grid(row=0, column=4)

nombre = tk.Label(ventana, text="Nombre", bg="green", fg="white", font=("Arial", 14, "bold"), relief="groove")
nombre.grid(row=1, column=1)
entry_nombre = tk.Entry(ventana, textvariable=nombre)
entry_nombre.grid(row=2, column=1)

label_num1 = tk.Label(ventana, text="Cantidad", bg="green", fg="white", font=("Arial", 14, "bold"), relief="groove")
label_num1.grid(row=3, column=1)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=4, column=1)
 
label_num2 = tk.Label(ventana, text="Precio", bg="green", fg="white", font=("Arial", 14, "bold"), relief="groove")
label_num2.grid(row=6, column=1)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=7, column=1)

boton_multiplicar = tk.Button(ventana, text="Valor total en Stock del producto", bg="lightgray", command=calcular_valor_total, fg="gray", font=("Arial", 12, "bold"))
boton_multiplicar.grid(row=3, column=8)

detalles = tk.Button(ventana, text="Detalles del producto", bg="lightgray", command=mostrar_detalles, fg="gray", font=("Arial", 12, "bold"))
detalles.grid(row=4, column=8)


#def agregar():
    #tk.Label(ventana, text = "Productos: 1. Refrescos 2. Galletas 3. Latas de atún 4. Manzanas 5. Jitomates").pack()

#def salir():
  #  ventana.destroy()


#boton = tk.Button(ventana, text = "Agregar producto", command = agregar, fg = "black")
#boton.pack()
#boton.place(x=50, y=50)


#boton = tk.Button(ventana, text = "Salir", command = salir, fg = "black")
#boton.pack()
#boton.place(x=50, y=90)








ventana.mainloop()