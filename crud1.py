import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from usuarios import *
from crudMySQL import *



class clientes:

    global base
    base = None

    global textcc
    textCC = None

    global textNombre
    textNombre = None

    global textApellido
    textApellido = None

    global textid
    textid = None

    global contenedor
    contenedor = None

    global tree
    tree = None

def interfaz():
        global base
        global textcc
        global textNombre
        global textApellido
        global textid
        global contenedor
        global tree

        try:
            base = Tk()
            base.geometry("1200x500")
            base.title("CRUD")

            contenedor = LabelFrame(base, text="REGISTRO DE PERSONAL",padx=5,pady=5)
            contenedor.grid(row=0,column=0,padx=10,pady=10)

            Labelocu = Label(contenedor, text="CC: ",width=12, font=("arial",12),padx=10,pady=10).grid(row=0,column=0)
            textcc = Entry(contenedor)
            textcc.grid(row=0,column=1)

            LabelNombre = Label(contenedor, text="Nombre: ",width=12, font=("arial",12),padx=10,pady=10).grid(row=1,column=0)
            textNombre = Entry(contenedor)
            textNombre.grid(row=1,column=1)

            LabelApellido = Label(contenedor, text="Apellido: ",width=12, font=("arial",12),padx=10,pady=10).grid(row=2,column=0)
            textApellido = Entry(contenedor)
            textApellido.grid(row=2,column=1)

            Labelid = Label(contenedor, text="ID: ",width=12, font=("arial",12),padx=10,pady=10).grid(row=3,column=0)
            textid = Entry(contenedor)
            textid.grid(row=3,column=1)


            Button(contenedor, text="Guardar", width=10,command=guardarUsuarios).grid(row=4,column=0,)
            Button(contenedor, text="Modificar", width=10,command=modificacionRegistros).grid(row=4,column=1)
            Button(contenedor, text="Eliminar", width=10,command=eliminacionDatos).grid(row=4,column=2)


            contenedor = LabelFrame(base,text="TOTAL DEL PERSONAL",padx=5,pady=5,)
            contenedor.grid(row=0,column=1,padx=0,pady=5)


            tree = ttk.Treeview(contenedor,columns=("CC","Nombre","Apellido","ID"),show="headings",height=5)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1",text="CC")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2",text="Nombre")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3",text="Apellido")
            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4",text="ID")

            for row in usuarios.mostrarClientes():
                 tree.insert("","end",values=row)

            tree.bind("<<TreeviewSelect>>",seleccionRegistro)
    

            tree.pack()

            base.mainloop()
        except ValueError as error:
            print("ERROR AL MOSTRAR LA GRAFICA,error: {}".format(error))

def guardarUsuarios():
        global textcc,textNombre,textApellido,contenedor

        try:
            if textNombre is None or textApellido is None or textcc is None:
                print("Llenar los campos vacios")
                return
        
            nombre = textNombre.get()
            apellido = textApellido.get()
            cc = textcc.get()

            usuarios.ingresarUsuarios(cc,nombre,apellido)
            messagebox.showinfo("Informacion","Los datos fueron guardados")
            actualizacion_datos()

            textcc.delete(0,END)
            textNombre.delete(0,END)
            textApellido.delete(0,END)

        except ValueError as error:
            print("Error al ingresar los datos {}".format(error))

def actualizacion_datos():
    global tree

    try:
         tree.delete(*tree.get_children())
         datos = usuarios.mostrarClientes()
         for row in usuarios.mostrarClientes(): 
            tree.insert("","end",values=row)

    except ValueError as error:
         print("Erro al actualizar la tabla: {}".format(error))
    
def seleccionRegistro(event):
    try:
          datoSeleccionado = tree.focus()

          if datoSeleccionado:
               values = tree.item(datoSeleccionado)["values"]

               textcc.delete(0,END)
               textcc.insert(0,values[0])
               textNombre.delete(0,END)
               textNombre.insert(0,values[1])
               textApellido.delete(0,END)
               textApellido.insert(0,values[2])
               textid.delete(0,END)
               textid.insert(0,values[3])


    except ValueError as error:
        print("Error al seleccionar los datos: {}".format(error))

def modificacionRegistros():
        global textcc,textNombre,textApellido,textid,contenedor

        try:
            if textNombre is None or textApellido is None or textcc is None or textid is None:
                print("Llenar los campos vacios")
                return
    
            nombre = textNombre.get()
            apellido = textApellido.get()
            cc = textcc.get()
            id = textid.get()

            usuarios.modificacionDatos(cc,nombre,apellido,id)
            messagebox.showinfo("Informacion","Los datos fueron actualizados")
            actualizacion_datos()

            textcc.delete(0,END)
            textNombre.delete(0,END)
            textApellido.delete(0,END)
            textid.delete(0,END)

        except ValueError as error:
            print("Error al modificar los datos {}".format(error))

def eliminacionDatos():
        global textid,textcc,textNombre,textApellido

        try:
            if textid is None:
                print("Llenar los campos vacios")
                return

            id = textid.get()

            usuarios.eliminarUsuarios(id)
            messagebox.showinfo("Informacion","Los datos fueron eliminados")
            actualizacion_datos()

            textcc.delete(0,END)
            textNombre.delete(0,END)
            textApellido.delete(0,END)
            textid.delete(0,END)

        except ValueError as error:
            print("Error al eliminar los datos {}".format(error))

interfaz()