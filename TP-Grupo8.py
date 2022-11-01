
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
            print("6- Cargar producto especifico")
            print("7- Mostrar monopatines de acuerdo a fecha")
            print("8- Aumentar precio en 23%")
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
                nuevo_monopatin = Monopatin(marca,precio,cantidadDisponibles = cantidadDisponibles)
                nuevo_monopatin.cargar_monopatin()
            if nro == 2:
                marca = generico(marca)
                precio = obtenerprecio(precio)
                monopatin_a_modificar=Monopatin(marca,precio)
                monopatin_a_modificar.modificar_monopatines()   
            if nro == 3:
                marca = generico(marca)
                monopatin_a_borrar=Monopatin(marca)  
                monopatin_a_borrar.borrar_monopatin() 
            if nro == 4: 
                marca =generico(marca)
                monopatin_a_sumar=Monopatin(marca)
                monopatin_a_sumar.cargar_disponibilidad()   
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
                nuevo_mono = Monopatin(marca,precio,modelo,potencia,color,fechaUltimoPrecio=fecha_ult_precio)
                nuevo_mono.cargarMonopatin2()
                
                
            if nro == 7:
                while dia < 1 or dia > 31:
                    dia = int(input("Por favor ingrese dia : "))
                while mes < 1 or mes > 12:
                    mes = int(input("Por favor ingrese mes: "))
                while año < 1 :
                    año = int(input("por favor ingrese año: "))
                fecha = f'{año}-{mes}-{dia} 00:00:00'
                MostrarPorFecha(fecha)
                MostrarPorFechaHistorica(fecha)  
            if nro == 8:
                fecha = datetime.datetime.now()
                nuevo_iva=Monopatin(fechaUltimoPrecio=fecha)
                cargarhistorial()
                nuevo_iva.Actualizarconiva()         
            if nro == 0:
                break

    def crearTablas(self):
        conexion = Tienda() #Esto
        conexion.abrirTienda() #ESTO
        conexion.miCursorTienda.execute("DROP TABLE IF EXISTS Monopatines")
        conexion.miCursorTienda.execute("CREATE TABLE Monopatines (id_monopatin INTEGER PRIMARY KEY , marca  VARCHAR(30) ,precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca))")
        conexion.miCursorTienda.execute("DROP TABLE IF EXISTS Monopatin")
        conexion.miCursorTienda.execute("CREATE TABLE Monopatin (id_mono INTEGER PRIMARY KEY , marca  VARCHAR(30) , modelo  VARCHAR(30) , potencia  VARCHAR(30) , precio INTEGER NOT NULL, color  VARCHAR(30) , fechaUltimoPrecio DATETIME)")  
        conexion.miCursorTienda.execute("DROP TABLE IF EXISTS MonopatinH")
        conexion.miCursorTienda.execute("CREATE TABLE MonopatinH (mono INTEGER NOT NULL , marca  VARCHAR(30) , modelo  VARCHAR(30) , potencia  VARCHAR(30) , precio INTEGER NOT NULL, color  VARCHAR(30) , fechaUltimoPrecio DATETIME)")  
        conexion.miConexion.commit()  #ESTO     
        conexion.cerrarTienda() # ESTO SIEMPRE LO MISMO

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
    def __init__(self, marca=None,precio=None, modelo=None, potencia=None, color=None, fechaUltimoPrecio=None, cantidadDisponibles=None):
        self.marca = marca
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        self.modelo = modelo
        self.potencia = potencia
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio
        
    def cargar_monopatin(self):
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

    
    def modificar_monopatines(self):
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

    def borrar_monopatin(self):
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


    def cargarMonopatin2(self):
        conexion = Tienda()
        conexion.abrirTienda()
        try:
            
            conexion.miCursorTienda.execute("INSERT INTO Monopatin(marca,modelo,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.potencia,self.precio,self.color,self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarTienda()


    def Actualizarconiva(self):
        conexion = Tienda()
        conexion.abrirTienda()
        try:
            
            conexion.miCursorTienda.execute("UPDATE Monopatin SET precio = round(precio + (precio * 0.23))")
            conexion.miCursorTienda.execute("UPDATE Monopatin SET fechaUltimoPrecio='{}'" .format(self.fechaUltimoPrecio))
            conexion.miConexion.commit()
            print("Monopatin actualizado exitosamente")
        except:
            print("Error al actualizar un Monopatin")
        finally:
            conexion.cerrarTienda()

def mostrarDatos():
    conexion = Tienda()
    conexion.abrirTienda()
    try:
        conexion.miCursorTienda.execute("SELECT * FROM Monopatines ORDER BY precio ASC")
        prod = conexion.miCursorTienda.fetchall() 
        print("ID Marca precio cantidadDisponible")
            
        for i in prod:
            print(i)
        conexion.miConexion.commit()
    finally:
        conexion.cerrarTienda()

def cargarhistorial():
    conexion = Tienda()
    conexion.abrirTienda()
    try:
        conexion.miCursorTienda.execute("INSERT INTO MonopatinH(mono,marca,modelo,potencia,precio,color,fechaUltimoPrecio) SELECT id_mono, marca, modelo, potencia, precio, color, fechaUltimoPrecio FROM Monopatin")
        conexion.miConexion.commit()
        print("Monopatin cargado historial exitosamente")
    except:
        print("Error al agregar historial de un Monopatin")
    finally:
        conexion.cerrarTienda()

def MostrarPorFechaHistorica(fecha):
    conexion = Tienda()
    conexion.abrirTienda()
    try:
        conexion.miCursorTienda.execute("SELECT * FROM MonopatinH WHERE fechaUltimoPrecio < '{}' ORDER BY mono ASC".format(fecha))
        prod = conexion.miCursorTienda.fetchall()
        print("")
        print("Precio historial")
        for i in prod:
            print(i)
        conexion.miConexion.commit()
    finally:
        conexion.cerrarTienda()

def MostrarPorFecha(fecha):
    conexion = Tienda()
    conexion.abrirTienda()
    try:
        conexion.miCursorTienda.execute("SELECT * FROM Monopatin WHERE fechaUltimoPrecio < '{}'".format(fecha))
        prod = conexion.miCursorTienda.fetchall()
        print("")
        print("Precio luego del aumento")
        for i in prod:
            print(i)
        conexion.miConexion.commit()
    finally:
        conexion.cerrarTienda()

class Tienda:
    
    def abrirTienda(self):
        self.miConexion = sqlite3.connect("Tienda")
        self.miCursorTienda = self.miConexion.cursor()
        
    def cerrarTienda(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()