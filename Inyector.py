import os

print("\n" * 5)
print("=" * 30)
print("Programa que inyecta texto de una fuente en un formato específico.")
print("Selecciona tu archivo: ")
Directorios = os.listdir()
for archivo_paraLeer in Directorios:
    print(archivo_paraLeer)