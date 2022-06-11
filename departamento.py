"""Problema 3 - Departamento de fidelización. El departamento de fidelización de una empresa 
requiere almacenar información de sus clientes más fieles. La solución debe incluir mínimo 2 
clases con sus respectivos atributos y métodos (adicionales al método constructor). 
Adicionalmente, se requiere un programa que contenga las siguientes opciones en su menú.
▪Agregar cliente (nombre, cédula, teléfono, antigüedad en años, si tiene carnéde fidelización 
o no ).
▪Mostrar clientes.
▪Salir
Todos los datos de ingreso deben ser validados."""
"""
Almacenar información
2 Clases:
    - Cliente.
    - 
Menu con:
    Agregrar cliente(nombre, cédula, teléfono, antigüedad en años, tiene carnet de fidelización.)
    Mostrar clientes.
    Salir
"""
class ECB_Persona:
    def __init__(self, cedula):
        self.nombre = ""
        self.cedula = cedula
        self.telefono = ""

    def agregar(self):
        self.nombre = input("Ingrese nombre del cliente: ")
        self.telefono = input("Ingrese telefono del cliente: ")

    def mostrar(self):
        print("Cédula:     {}".format(self.cedula))
        print("Nombre:     {}".format(self.nombre))
        print("Telefono:   {}".format(self.telefono))

class ECB_Cliente(ECB_Persona):
    def __init__(self, cedula):
        ECB_Persona.__init__(self, cedula)
        self.antiguedad = 0
        self.carnet = False

    def add(self):
        self.agregar()
        self.antiguedad = int(input("Ingrese la antigüedad del cliente (Años): "))
        print("El cliente tiene carnet de fidelización?.")
        print("1. Si")
        print("Culaquier otra tecla. No")
        option = input("Ingrese la opcion: ")
        self.carnet = True if option =="1" else False

    def show(self):
        print("\n-__--__--__--__--__--_")
        print(" Datos del Cliente..")
        self.mostrar()
        print("Antigüedad: {} Años".format(self.antiguedad))
        print("Carnet:     {}".format('Si' if self.carnet else 'No'))
        print("_--__--__--__--__--__-\n\n")


if __name__ == '__main__':
    option = "2"
    dictionary = {}
    sort = {}
    anti = []
    while option != "0":
        print("1. Agregar Cliente: ")
        print("2. Mostrar Cliente: ")
        print("3. Mostrar Clientes por antiguedad: ")
        print("4. Mostrar Clientes sin carnet: ")
        print("0. Salir")
        option = input("Seleccione su opcion: ")
        if option == "1":
            cedula = input("Ingrese cédula del cliente: ")
            c1 = ECB_Cliente(cedula)
            c1.add()
            c1.show()
            dictionary[cedula] = c1
            sort[cedula] = c1.antiguedad
        elif option == "2":
            cedula = input("Ingrese cédula del cliente: ")
            show = dictionary[cedula]
            show.show()
        elif option == "3":
            print("-__--__--__Clientes por antiguedad__--__--__--__-")
            anti = sorted(sort.items(), key=lambda x:x[1], reverse=True)
            for element in anti:
                dictionary[element[0]].show()
        elif option == "4":
            print("-__--__--__Clientes sin carnet__--__--__--__-")
            for element in dictionary:
                if not dictionary[element].carnet:
                    dictionary[element].show()
        elif option == "0":
            print("Saliendo...")
        else:
            print("Opcion Incorrecta!!!")

