import tkinter as tk
from tkinter import messagebox
import mysql.connector
import tkinter as tk
import mysql.connector
from tkinter import ttk,messagebox
from tkinter import *


def verificar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
 
    try:
        conn = mysql.connector.connect(
            host='localhost',      
            user='root',          
            password='',  
            database='biblioteca'    
            )
 
        cursor = conn.cursor()
 
        cursor.execute('''
            SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s
        ''', (usuario, contraseña))
 
        usuario = cursor.fetchone()
 
        if usuario:
            messagebox.showinfo("Login exitoso", f"Bienvenido {usuario[3]}")
            validacion(usuario=usuario)
        else:
            messagebox.showerror("Error", "Usuario o contraseña no encontrados.")
   
    except mysql.connector.Error as err:
        messagebox.showerror("Error de conexión", f"Error: {err}")
   
    finally:
        if conn.is_connected():
            conn.close()  
 
def validacion(usuario):
    if usuario[5] == "Administrador":
        root.withdraw()
        vent_administrador()
    else:
        root.withdraw()
        vent_empleado()

def vent_administrador():
    root.withdraw()

    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()
        micursos.execute("Select * from usuarios")
        lista = micursos.fetchall()

        for i,(id, Nombre, Apellido, usuario, contraseña, rol) in enumerate(lista, start=1):
            listbox.insert("", "end", values = (id, Nombre, Apellido, usuario, contraseña, rol))
            mysqlC.close()

    def add():
        nombreAdd = nombre.get()
        apellidoAdd = apellido.get()
        usuarioAdd = usuario.get()
        contraseñaAdd = contraseña.get()
        rolAdd = rol.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"INSERT INTO usuarios(id, Nombre, Apellido, usuario, contraseña, rol) values('{idAdd}','{nombreAdd}','{apellidoAdd}','{usuarioAdd}','{contraseñaAdd}','{rolAdd}')")
            mysqlC.commit()
            nombre.delete(0,END)
            apellido.delete(0,END)
            usuario.delete(0,END)
            contraseña.delete(0,END)
            rol.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("Informacion", "Empleado agregado")
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def eliminar():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"DELETE FROM usuarios WHERE id={idAdd}")
            mysqlC.commit()
            nombre.delete(0,END)
            apellido.delete(0,END)
            usuario.delete(0,END)
            contraseña.delete(0,END)
            rol.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("Informacion", "Empleado eliminado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit():
        nombreAdd = nombre.get()
        apellidoAdd = apellido.get()
        usuarioAdd = usuario.get()
        contraseñaAdd = contraseña.get()
        rolAdd = rol.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"UPDATE usuarios set Nombre='{nombreAdd}', Apellido='{apellidoAdd}', usuario='{usuarioAdd}', contraseña='{contraseñaAdd}', rol='{rolAdd}' where id={idAdd}")
            mysqlC.commit()
            mysqlC.commit()
            nombre.delete(0,END)
            apellido.delete(0,END)
            usuario.delete(0,END)
            contraseña.delete(0,END)
            rol.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("Informacion", "Empleado editado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def obtenerResultados(event):
        nombre.delete(0,END)
        apellido.delete(0,END)
        usuario.delete(0,END)
        contraseña.delete(0,END)
        rol.delete(0,END)
        identificador.delete(0,END)

        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0,seleccion["Id"])
        nombre.insert(0,seleccion["Nombre"])
        apellido.insert(0,seleccion["Apellido"])
        usuario.insert(0,seleccion["Usuario"])
        contraseña.insert(0,seleccion["Contraseña"])
        rol.insert(0,seleccion["Rol"])

    def regresar_a_principal():
            ventana_administrador.destroy()  
            root.deiconify()  


    ventana_administrador = tk.Toplevel(root, background=("snow2"))
    ventana_administrador.geometry("1200x600")

    label1 = tk.Label(ventana_administrador,text = "Administrador", fg ="steel blue", font = ("Arial",25)).place(x=60,y=0)

    global nombre
    global apellido
    global usuario
    global contraseña
    global rol
    global identificador
   

    #Para agregar libros
    boton_regresar = tk.Button(ventana_administrador, text="Regresar a la ventana principal",font=("Arial",12),bg="lightgrey", command=regresar_a_principal)
    boton_regresar.place(x=700, y=300)


    labelid = tk.Label(ventana_administrador, text = "ID", font = ("Arial", 12))
    labelid.place(x=35, y=50)
    
    labelnombre = tk.Label(ventana_administrador, text = "Nombre", font = ("Arial", 12))
    labelnombre.place(x=35, y=80)
    
    labelapellido = tk.Label(ventana_administrador, text = "Apellido", font = ("Arial", 12))
    labelapellido.place(x=35, y=110)

    labelusuario = tk.Label(ventana_administrador, text = "Usuario", font = ("Arial", 12))
    labelusuario.place(x=35, y=140)

    labelcontraseña = tk.Label(ventana_administrador, text = "Contraseña", font = ("Arial", 12))
    labelcontraseña.place(x=35, y=170)

    labelrol = tk.Label(ventana_administrador, text = "Rol", font = ("Arial", 12))
    labelrol.place(x=35, y=200)
    
    identificador = tk.Entry(ventana_administrador, border=1,relief='solid')
    identificador.place(x=180, y=50)
    
    nombre = tk.Entry(ventana_administrador, border=1,relief='solid')
    nombre.place(x=180, y=80)
    
    apellido = tk.Entry(ventana_administrador, border=1,relief='solid')
    apellido.place(x=180, y=110)

    usuario = tk.Entry(ventana_administrador, border=1,relief='solid')
    usuario.place(x=180, y=140)

    contraseña = tk.Entry(ventana_administrador, border=1,relief='solid')
    contraseña.place(x=180, y=170)

    rol = tk.Entry(ventana_administrador, border=1,relief='solid')
    rol.place(x=180, y=200)
    
    tk.Button(ventana_administrador,text="Agregar empleado",command=add, height=5, width=15, fg ="white", background=("green"), font=("Arial",12)).place(x=100,y=250)
    tk.Button(ventana_administrador,text="Editar empleado",command=edit, height=5, width=14, fg ="white", background=("grey"), font=("Arial",12)).place(x=300,y=250)
    tk.Button(ventana_administrador,text="Eliminar empleado",command=eliminar, height=5, width=15, fg ="white", background=("red"), font=("Arial",12)).place(x=490,y=250)
    
    columnas = ("Id","Nombre","Apellido","Usuario", "Contraseña", "Rol")
    listbox = ttk.Treeview(ventana_administrador,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=380)

    mostrar()
    listbox.bind("<Double-Button-1>",obtenerResultados)
 
