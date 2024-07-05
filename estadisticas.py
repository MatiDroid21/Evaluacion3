import globales
import math

def venta_mas_alta():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x["valor"], reverse=True)
    
    try:
        print("| nombre \t| valor ")
  
        for venta in ventas_ordenadas[:1]:
            print(f"| {venta['nombre']} | ${venta['valor']} |")
            input("Presione Enter Para Continuar")
    except:
        print("Ha ocurrido un error en la funcion mostrar venta más alta")
        
def iva_mas_bajo():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    ventas_ordenadas = sorted(todas_las_ventas, key=lambda x: x["iva"], reverse=False)
    
    try:
        print("| nombre \t| valor t| iva ")
  
        for venta in ventas_ordenadas[:1]:
            print(f"| {venta['nombre']} | ${venta['valor']} | ${venta['iva']} |")
            input("Presione Enter Para Continuar")
    except:
        print("Ha ocurrido un error en la funcion mostrar iva mas bajo")


def promedio_ventas():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    try:
        cantidad = 0
        suma_valor = 0

        for venta in todas_las_ventas:
            suma_valor = venta['valor']
            cantidad += 1

        promedio = suma_valor / cantidad
        print(f"El promedio de las ventas es de => {promedio}")
        #return promedio
    except:
        print("Ha ocurrido un error en la funcion promedio_ventas")

def media_geometrica():
    todas_las_ventas = globales.leer_archivo_json("./ventas.json")
    try:
        for venta in todas_las_ventas:
            suma_ventas += int(math.log(venta['valor']))
            cantidad_ventas += 1
        media_geometrica = math.exp(suma_ventas / cantidad_ventas)
        print(f"La media geometrica es -> {media_geometrica}")
        input("Presione Enter para continuar")
        return media_geometrica
    except:
        print("Ha ocurrido un error en la funcion media_geometrica")


       