import pandas as pd
from datetime import datetime

# Función para registrar un gasto con validación de fecha
def registrar_gasto(df):
    categoria = input("Ingrese la categoría del gasto: ")
    monto = 0
    while True:
        try:
            monto = float(input("Ingrese el monto del gasto: "))
            break
        except ValueError:
            print("Monto inválido. Por favor, ingrese un número.")

    while True:
        fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
        try:
            fecha_valida = datetime.strptime(fecha, "%Y-%m-%d")
            break
        except ValueError:
            print("Formato de fecha incorrecto. Use YYYY-MM-DD (ejemplo: 2025-10-24).")

    nuevo_gasto = {'Categoría': categoria, 'Monto': monto, 'Fecha': fecha}
    df = pd.concat([df, pd.DataFrame([nuevo_gasto])], ignore_index=True)
    print("Gasto registrado correctamente.")
    return df

# Función para evaluar estado financiero
def evaluar_ahorro(df, ingreso_mensual):
    total_gastos = df['Monto'].sum()
    ahorro = ingreso_mensual - total_gastos
    porcentaje_ahorro = (ahorro / ingreso_mensual) * 100

    print("\n--- Evaluación Financiera ---")
    print(f"Ingreso mensual: ${ingreso_mensual:.2f}")
    print(f"Gastos totales: ${total_gastos:.2f}")
    print(f"Ahorro estimado: ${ahorro:.2f} ({porcentaje_ahorro:.2f}%)")

    if porcentaje_ahorro >= 20:
        print("Estás ahorrando más del 20%. Buen trabajo.")
    elif porcentaje_ahorro < 0 or total_gastos > ingreso_mensual * 0.8:
        print("Estás en números rojos. Has gastado más del 80% de tu ingreso.")
    else:
        print("Tu ahorro es menor al ideal. Intenta reducir tus gastos.")

# Función principal
def main():
    nombre = input("¿Cuál es tu nombre? ")
    print(f"\nHola, {nombre}. Bienvenido a tu gestor de gastos.")

    try:
        df_gastos = pd.read_csv('gastos.csv')
    except FileNotFoundError:
        df_gastos = pd.DataFrame(columns=['Categoría', 'Monto', 'Fecha'])

    while True:
        try:
            ingreso_mensual = float(input("Ingresa tu ingreso mensual estimado: "))
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar gasto")
        print("2. Evaluar ahorro")
        print("3. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            df_gastos = registrar_gasto(df_gastos)
        elif opcion == '2':
            evaluar_ahorro(df_gastos, ingreso_mensual)
        elif opcion == '3':
            df_gastos.to_csv('gastos.csv', index=False)
            print("Datos guardados. Hasta luego.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
if __name__ == "__main__":
    main()
