import globales
import ventas
import estadisticas
import time
import os


def menu_estadisticas():
    print("--- Estadisticas ---")
    print("1. Mostrar Venta Valor Más Alto")
    print("2. Mostrar Venta Iva Más Bajo")
    print("3. Promedio De Ventas")
    print("4. Media Geometrica")
    print("5. Salir")

    opcion_estadistica = globales.seleccionar_opcion(5)

    if opcion_estadistica == 1:
        estadisticas.venta_mas_alta()
    elif opcion_estadistica == 2:
        estadisticas.iva_mas_bajo()
    elif opcion_estadistica == 3:
        estadisticas.promedio_ventas()
    elif opcion_estadistica == 4:
        estadisticas.media_geometrica()
    elif opcion_estadistica == 5:
        os.system("cls")
        return

def menu_general():
    while True:
        print("1. Asignar Montos Aleatorios")
        print("2. Estadisticas")
        print("3. Salir")
        opcion = globales.seleccionar_opcion(3)

        if opcion == 1:
            print("--- Asignacion Ventas ---")
            ventas.precargar_venta()
        elif opcion == 2:
            menu_estadisticas()
        elif opcion == 3:
            print("Cerrando Programa.")
            time.sleep(2)
            print("Fin de la ejecución")
            return

#inicialzacion del programa
menu_general()