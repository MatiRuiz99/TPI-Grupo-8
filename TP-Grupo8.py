
import datetime
import sqlite3

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
            print("8- Mostrar monopatines de acuerdo a fecha")
            print("0- Salir de menu")
            nro = int(input("Por favor ingrese un número"))
            if nro == 1:
                marca = input("Por favor ingrese la marca del Monopatin: ")
                precio = input("Por favor ingrese el precio del Monopatin: ")
                cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                nuevo_automovil = Monopatin(marca,precio,cantidadDisponibles)
                nuevo_automovil.cargar_automovil()
            if nro ==2:
                marca = input("Por favor ingrese el nombre de la marca: ")
                precio = input("Por favor ingrese el nuevo precio: ")
                automovil_a_modificar=Monopatin(marca,precio)
                automovil_a_modificar.modificar_automoviles()   
            if nro ==3:
                marca = input("Por favor ingrese el nombre de la marca: ")
                automovil_a_borrar=Monopatin(marca)  
                automovil_a_borrar.borrar_automovil() 
            if nro ==4:
                marca = input("Por favor ingrese el nombre de la marca: ")
                automovil_a_sumar=Monopatin(marca)
                automovil_a_sumar.cargar_disponibilidad()   
            if nro ==5:
                mostrar = Monopatin('a')
                mostrar.mostrarDatos() 
            if nro ==6:
                marca = input("Por favor ingrese la marca del Monopatin: ")
                modelo = input("Por favor ingrese el modelo del Monopatin: ")
                potencia = input("Por favor ingrese la potencia del Monopatin: ")
                precio = input("Por favor ingrese el precio del Monopatin: ")
                color = input("Por favor ingrese el color del monopatin: ")
                fecha_ult_precio = datetime.datetime.now()
                nuevo_mono = Monopatin2(marca,modelo,potencia,color,fecha_ult_precio,precio)
                nuevo_mono.cargarMonopatin2()
                nuevo_mono.cargarHistorial()
                nuevo_mono.Actualizarconiva()
                
            if nro ==8:
                fecha = input("Por favor ingrese la fecha necesitar")
                ultimafecha = Monopatin2(fechaUltimoPrecio = fecha)
                ultimafecha.MostrarPorFecha()
                
            if nro==0:
                break
    
    def crearTablas(self):
        conexion = Conexiones() #Esto
        conexion.abrirConexion() #ESTO
        conexion.miCursor.execute("DROP TABLE IF EXISTS Monopatines")
        conexion.miCursor.execute("CREATE TABLE Monopatines (id_monopatin INTEGER PRIMARY KEY , marca  VARCHAR(30) ,precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca))")    
        conexion.miConexion.commit()  #ESTO     
        conexion.cerrarConexion() # ESTO SIEMPRE LO MISMO
    
    def crearTablaMono(self):
        conexion = Conexiones2() #Esto
        conexion.abrirConexion2() #ESTO
        conexion.miCursor2.execute("DROP TABLE IF EXISTS Monopatin")
        conexion.miCursor2.execute("CREATE TABLE Monopatin (id_mono INTEGER PRIMARY KEY , marca  VARCHAR(30) , modelo  VARCHAR(30) , potencia  VARCHAR(30) , precio INTEGER NOT NULL, color  VARCHAR(30) , fechaUltimoPrecio DATETIME)")    
        conexion.miConexion2.commit()  #ESTO     
        conexion.cerrarConexion2() # ESTO SIEMPRE LO MISMO
    
    def crearTablaMonoHistorial(self):
        conexion = Conexiones3() #Esto
        conexion.abrirConexion3() #ESTO
        conexion.miCursor3.execute("DROP TABLE IF EXISTS Monopatin")
        conexion.miCursor3.execute("CREATE TABLE Monopatin (id_mono INTEGER PRIMARY KEY , marca  VARCHAR(30) , modelo  VARCHAR(30) , potencia  VARCHAR(30) , precio INTEGER NOT NULL, color  VARCHAR(30) , fechaUltimoPrecio DATETIME)")    
        conexion.miConexion3.commit()  #ESTO     
        conexion.cerrarConexion3() # ESTO SIEMPRE LO MISMO

