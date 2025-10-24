print("---Bienvenido al cajero automático---")

saldo = 100000

# Diccionario con denominaciones y cantidad de billetes disponibles
billetes = {
    100: 10,
    50: 20,
    20: 30,
    10: 40,
    5: 50,
    1: 100
}

def entregar_billetes(monto):
    entrega = {}
    for denom in sorted(billetes.keys(), reverse=True):
        cantidad = min(monto // denom, billetes[denom])
        if cantidad > 0:
            entrega[denom] = cantidad
            monto -= denom * cantidad
    if monto == 0:
        return entrega
    else:
        return None

salir = False

while not salir:
    print("\n-----Selecciona una opción-----")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Salir del sistema")

    op = input("Opción: ")

    if op == "1":
        print(f"El saldo es: ${saldo}")
    elif op == "2":
        try:
            monto_retirar = int(input("Ingrese el monto a retirar: "))
            if monto_retirar > saldo:
                print("Fondos insuficientes.")
            else:
                resultado = entregar_billetes(monto_retirar)
                if resultado:
                    print("Billetes entregados:")
                    for denom, cant in resultado.items():
                        print(f"${denom} x {cant}")
                        billetes[denom] -= cant
                    saldo -= monto_retirar
                else:
                    print("No se puede entregar el monto con los billetes disponibles.")
        except ValueError:
            print("Por favor ingrese un número válido.")
    elif op == "3":
        try:
            monto_depositar = int(input("Ingrese el monto a depositar: "))
            saldo += monto_depositar
            print(f"Nuevo saldo: ${saldo}")
        except ValueError:
            print("Por favor ingrese un número válido.")
    elif op == "4":
        print("-----Saliendo del sistema-----\n----1Gracias por usar el cajero---")
        salir = True
    else:
        print("Opción inválida. Intente nuevamente.")