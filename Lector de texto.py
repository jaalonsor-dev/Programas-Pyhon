import os

def contar_lineas_palabras_caracteres(nombre_archivo):
  
    if not os.path.exists(nombre_archivo):
        print(f" X Error: El archivo '{nombre_archivo}' no fue encontrado.")
        return

    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        total_lineas = len(lineas)
        total_palabras = 0
        total_caracteres = 0

        for linea in lineas:
            total_palabras += len(linea.split())
            total_caracteres += len(linea.replace(" ", "").replace("\n", ""))

        print(f"\n📄 Resultados para el archivo: '{nombre_archivo}'")
        print("===============================================")
        print(f"La Cantidad total de líneas dentro del texto es de : {total_lineas}")
        print(f"La Cantidad total de palabras: {total_palabras}")
        print(f"La Cantidad total de caracteres (sin espacios ni saltos de línea): {total_caracteres}")
        print("===============================================\n")

    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")

def mostrar_menu():
 
    while True:
        print("=== Menú Principal del analizador del texto ===")
        print("1. Contar líneas, palabras y caracteres de un archivo")
        print("2. Salir del programa")
        opcion = input("Elige una opción (1 o 2): ")

        if opcion == '1':
            nombre_archivo = input("Ingresa el nombre del archivo de texto (ej. mi_archivo.txt): ")
            contar_lineas_palabras_caracteres(nombre_archivo)
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingresa '1' o '2'.")

# Inicia el programa
if __name__ == "__main__":
    mostrar_menu()
