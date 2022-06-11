"""
Grupos de 3 personas
El viaje dura 2 días
Cada grupo registrar lo que necesita
--Desayuno los 2 días $30.000
--Almuerzo los 2 días $60.000
--Cena los 2 días     $60.000
El resultado es el valor a pagar por el grupo
El usuario debe validar los datos ingresados
"""
class Group:
    def __init__(self, name):
        self.name = name
        self.userservices = {}
        self.services = ['Desayuno', 'Almuerzo', 'Cena']
        self.price = {'Desayuno': 30000, 'Almuerzo': 60000, 'Cena': 60000}
        self.total = 0

    def agregra(self):
        i = 0
        while i < len(self.services):
            element = self.services[i]
            myelement  = input("Desea adquirir el servicio de {} (si / no): ".format(element))
            if(myelement == "si"):
                self.userservices[element] = True
                print("Se ha agregado {} a la lista\n".format(element))
                i += 1
            elif(myelement == "no"):
                self.userservices[element] = False
                print("Se ha descartado {} de la lista\n".format(element))
                i += 1
            else:
                print("Se ha seleccionado una opcion incorrecta!!\n")
    
    def validar(self):
        self.total = 0
        print("Servicios Contratados para {}.".format(self.name))
        print("-_-_-_-_-_-_-_-_-_-_-_")
        for element in self.services:
            if self.userservices[element] == True:
                print("{}: $ {}".format(element, self.price[element]))
                self.total += self.price[element]
        print("Total a Pagar: $ {}\n\n".format(self.total))

if __name__ == '__main__':
    option = "2"
    dictionari = {}
    while option != "0":
        print("1. Agregar grupo: ")
        print("2. Ver grupo: ")
        print("0. Salir")
        option = input("Seleccione su opcion: ")
        if option == "1":
            name = input("Nombre del grupo: ")
            g1 = Group(name)
            g1.agregra()
            g1.validar()
            dictionari[name] = g1
        elif option == "2":
            name = input("Nombre del grupo:")
            show = dictionari[name]
            show.validar()
        elif option == "0":
            print("Saliendo...")
        else:
            print("Opcion Incorrecta")