def vent_empleado():
    root.withdraw()

    def filtrar():
        preciof = buscar.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursor = mysqlC.cursor()
        micursor.execute(f"SELECT * FROM libros WHERE precio = '{preciof}'")
        lista = micursor.fetchall()

        for i in listbox.get_children():
            listbox.delete(i)
        for i,(id,titulo,autor,editorial,año_publicacion,precio) in enumerate(lista, start=0):
            listbox.insert("","end", values=(id,titulo,autor,editorial,año_publicacion,precio))
            mysqlC.close()

    def mostrar():
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()
        micursos.execute("Select * from libros")
        lista = micursos.fetchall()

        for i,(id, titulo, autor, editorial, año_publicacion, precio) in enumerate(lista, start=1):
            listbox.insert("", "end", values = (id, titulo, autor, editorial, año_publicacion, precio))
            mysqlC.close()

    def add():
        tituloAdd = titulo.get()
        autorAdd = autor.get()
        editorialAdd = editorial.get()
        año_publicacionAdd = año_publicacion.get()
        precioAdd = precio.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"INSERT INTO libros(id, titulo, autor, editorial, año_publicacion, precio) values('{idAdd}','{tituloAdd}','{autorAdd}','{editorialAdd}','{año_publicacionAdd}','{precioAdd}')")
            mysqlC.commit()
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año_publicacion.delete(0,END)
            precio.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("Informacion", "Libro agregado")
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()
        actualizar()

    def actualizar():
        for i in listbox.get_children():
            listbox.delete(i)
        mostrar()

    def eliminar():
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"DELETE FROM libros WHERE id={idAdd}")
            mysqlC.commit()
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año_publicacion.delete(0,END)
            precio.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("Informacion", "Libro eliminado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def edit():
        tituloAdd = titulo.get()
        autorAdd = autor.get()
        editorialAdd = editorial.get()
        año_publicacionAdd = año_publicacion.get()
        precioAdd = precio.get()
        idAdd = identificador.get()
        mysqlC = mysql.connector.connect(host = "localhost", user = "root", password = "", database = "biblioteca")
        micursos = mysqlC.cursor()

        try:
            micursos.execute(f"UPDATE libros set titulo='{tituloAdd}', autor='{autorAdd}', editorial='{editorialAdd}', año_publicacion='{año_publicacionAdd}', precio='{precioAdd}' where id={idAdd}")
            mysqlC.commit()
            mysqlC.commit()
            titulo.delete(0,END)
            autor.delete(0,END)
            editorial.delete(0,END)
            año_publicacion.delete(0,END)
            precio.delete(0,END)
            identificador.delete(0,END)
            messagebox.showinfo("Informacion", "Libro editado")
            actualizar()
            
        except Exception as e:
            print(e)
            mysqlC.rollback()
            mysqlC.close()

    def obtenerResultados(event):
        titulo.delete(0,END)
        autor.delete(0,END)
        editorial.delete(0,END)
        año_publicacion.delete(0,END)
        precio.delete(0,END)
        identificador.delete(0,END)

        renglon = listbox.selection()[0]
        print(renglon)
        seleccion = listbox.set(renglon)
        print(seleccion)
        identificador.insert(0,seleccion["Id"])
        titulo.insert(0,seleccion["Titulo"])
        autor.insert(0,seleccion["Autor"])
        editorial.insert(0,seleccion["Editorial"])
        año_publicacion.insert(0,seleccion["Año de publicacion"])
        precio.insert(0,seleccion["Precio"])

    def regresar_a_principal():
            ventana_empleado.destroy()  
            root.deiconify() 

    ventana_empleado = tk.Toplevel(root, background=("snow2"))
    ventana_empleado.geometry("1200x600")

    label2 = tk.Label(ventana_empleado,text = "Empleados", fg ="steel blue", font = ("Arial",25)).place(x=78,y=0)

    global titulo
    global autor
    global editorial
    global año_publicacion
    global precio
    global identificador
   

    #Para agregar libros
    boton_regresar = tk.Button(ventana_empleado, text="Regresar a la ventana principal",bg="lightgrey", font = ("Arial", 12), command=regresar_a_principal)
    boton_regresar.place(x=700, y=300)

    labelid = tk.Label(ventana_empleado, text = "ID", font = ("Arial", 12))
    labelid.place(x=35, y=50)
    
    labeltitulo = tk.Label(ventana_empleado, text = "Titulo", font = ("Arial", 12))
    labeltitulo.place(x=35, y=80)
    
    labelautor = tk.Label(ventana_empleado, text = "Autor", font = ("Arial", 12))
    labelautor.place(x=35, y=110)

    labeleditorial = tk.Label(ventana_empleado, text = "Editorial", font = ("Arial", 12))
    labeleditorial.place(x=35, y=140)

    labelpublicacion = tk.Label(ventana_empleado, text = "Año de publicacion", font = ("Arial", 12))
    labelpublicacion.place(x=35, y=170)

    labelprecio = tk.Label(ventana_empleado, text = "Precio", font = ("Arial", 12))
    labelprecio.place(x=35, y=200)

    labelfiltrar = tk.Label(ventana_empleado, text = "Introduzca el año que desea", border=1,relief='ridge', font = ("Arial", 12))
    labelfiltrar.place(x=700, y=70)
    
    identificador = tk.Entry(ventana_empleado, border=1,relief='solid')
    identificador.place(x=180, y=50)
    
    titulo = tk.Entry(ventana_empleado, border=1,relief='solid')
    titulo.place(x=180, y=80)
    
    autor = tk.Entry(ventana_empleado, border=1,relief='solid')
    autor.place(x=180, y=110)

    editorial = tk.Entry(ventana_empleado, border=1,relief='solid')
    editorial.place(x=180, y=140)

    año_publicacion = tk.Entry(ventana_empleado, border=1,relief='solid')
    año_publicacion.place(x=180, y=170)

    precio = tk.Entry(ventana_empleado, border=1,relief='solid')
    precio.place(x=180, y=200)

    buscar = tk.Entry(ventana_empleado, border=1,relief='solid')
    buscar.place(x=768,y=108)
    
    tk.Button(ventana_empleado,text="Agregar libro",command=add, height=5, width=10, fg ="white",background=("green"), font=("Arial",12)).place(x=100,y=250)
    tk.Button(ventana_empleado,text="Editar libro",command=edit, height=5, width=10, fg ="white", background=("grey"), font=("Arial",12)).place(x=250,y=250)
    tk.Button(ventana_empleado,text="Eliminar libro",command=eliminar, height=5, width=10, fg ="white", background=("red"), font=("Arial",12)).place(x=400,y=250)
    boton_filtrar = tk.Button(ventana_empleado, text="Buscar",bg="lightgrey", font = ("Arial", 12), command=filtrar)
    boton_filtrar.place(x=700, y=100)
    boton_filtrar = tk.Button(ventana_empleado, text="Cancelar",bg="grey", font = ("Arial", 12), command=actualizar)
    boton_filtrar.place(x=790, y=138)
    
    columnas = ("Id","Titulo","Autor","Editorial", "Año de publicacion", "Precio")
    listbox = ttk.Treeview(ventana_empleado,columns=columnas,show="headings")
    
    for col in columnas:
        listbox.heading(col, text=col)
        listbox.grid(row=1, column=0, columnspan=1)
        listbox.place(x=0, y=380)

    mostrar()
    listbox.bind("<Double-Button-1>",obtenerResultados)
     

root = tk.Tk()
root.title("Login")
root.geometry("300x200")
 
label_usuario = tk.Label(root, text="Usuario:")
label_usuario.pack(pady=5)
entry_usuario = tk.Entry(root, width=30)
entry_usuario.pack(pady=5)
 
label_contraseña = tk.Label(root, text="Contraseña:")
label_contraseña.pack(pady=5)
entry_contraseña = tk.Entry(root, width=30, show="*")
entry_contraseña.pack(pady=5)
 
btn_login = tk.Button(root, text="Login", command=verificar_usuario)
btn_login.pack(pady=20)
 

root.mainloop()