class Monopatin:
    def __init__(self, marca,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO Monopatines(marca,precio,cantidadDisponibles) VALUES('{}', '{}','{}')".format(self.marca, self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarConexion()

    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE Monopatines SET precio='{}' where marca='{}' ".format(self.precio,self.marca))
            conexion.miConexion.commit()
            print("Monopatin modificado correctamente")
        except:
            print('Error al actualizar un Monopatin')
        finally:
            conexion.cerrarConexion()  

    def borrar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("DELETE FROM Monopatines where marca='{}' ".format(self.marca))
            conexion.miConexion.commit() 
            print("Monopatin borrado correctamente") 
        except:
            print('Error al borrar un Monopatin') 
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE Monopatines SET cantidadDisponibles = cantidadDisponibles + 1 WHERE marca='{}' ".format(self.marca)) 
            conexion.miConexion.commit()
            print("Monopatin modificado correctamente")
        except:
            print('Error al actualizar un Monopatin')
        finally:
            conexion.cerrarConexion()

    def mostrarDatos(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM Monopatines ORDER BY precio ASC")
            productos = conexion.miCursor.fetchall() 
            print("ID Marca precio cantidadDisponible")
            
            for i in productos:
                print(i)
            conexion.miConexion.commit()
        finally:
            conexion.cerrarConexion()

class Monopatin2:
    def __init__(self, marca=None, modelo=None, potencia=None, color=None, fechaUltimoPrecio=None, precio=None):
        self.marca = marca
        self.modelo = modelo
        self.potencia = potencia
        self.precio=precio
        self.color = color
        self.fechaUltimoPrecio = fechaUltimoPrecio

    def cargarMonopatin2(self):
        conexion = Conexiones2()
        conexion.abrirConexion2()
        try:
            
            conexion.miCursor2.execute("INSERT INTO Monopatin(marca,modelo,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.potencia,self.precio,self.color,self.fechaUltimoPrecio))
            conexion.miConexion2.commit()
            
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarConexion2()

    def Actualizarconiva(self):
        conexion = Conexiones2()
        conexion.abrirConexion2()
        
        try:
            conexion.miCursor2.execute("UPDATE Monopatin SET precio = precio + (precio * 0.23) WHERE marca='{}' and modelo='{}' and potencia='{}' and color='{}' ".format(self.marca,self.modelo,self.potencia,self.color))
            conexion.miConexion2.commit()
            print("Monopatin actualizado exitosamente")
        except:
            print("Error al actualizar un Monopatin")
        finally:
            conexion.cerrarConexion2()

    def cargarHistorial(self):
        conexion = Conexiones3()
        conexion.abrirConexion3()
        try:
            conexion.miCursor3.execute("INSERT INTO Monopatin(marca,modelo,potencia,precio,color,fechaUltimoPrecio) VALUES('{}','{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.potencia,self.precio,self.color,self.fechaUltimoPrecio))
            conexion.miConexion3.commit()
            print("Monopatin cargado historial exitosamente")
        except:
            print("Error al agregar historial de un Monopatin")
        finally:
            conexion.cerrarConexion3()

    def MostrarPorFecha(self):
        conexion = Conexiones3()
        conexion.abrirConexion3()
        try:
            conexion.miCursor3.execute("SELECT * FROM Monopatin WHERE fechaUltimoPrecio < '{}'".format(self.fechaUltimoPrecio))
            productos = conexion.miCursor3.fetchall()
            for i in productos:
                print(i)
            conexion.miConexion3.commit()
        finally:
            conexion.cerrarConexion3()


class Conexiones3:
    def abrirConexion3(self):
        self.miConexion3 = sqlite3.connect("Hitorico_Mono")
        self.miCursor3 = self.miConexion3.cursor()
    
    def cerrarConexion3(self):
        self.miConexion3.close()

class Conexiones2:
    def abrirConexion2(self):
        self.miConexion2 = sqlite3.connect("Tienda especial")
        self.miCursor2 = self.miConexion2.cursor()

    def cerrarConexion2(self):
        self.miConexion2.close()

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Tienda")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.crearTablaMono()
programa.crearTablaMonoHistorial()
programa.menu()