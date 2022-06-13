class Cliente:
    def __init__(self, cedula):
        self.nombre_cliente = ""
        self.cedula = cedula
        self.telefono = ""
    
    def capturar_cliente(self):
        print("//////////////////////////////////")
        print("Ingrese la Informacion del cliente")
        self.nombre_cliente = input("Nombre del cliente: ")
        self.telefono = input("Telefono del cliente: ")
        self.mostrar_cliente()

    def mostrar_cliente(self):
        print("//////////////////////////////////")
        print("Datos del Cliente!!!!")
        print("Nombre: {}".format(self.nombre_cliente))
        print("Cedula: {}".format(self.cedula))
        print("Telefono: {}".format(self.telefono))

class Mascota:
    def __init__(self, cedula, ident):
        self.nombre_mascota = ""
        self.edad = ""
        self.tipo = ""
        self.cedula_own = cedula
        self.ident = ident
    
    def capturar_mascota(self):
        print("///////////////////////////////////")
        print("Ingrese los datos de la Mascota")
        self.nombre_mascota = input("Nombre de la mascota: ")
        self.edad = input("Ingrese la edad de {}: ".format(self.nombre_mascota))
        self.tipo = input("Ingrese el tipo: ")
        self.mostrar_mascota()

    def mostrar_mascota(self):
        print("///////////ID: {}///////////////////".format(self.ident))
        print("Datos de la Mascota {}".format(self.nombre_mascota))
        print("Nombre: {}".format(self.nombre_mascota))
        print("Edad: {} años".format(self.edad))
        print("Tipo: {}".format(self.tipo))

if __name__ == '__main__':
    clientes = {}
    mascotas = {}
    mascotasxid = {}
    sort = {}
    opt = ""
    ident = 0
    while opt != "0":
        print("\n//////////////////////////////////")
        print("1. Registrar Mascota.")
        print("2. Mostrar Mascotas por dueño.")
        print("3. Ver todas las mascotas por edad. ")
        print("0. Salir")
        opt = input("Seleccione una opcion: ")
        if opt == "1":
            cedula = input("por favor ingrese la cédula del dueño: ")
            if cedula in clientes:
                cli = clientes[cedula]
                cli.mostrar_cliente()
            else:
                cli = Cliente(cedula)
                cli.capturar_cliente()
                clientes[cedula] = cli
            if cedula not in mascotas:
                mascotas[cedula] = []
            mas = Mascota(cedula, ident)
            mas.capturar_mascota()
            lista = mascotas[cedula]
            lista.append(mas)
            mascotas[cedula] = lista
            sort[ident] = mas.edad
            mascotasxid[ident] = mas
            ident += 1
        elif opt == "2":
            """Aqui mostramos todas las mascotas que tiene un cliente"""
            cedula = input("por favor ingrese la cédula del dueño: ")
            cli = clientes[cedula]
            mas = mascotas[cedula]
            print("Representacion de Datos")
            cli.mostrar_cliente()
            # Tenemos un bucle aqui abajito
<<<<<<< HEAD
            print("Aqui quiero agregar un bucle")
            for elm in mas:
                elm.mostrar_mascota()
=======
            for element in mas:
                element.mostrar_mascota()
>>>>>>> refs/remotes/origin/main
            print("\n\n\n")
        elif opt == "3":
            """No se me occurren muchos cambios para hacer pruebas y ver como esta funcionando correctamente. """
            print("\n\n////////Mascotas por edad.////")
            ordenar = sorted(sort.items(), key=lambda x:x[1], reverse=False)
<<<<<<< HEAD
            for elm in ordenar:
                mascotasxid[elm[0]].mostrar_mascota()
=======
            for elemento in ordenar:
                mascotasxid[elemento[0]].mostrar_mascota()
>>>>>>> refs/remotes/origin/main
        elif opt == "0":
            print("Saliendo...")
        else:
            print("Por favor digite una opcion valida!!")

"""
This also added by user 1
"""
