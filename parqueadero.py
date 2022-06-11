"""
Calcular el valor a pagar por el uso del parqueadero
Sole se admiten los vehiculos:
    automoviles
    camionetas
    motos
valor por minuto:
    automoviles = $100
    camionetas  = $120
    motos       = $70
El parquedero solo funciona de 7:00 a 19:00
Se debe capturar la placa del vehiculo
Menu para seleccionar el tipo de vehiculo con su valor
Se debe capturar la hora de entrada y salida formato 24h
Como salida se debe mostrar la informacion capturada, cantidad de minutos que duro el vehiculo y el valor.
Clase
atributos
metodo capturar informacion
metodo calcular los minutos
metodo mostrar la informacion
"""

class Parqueadero:
    def __init__(self, plt_num):
        """Constructor"""
        self.plate_number = plt_num
        self.vehicle = ['automovil', 'camioneta', 'moto']
        self.vehiculo = ''
        self.price = {'automovil': 100, 'camioneta': 120, 'moto': 70}
        self.time = "hh:mm"
        self.hora_ingreso = "hh:mm"
        self.hora_salida = "hh:mm"
        self.minutes = 0
        self.total = 0

    def capturar_informacion(self):
        print("1. Automovil:    ${}".format(self.price['automovil']))
        print("2. Camioneta:    ${}".format(self.price['camioneta']))
        print("3. Moto:         $ {}".format(self.price['moto']))
        option = input("Cual es su vehiculo: ")
        if option == "1":
            self.vehiculo = self.vehicle[0]
            self.mensaje(self.vehiculo)
        elif option == "2":
            self.vehiculo = self.vehicle[1]
            self.mensaje(self.vehiculo)
        elif option == "3":
            self.vehiculo = self.vehicle[2]
            self.mensaje(self.vehiculo)
        else: 
            print("Se ha seleccionado una opcion incorreta!!!")
        aux = 0
        while aux != 1:
            self.hora_ingreso = self.valida_horas('ingreso') 
            self.hora_salida = self.valida_horas('salida')
            if (((self.hora_salida[0] * 60) + self.hora_salida[1]) > ((self.hora_ingreso[0] * 60) + self.hora_ingreso[1])
                    and 7 <= self.hora_ingreso[0] < 19 and 7 <= self.hora_salida[0] <= 19):
                print("Hora de Ingreso: {}:{}".format(str(self.hora_ingreso[0]).rjust(2, '0'),
                      str(self.hora_ingreso[1]).rjust(2, '0')))
                print("Hora de Salida: {}:{} \n\n".format(str(self.hora_salida[0]).rjust(2, '0'),
                       str(self.hora_salida[1]).rjust(2, '0')))
                aux = 1
            elif self.hora_ingreso[0] == self.hora_salida[0] and self.hora_ingreso[1] >= self.hora_salida[1]:
                print("La hora de entrada debe ser menor a la de salida!!!")
            else:
                print("Porfavor ingrese una hora entre 07:00 y 19:00!!!")
        self.calcular_minutos(self.hora_ingreso, self.hora_salida)

    def mensaje(self, vehiculo):
        print("Se ha seleccionado el vehiculo {}".format(vehiculo))

    def valida_horas(self, msj):
        aux = 1
        while aux != 0:
            self.time = input("Ingrese la hora de {} (hh:mm): ".format(msj))
            hora = self.time.split(":")
            if (hora[0].isdigit and hora[1].isdigit and int(hora[1]) < 60 and int(hora[1]) >= 0):
                aux = 0
                hora = [int(x) for x in hora]
            else:
                print("Se ha ingresado un formato erroneo!!!")
        return hora

    def calcular_minutos(self, h1, h2):
        self.minutes = ((h2[0] * 60) + h2[1]) - ((h1[0] * 60) + h1[1]) 
        self.total = self.minutes * self.price[self.vehiculo]

    def mostrar_informacion(self):
        print("-_-_-_-_-_-_{}-_-_-_-_-_-_".format(self.plate_number))
        print("Informacion de estacionamiento.")
        print("Placa Vehiculo:     {}".format(self.plate_number))
        print("Tipo de vehiculo:   {}".format(self.vehiculo))
        print("Precio por minuto:  $ {}".format(self.price[self.vehiculo]))
        print("Hora de Ingreso:    {}:{}".format(str(self.hora_ingreso[0]).rjust(2, '0'),
            str(self.hora_ingreso[1]).rjust(2, '0')))
        print("Hora de Salida:     {}:{}".format(str(self.hora_salida[0]).rjust(2, '0'),
            str(self.hora_salida[1]).rjust(2, '0')))
        print("Tiempo estacionado: {} minutos.".format(self.minutes))
        print("Precio a pagar:     $ {}".format(self.total))
        print("-_-_-_-_-_-_-_-_-_-_-_-\n\n")


if __name__ == '__main__':
    option = "2"
    dictionari = {}
    while option != "0":
        print("-_-_-_-_-_MENU PRINCIPAL-_-_-_-_-_-_")
        print("1. Agregar un Vehiculo. ")
        print("2. Ver Informacion de un Vehiculo. ")
        print("0. Salir")
        option = input("Seleccione su opcion: ")
        if option == "1":
            placa = input("Ingrese el numero de placa: ")
            pk1 = Parqueadero(placa)
            pk1.capturar_informacion()
            pk1.mostrar_informacion()
            dictionari[placa] = pk1
        elif option == "2":
            placa = input("Ingrese el numero de placa: ")
            print("\n")
            show = dictionari[placa]
            show.mostrar_informacion()
        elif option == "0":
            print("Saliendo...")
        else:
            print("Opcion Incorrecta")

