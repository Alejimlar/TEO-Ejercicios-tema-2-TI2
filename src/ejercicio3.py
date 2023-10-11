from ejercicio1 import lee_variaciones_temperatura
from matplotlib import pyplot
from datetime import date

def muestra_variaciones_temperatura(ruta_csv, fecha_inicial, fecha_final):

    #suponemos que fecha_inicial y fecha_final son del tipo date

    datos = lee_variaciones_temperatura(ruta_csv)

    #Posible solución: buscar la fecha mínima de datos
    # if fecha_inicial == None:
    #     fecha_inicial = min(datos)


    #Esquema filtrado
    datos_filtrados = []
    for fecha, temp in datos:
        if fecha_inicial <= fecha <= fecha_final:
        # if fecha_inicial == None or fecha_inicial <= fecha:
        # if (fecha_inicial == None or fecha_inicial <= fecha) and\
        #     (fecha_inicial == None or fecha_inicial <= fecha):

            tupla = (fecha, temp)
            datos_filtrados.append(tupla)

    #Esquema transformación
    valores_x = []
    valores_y = []
    for fecha, temp in datos_filtrados:
        valores_x.append(fecha)
        valores_y.append(temp)

    pyplot.title("Variación de temperaturas medias del planeta")
    pyplot.plot(valores_x, valores_y)
    pyplot.show()


if __name__ == '__main__':
    muestra_variaciones_temperatura("data/monthly_csv.csv", date(2001,1,1), date(2017,1,1))

    #todo: permitir valores None en los parámetros
    muestra_variaciones_temperatura("data/monthly_csv.csv", None, date(2017, 1, 1))
    muestra_variaciones_temperatura("data/monthly_csv.csv", date(2017, 1, 1), None)