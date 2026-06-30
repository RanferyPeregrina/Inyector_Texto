#No olvides: pip install pynput
import os
from pynput.keyboard import Controller

Teclado = Controller()

CarpetaTextos = 'Textos'

def LeerTexto(CarpetaTextos):

    Directorios = os.listdir(CarpetaTextos)
    for Indice, archivo_paraLeer in enumerate(Directorios):
        print(f"{Indice}.- {archivo_paraLeer}")
    print(f"{Indice + 1}.- 'Otros'")
    ArchivoElegido = int(input("Ingrese el numero de archivo que quiere leer:  "))

    if ArchivoElegido.lower() == "otros":
        pass #Aquí lo que va a pasar es una interfaz que abra una ventana de Windows para elegir tu archivo
    else:
        ArchivoElegido = os.path.join(CarpetaTextos, Directorios[ArchivoElegido])
        with open(ArchivoElegido, "r", encoding="utf-8") as Archivo:
            TextoLeido = Archivo.read()
            print("El contenido leído es el siguiente: ")
            print(TextoLeido)

    return TextoLeido

    pass

# AQUÍ INICIA EL FLUJO DEL PROGRAMA ===============================================================================

print("\n" * 5)
print("=" * 30)
print("Programa que inyecta texto de una fuente en un formato específico.")
print("Selecciona tu archivo: ")
Texto = LeerTexto(CarpetaTextos)
print('\nEl texto leído es: ')
print(Texto)
print('\n')

# ===============================================================================
# Menú para elegir el modo de inyección
print('Según el código, el texto se inyecta con la tecla PgDn. \nSi quieres cambiarle, mueve el código.')
print('\n1.- Inyectar renglón por renglón.')
print('2.- Inyectar todo el texto.')
print('3.- Cambiar de archivo.')
ModoInyeccion = int(input)

