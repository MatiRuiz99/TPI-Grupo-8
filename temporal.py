
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
                fecha_ult_precio = input("Por favor ingrese la fecha de ultimo precio: ")
                nuevo_mono = Monopatin2(marca,modelo,potencia,color,fecha_ult_precio,precio)
                nuevo_mono.cargarMonopatin2()
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
            conexion.miCursor.execute("SELECT * FROM Monopatines")
            productos = conexion.miCursor.fetchall() 
            print(productos)
            conexion.miConexion.commit()
        finally:
            conexion.cerrarConexion()

class Monopatin2:
    def __init__(self, marca, modelo, potencia, color, fechaUltimoPrecio, precio=None):
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
            conexion.miCursor2.execute("INSERT INTO Monopatines(marca,modelo,potencia,precio,color,fechaUltimoPrecio) VALUES('{}', '{}','{}','{}','{}','{}')".format(self.marca,self.modelo,self.potencia,self.precio,self.color,self.fechaUltimoPrecio))
            conexion.miConexion2.commit()
            print("Monopatin cargado exitosamente")
        except:
            print("Error al agregar un Monopatin")
        finally:
            conexion.cerrarConexion2()

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
programa.menu()