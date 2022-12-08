import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class AplicacionArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("Artículos alejandra")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.carga_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_articulos(self):
        #Crea el Frame(ventana)
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de artículos")

        #LabelFrame(Artículo)
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        #Label de descripción
        self.label1=ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        #Cuadro de texto de descripción
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        
        #Label de precio
        self.label2=ttk.Label(self.labelframe1, text="Precio:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        #Cuadro de texto de precio
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciocarga)
        self.entryprecio.grid(column=1, row=1, padx=4, pady=4)

        #Boton de confirmar y se hace el llamado de agregar con el comant
        self.boton1=ttk.Button(
            self.labelframe1, 
            text="Confirmar", 
            command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    #Funcion que nos permite agregar un aritículo 
    def agregar(self):
        datos=(self.descripcioncarga.get(), self.preciocarga.get())
        self.articulo1.insertarArticulo(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")

    def consulta_por_codigo(self):
        #Crea el Frame(ventana)
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")

        #LabelFrame(Artículo)
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        #Label de código
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        #Cuadro de texto de código
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        #Label Descripción
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        #Cuadro de texto de Descripción
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        #Label Precio 
        self.label3=ttk.Label(self.labelframe2, text="Precio:")    
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        #Cuadro de texto de Precio
        self.precio=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe2, textvariable=self.precio, state="readonly")
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        #Boton de consultar y se hace el llamado de agregar con el comant
        self.boton1=ttk.Button(
            self.labelframe2, 
            text="Consultar", 
            command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    #Funcion que nos permiten consultar
    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.articulo1.consulta(datos)
        #Condicional que nos permite saber si la el artículo consultado existe
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.precio.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.precio.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listado_completo(self):
        #Crea el Frame(ventana)
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")

        #LabelFrame(Artículo)
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Artículo")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)

        #Boton de listado nos permite optener todo los articulos
        self.boton1=ttk.Button(
            self.labelframe3, 
            text="Listado completo", 
            command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)

        #Nos permite mostar todo los articulos dentro de un scrolledtext1
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    #Funcion que nos permite listar los aritulos en nuestro scrolledtext
    def listar(self):
        respuesta=self.articulo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+
                                              "\ndescripción:"+fila[1]+
                                              "\nprecio:"+str(fila[2])+"\n\n")

    def borrado(self):
        #Crea el Frame(ventana)
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")

        #LabelFrame(Artículo)
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Artículo")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)

        #Labeld e Código
        self.label1=ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        #Cuadro de texto de Código
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)

        #Boton para eliminar el Artículo
        self.boton1=ttk.Button(
            self.labelframe4, 
            text="Borrar", 
            command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    #Funcion para borrar el Artículo 
    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulo1.eliminar(datos)
        #Condicional que nos permite saber si el articulo existe en la base de datos 
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        #Crea el Frame(ventana)
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")

        #LabelFrame(Artículo) 
        self.labelframe5=ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe5.grid(column=0, row=0, padx=5, pady=10)

        #Label de Código
        self.label1=ttk.Label(self.labelframe5, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)

        #Cuadro de texto de Código
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe5, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        #label de Descripción
        self.label2=ttk.Label(self.labelframe5, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)

        #Cuadro de texto de Descripción
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe5, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)

        #label de Precio
        self.label3=ttk.Label(self.labelframe5, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)

        #Cuadro de texto de Precio
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe5, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)

        #Boton uno que nos permite recuperar los datos de Descripción y Precio apartir de codigo
        self.boton1=ttk.Button(
            self.labelframe5, 
            text="Consultar", 
            command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

        #Boton uno que nos permite modificar los valores de nuestro Artículo
        self.boton2=ttk.Button(self.labelframe5, text="Modificar", command=self.modifica)
        self.boton2.grid(column=1, row=4, padx=4, pady=4)

    #Funcion que nos permite modificar
    def modifica(self):
        datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulo1.modificacion(datos)
        #Condicional que nos permite saber si articulo existe
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    #Funcion que nos permite consultar
    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulo1.consulta(datos)
         #Condicional que nos permite saber si articulo existe
        if len(respuesta)>0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")


aplicacion1=AplicacionArticulos()