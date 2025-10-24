# Convertidor de unidades con menú interactivo
def mostrar_menu():
    print("\n-------------- CONVERTIDOR DE UNIDADES -----------------")
    print("""
1 - Libras a Kilos
2 - Kilos a Libras
3 - Euros a Dólares
4 - Dólares a Euros
5 - Pesos Colombianos a Dólares
6 - Dólares a Pesos Colombianos
7 - Pies a Metros
8 - Metros a Pies
9 - Salir
""")

# Diccionario de tasas de conversión
conversiones = {
    1: ("Libras a Kilos", 0.453592),
    2: ("Kilos a Libras", 2.20462),
    3: ("Euros a Dólares", 1.19),
    4: ("Dólares a Euros", 0.84),
    5: ("Pesos Colombianos a Dólares", 0.00025),
    6: ("Dólares a Pesos Colombianos", 4000),
    7: ("Pies a Metros", 0.3048),
    8: ("Metros a Pies", 3.28084)
}

# Bucle principal
while True:
    mostrar_menu()
    try:
        opcion = int(input("Ingrese la opción de conversión que desea utilizar (1-9): "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 9:
        print("Gracias por usar el convertidor. ¡Hasta pronto!")
        break

    if opcion in conversiones:
        nombre_conversion, tasa = conversiones[opcion]
        print(f"\n{nombre_conversion}")
        try:
            entrada = float(input("Ingresa la cantidad a convertir: "))
            resultado = round(entrada * tasa, 2)
            print(f"✅ El resultado de la conversión es: {resultado}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
    else:
        print("Opción inválida. Por favor, elija una opción del 1 al 9.")