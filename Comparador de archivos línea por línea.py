# Comparador de archivos línea por línea

archivo1 = input("Ingrese el nombre del primer archivo para iniciar la comparación: ")
archivo2 = input("Ingrese el nombre del segundo archivo: ")

try:
    with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2:
        linea_num = 1
        iguales = True

        while True:
            linea1 = f1.readline()
            linea2 = f2.readline()

            # Si ambos archivos han terminado
            if not linea1 and not linea2:
                break

            # Si una línea es vacía pero la otra no (diferente longitud)
            if linea1 != linea2:
                print(f"\nDiferencia en la línea {linea_num}:")
                print(f"{archivo1}: {linea1.strip()}")
                print(f"{archivo2}: {linea2.strip()}")
                iguales = False
                break

            linea_num += 1

        if iguales:
            print("En este caso Los archivos son idénticos línea por línea.")

except FileNotFoundError:
    print(" Uno de los archivos no existe. Verifica los nombres.")
except Exception as e:
    print(f"Error inesperado: {e}")
