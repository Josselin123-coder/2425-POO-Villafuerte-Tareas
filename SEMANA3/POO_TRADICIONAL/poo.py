class Reg_Temperaturas:  #Creamos una nueva clase
    def __init__(self, semanas=4):   #Llamamos al metodo constructor
        self.semanas = semanas  # Número de semanas
        self.temperaturas = []  # Lista para guardar las temperaturas

    def ingresar_temperaturas(self):  #Creamos un metodo para ingresar la temperatura

        for semana in range(self.semanas):
            print(f"Ingrese las temperaturas para la semana {semana + 1}:")
            temp_semana = []  # Crramos una lista para guardar las temperaturas de la semana

            for dia in range(7):
                temp = int(input(f"Ingrese la temperatura del día {dia + 1}: "))
                temp_semana.append(temp)  # Guardamos en la lista temp_semana

            self.temperaturas.append(temp_semana)  # Agregamos al atributo temperaturas de la semana

    def calcular_promedios(self): #Creamos el metodo para calcular el promedio

        print("TEMPERATURAS")
        print(self.temperaturas)  # Imprimimos la lista de temperaturas

        for i, temp_semana in enumerate(self.temperaturas):
            prom = sum(temp_semana) / len(temp_semana)
            print(f"El promedio de la semana {i + 1} es: {prom:.2f}°C")  # Imprimimos el promedio


registro = Reg_Temperaturas()  # Creamos una instanciade la clase
registro.ingresar_temperaturas()  # Llamamos al metodo para ingresar las temepraturas
registro.calcular_promedios()   #Llamamos al metodo