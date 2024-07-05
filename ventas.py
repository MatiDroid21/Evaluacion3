import globales
import random
import os
import math

def precargar_venta():
    ventas = globales.leer_archivo_json('./ventas.json')
    productos = globales.leer_archivo_json('./productos.json')

    for i in range(10): #10 por las cantidad de ventas solicitadas
        try:
            producto = random.choice(productos)['producto']
            venta = random.randint(2000, 10000)
            iva = venta * 0.19
            
            nueva_venta = {
                "nombre":producto,
                "valor":venta,
                "iva":iva
            }
            ventas.append(nueva_venta)
            print("Ventas cargadas")
        except:
           print("Error En Precargar Venta")

    globales.guardar_archivo_json("ventas.json",ventas)