def datos():
    semanas = 4  # Colocamos el numero de semanas
    temperaturas = []  # Creamos una lista para almacenar las temperaturas

    # Utilizamos el ciclo for para cada semana
    for semana in range(semanas):
        print(f"Ingrese las temperaturas para la semana {semana + 1}:")  #Pedimos al usuario que ingrese las temperaturas de la semana
        temp_semana = []  # Creamos una lista para guardar las temperaturas

        #Creamos otro bucle for para ingresar temperaturas para 7 días
        for dia in range(7):
            temp = int(input(f"Ingrese la temperatura del día {dia + 1}: ")) #Ingresamos las temperaturas
            temp_semana.append(temp)  #Guardamos en la lista tem_semana

        # Agregar las temperaturas de la semana a la lista principal

        temperaturas.append(temp_semana)
    print("TEMPERATURAS")
    print(temperaturas) #Imprimimos la lista temperaturas
    # Calcular y mostrar el promedio de cada semana
    for i, temp_semana in enumerate(temperaturas):
        prom = sum(temp_semana) / len(temp_semana)
        print(f"El promedio de la semana {i + 1} es: {prom:.2f}°C") #Imprimimos el promedio de la tempratura para cada semana

datos()  #Llamamos a nuestra funcion datos


