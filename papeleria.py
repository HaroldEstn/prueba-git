"""
Informar varol de imprimir y empastar tesis de grado.
2 tipos de material:
    -Papel cuero: $30.000
    -Percalina: $20.000

precio por imprimir hoja: $65
precio adicional por imagen: $30

Datos:
    -Nombre
    -Identificacion
    -Numero de hojas
    -Numero de imagenes
    -tipo de papel

Mostrar:
    -Nombre
    -Identificacion
    -Numero de hojas
    -Numero de imagenes
    -tipo de papel
    -total a pagar
    -empaste?

clase:
    atributos.
    metodo constructos.
    metodo capturar.
    metodo calcular.
    metodo mostrar.
    
"""

class Empastar:
    def __init__(self, iden):
        self.nombre = ""
        self.identificacion = iden
        self.num_sheets = 0
        self.num_pics = 0
        self.paper = ""
        self.paper_type = {'Cuero': 30000, 'Percalina': 20000}
        self.imprimir = {'hoja': 65, 'imagen': 30}
        self.total = 0

    def capturar(self):
        self.nombre = input("Ingrese nombre del cliente: ") 
        self.num_sheets = int(input("Ingrese numero de hojas: "))
        self.num_pics = int(input("Ingrese numero de imagenes: "))
        opt = False
        while not opt:
            print("Seleccione tipo de papel: ")
            print("1. Papel cuero.")
            print("2. Percalina.")
            opcion = input("Seleccione una opcion: ")
            if opcion == "1":
                self.paper = "Cuero"
                opt = True
            if opcion == "2":
                self.paper = "Percalina"
                opt = True
            else:
                print("Error!!!")
        self.calcular()

    def calcular(self):
        self.total = ((self.num_sheets * self.imprimir['hoja']) + (self.num_pics * self.imprimir['imagen']) 
                      + self.paper_type[self.paper])

    def mostrar(self):
        print("\n .....Informacion......")
        print("Identificacion:     {}".format(self.identificacion))
        print("Nombre:             {}".format(self.nombre))
        print("Numero de hojas:    {}".format(self.num_sheets))
        print("Precio de hojas:    $ {}".format(self.imprimir['hoja'] * self.num_sheets))
        print("Numero de imagenes: {}".format(self.num_pics))
        print("Precio de Imagenes: $ {}".format(self.imprimir['imagen'] * self.num_pics))
        print("Tipo de papel:      {}".format(self.paper))
        print("Precio del papel:   $ {}".format(self.paper_type[self.paper]))
        print("     Total:         $ {}".format(self.total))
        print("........................\n\n")

if __name__ == '__main__':
    opt = ""
    miobjects = {}
    while opt != "0":
        print("1. Capturar Datos.")
        print("2. Mostrar Cliente.")
        print("0. Salir")
        opt = input("Seleccione una opcion: ")
        if opt == "1":
            identidad = input("Ingrese el numero de identificacion: ")
            emp = Empastar(identidad)
            emp.capturar()
            emp.mostrar()
            miobjects[identidad] = emp
        elif opt == "2":
            identidad = input("Ingrese el numero de identificacion a consultar: ")
            miobjects[identidad].mostrar()
        elif opt == "0":
            print("Hasta luego...")
        else:
            print("No se encontro esa opcion!!!!")

