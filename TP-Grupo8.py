
import datetime
import sqlite3
from timeit import repeat

class ProgramaPrincipal:

    def menu(self):
        while True:
            print("Menu de opciones Concesionaria")
            print("1- Cargar Monopatin")
            print("2- Modificar Monopatin")
            print("3- Borrar Monopatin")
            print("4- Cargar disponibilidad")
            print("5- Mostrar datos")
            print("6- Tabla monopatin especial")
            print("7- Mostrar monopatines de acuerdo a fecha")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número: "))
            marca = modelo = potencia = color = ''
            precio = cantidadDisponibles = dia = mes = año = hora = -1
            if nro == 1:
                marca = generico(marca)
                precio = obtenerprecio(precio)
                while cantidadDisponibles < 0:
                    cantidadDisponibles = int(input("Por favor ingrese la cantidad de unidades disponibles: "))
                    if cantidadDisponibles < 0:
                        print("Ingrese un numero mayor a 0")
                nuevo_automovil = Monopatin(marca,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro == 2:
                marca = generico(marca)
                precio = obtenerprecio(precio)
                automovil_a_modificar=Monopatin(marca,precio)
                automovil_a_modificar.modificar_automoviles()   
            if nro == 3:
                marca = generico(marca)
                automovil_a_borrar=Monopatin(marca)  
                automovil_a_borrar.borrar_automovil() 
            if nro == 4: 
                marca =generico(marca)
                automovil_a_sumar=Monopatin(marca)
                automovil_a_sumar.cargar_disponibilidad()   
            if nro == 5:
                mostrarDatos() 
            if nro == 6:
                modelo = potencia = color = ''
                precio = -1
                marca = generico(marca)
                while modelo == '':
                    modelo = input("Por favor ingrese el modelo del Monopatin: ")
                while potencia == '':
                    potencia = input("Por favor ingrese la potencia del Monopatin: ")
                precio = obtenerprecio(precio)
                while color == '':
                    color = input("Por favor ingrese el color del monopatin: ")
                fecha_ult_precio = datetime.datetime.now()
                nuevo_mono = Monopatin2(marca,modelo,potencia,color,fecha_ult_precio,precio)
                nuevo_mono.cargarMonopatin2()
                nuevo_mono.cargarHistorial()
                nuevo_mono.Actualizarconiva()
            if nro == 7:
                while dia < 1 or dia > 31:
                    dia = int(input("Por favor ingrese dia : "))
                while mes < 1 or mes > 12:
                    mes = int(input("Por favor ingrese mes: "))
                while año < 1 :
                    año = int(input("por favor ingrese año: "))
                while hora < 0 or hora > 23:
                    hora = int(input("Por favor ingrese hora: "))
                fecha = f'{año}-{mes}-{dia} {hora}:00:00'
                MostrarPorFecha(fecha)
                MostrarPorFechaHistorica(fecha)           
            if nro == 0:
                break

    def crearTablas(self):
        conexion = Tienda() #Esto
        conexion.abrirTienda() #ESTO
        conexion.miCursorTienda.execute("DROP TABLE IF EXISTS Monopatines")
        conexion.miCursorTienda.execute("CREATE TABLE Monopatines (id_monopatin INTEGER PRIMARY KEY , marca  VARCHAR(30) ,precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca))")    
        conexion.miConexion.commit()  #ESTO     
        conexion.cerrarTienda() # ESTO SIEMPRE LO MISMO
    
    def crearTablaMono(self):
        conexion = Productos() #Esto
        conexion.abrirProductos() #ESTO
        conexion.miCursorProductos.execute("DROP TABLE IF EXISTS Monopatin")
        conexion.miCursorProductos.execute("CREATE TABLE Monopatin (id_mono INTEGER PRIMARY KEY , marca  VARCHAR(30) , modelo  VARCHAR(30) , potencia  VARCHAR(30) , precio INTEGER NOT NULL, color  VARCHAR(30) , fechaUltimoPrecio DATETIME)")    
        conexion.miProducto.commit()  #ESTO     
        conexion.cerrarProductos() # ESTO SIEMPRE LO MISMO
    
    def crearTablaMonoHistorial(self):
        conexion = Historial() #Esto
        conexion.abrirHistorial() #ESTO
        conexion.miCursorHistorial.execute("DROP TABLE IF EXISTS Monopatin")
        conexion.miCursorHistorial.execute("CREATE TABLE Monopatin (id_mono INTEGER PRIMARY KEY , marca  VARCHAR(30) , modelo  VARCHAR(30) , potencia  VARCHAR(30) , precio INTEGER NOT NULL, color  VARCHAR(30) , fechaUltimoPrecio DATETIME)")    
        conexion.miHistorial.commit()  #ESTO     
        conexion.cerrarHistorial() # ESTO SIEMPRE LO MISMO

def generico(marca):
    marca = input("Por favor ingrese la marca del Monopatin: ")
    if marca == '':
            marca = 'Generico'
    return marca

def obtenerprecio(precio):
    while precio < 0:
        precio = float(input("Por favor ingrese el nuevo precio: "))
        if precio < 0:
            print("Ingrese un numero mayor a 0")
    return precio

class Monopatin:
    def __init__(self, marca,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Tienda()
        conexion.abrirTienda()
        try:
            conexion.miCursorTienda.execute("INSERT INTO Monopatines(marca,precio,cantidadDisponibles) VALUES('{}', '{}','{}')".format(self.marca, self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarTienda()

    
    def modificar_automoviles(self):
        conexion = Tienda()
        conexion.abrirTienda()
        try:
            conexion.miCursorTienda.execute("UPDATE Monopatines SET precio='{}' where marca='{}' ".format(self.precio,self.marca))
            conexion.miConexion.commit()
            print("Monopatin modificado correctamente")
        except:
            print('Error al actualizar un Monopatin')
        finally:
            conexion.cerrarTienda()  

    def borrar_automovil(self):
        conexion = Tienda()
        conexion.abrirTienda()
        try:
            conexion.miCursorTienda.execute("DELETE FROM Monopatines where marca='{}' ".format(self.marca))
            conexion.miConexion.commit() 
            print("Monopatin borrado correctamente") 
        except:
            print('Error al borrar un Monopatin') 
        finally:
            conexion.cerrarTienda()

    def cargar_disponibilidad(self):
        conexion = Tienda()
        conexion.abrirTienda()
        try:
            conexion.miCursorTienda.execute("UPDATE Monopatines SET cantidadDisponibles = cantidadDisponibles + 1 WHERE marca='{}' ".format(self.marca)) 
            conexion.miConexion.commit()
            print("Monopatin modificado correctamente")
        except:
            print('Error al actualizar un Monopatin')
        finally:
            conexion.cerrarTienda()

def mostrarDatos():
    conexion = Tienda()
    conexion.abrirTienda()
    try:
        conexion.miCursorTienda.execute("SELECT * FROM Monopatines ORDER BY precio ASC")
        productos = conexion.miCursorTienda.fetchall() 
        print("ID Marca precio cantidadDisponible")
            
        for i in productos:
            print(i)
        conexion.miConexion.commit()
    finally:
        conexion.cerrarTienda()

class Monopatin2:
    def __init__(self, marca, modelo, potencia, color, fechaUltimoPrecio, precio):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.precio=precio
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio

    def cargarMonopatin2(self):
        conexion = Productos()
        conexion.abrirProductos()
        try:
            
            conexion.miCursorProductos.execute("INSERT INTO Monopatin(marca,modelo,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.potencia,self.precio,self.color,self.fechaUltimoPrecio))
            conexion.miProducto.commit()
            
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarProductos()

    def Actualizarconiva(self):
        conexion = Productos()
        conexion.abrirProductos()
        
        try:
            conexion.miCursorProductos.execute("UPDATE Monopatin SET precio = precio + (precio * 0.23) WHERE marca='{}' and modelo='{}' and potencia='{}' and color='{}' ".format(self.marca,self.modelo,self.potencia,self.color))
            conexion.miProducto.commit()
            print("Monopatin actualizado exitosamente")
        except:
            print("Error al actualizar un Monopatin")
        finally:
            conexion.cerrarProductos()

    def cargarHistorial(self):
        conexion = Historial()
        conexion.abrirHistorial()
        try:
            conexion.miCursorHistorial.execute("INSERT INTO Monopatin(marca,modelo,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.potencia,self.precio,self.color,self.fechaUltimoPrecio))
            conexion.miHistorial.commit()
            print("Monopatin cargado historial exitosamente")
        except:
            print("Error al agregar historial de un Monopatin")
        finally:
            conexion.cerrarHistorial()

def MostrarPorFechaHistorica(fecha):
    conexion = Historial()
    conexion.abrirHistorial()
    try:
        conexion.miCursorHistorial.execute("SELECT * FROM Monopatin WHERE fechaUltimoPrecio < '{}'".format(fecha))
        productos = conexion.miCursorHistorial.fetchall()
        print("")
        print("Precio historial")
        for i in productos:
            print(i)
        conexion.miHistorial.commit()
    finally:
        conexion.cerrarHistorial()

def MostrarPorFecha(fecha):
    conexion = Productos()
    conexion.abrirProductos()
    try:
        conexion.miCursorProductos.execute("SELECT * FROM Monopatin WHERE fechaUltimoPrecio < '{}'".format(fecha))
        productos = conexion.miCursorProductos.fetchall()
        print("")
        print("Precio luego del aumento")
        for i in productos:
            print(i)
        conexion.miProducto.commit()
    finally:
        conexion.cerrarProductos()

class Historial:
    def abrirHistorial(self):
        self.miHistorial = sqlite3.connect("Hitorico_Mono")
        self.miCursorHistorial = self.miHistorial.cursor()
    
    def cerrarHistorial(self):
        self.miHistorial.close()

class Productos:
    def abrirProductos(self):
        self.miProducto = sqlite3.connect("Monopatin")
        self.miCursorProductos = self.miProducto.cursor()

    def cerrarProductos(self):
        self.miProducto.close()

class Tienda:
    
    def abrirTienda(self):
        self.miConexion = sqlite3.connect("Tienda")
        self.miCursorTienda = self.miConexion.cursor()
        
    def cerrarTienda(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablaMono()
programa.crearTablaMonoHistorial()
programa.menu()