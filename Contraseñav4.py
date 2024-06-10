# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 13:57:12 2024

@author: menji
"""

import string
import random

def generar_contrasena(longitud, tipo):
    caracteres_insegura = string.ascii_lowercase
    caracteres_intermedio = string.ascii_letters + string.digits
    caracteres_segura = string.ascii_letters + string.digits + string.punctuation
    contrasena = ""
    
    if tipo == "insegura": 
        for i in range(longitud):
            contrasena += random.choice(caracteres_insegura)
    elif tipo == "segura":
        for i in range(longitud):
            contrasena += random.choice(caracteres_intermedio)
    elif tipo == "muy segura":
        for i in range(longitud):
            contrasena += random.choice(caracteres_segura)
    return contrasena

def main():
    while True:
        while True:
            try:
                longitud = int(input("Ingrese la longitud de la contraseña: "))
                break
            except ValueError:
                print("Error: Por favor ingrese un número válido para la longitud.")
        
        while True:
                tipo = input("Ingrese el tipo de contraseña ('insegura', 'segura', 'muy segura'): ").lower()
                if tipo not in ['insegura', 'segura', 'muy segura']:
                        print("Error: Tipo de contraseña no válido. Elija entre 'insegura', 'segura', 'muy segura'.")
                        continue
              
                password = generar_contrasena(longitud, tipo)
                break
            
        print("Contraseña generada: ", password)
        
        while True:
            
            aceptar = input("¿Le parece la contraseña? Escribir \n Sí \n No \n Cambiar tipo (Esta opción cambia el tipo y longitud de contraseña): ").lower()
            
            if aceptar not in ['sí', 'si', 'no','No', 'cambiar tipo']:
                print("Error: Por favor ingrese un valor valido.")
        
            else:
                if aceptar == 'sí' or aceptar == 'si':
                    print("Contraseña aceptada: ", password)
                    return
                elif aceptar == 'cambiar tipo':
                    break  # Salir del bucle de aceptación para cambiar el tipo de contraseña
                else:
                    print("Generando una nueva contraseña...")
                    password = generar_contrasena(longitud, tipo)
                    print("Su nueva contraseña es...", password)
            
               

if __name__ == "__main__":
    main()
