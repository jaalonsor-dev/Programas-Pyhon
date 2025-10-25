import datetime
import json
import os
from plyer import notification

# === Funciones ===

def cargar_agenda():
    """Carga la agenda desde un archivo JSON si existe."""
    if os.path.exists("agenda.json"):
        with open("agenda.json", "r") as f:
            datos = json.load(f)
        # Convertir las claves (fechas en texto) a objetos date
        return {datetime.date.fromisoformat(k): v for k, v in datos.items()}
    return {}

def guardar_agenda(agenda):
    """Guarda la agenda en un archivo JSON."""
    with open("agenda.json", "w") as f:
        json.dump({str(k): v for k, v in agenda.items()}, f, indent=4)

def mostrar_recordatorios(agenda):
    """Muestra los recordatorios del día actual."""
    hoy = datetime.date.today()
    if hoy in agenda:
        for evento in agenda[hoy]:
            print(f"El Recordatorio para hoy: {evento}")
            # Notificación de escritorio
            notification.notify(
                title="Recordatorio de hoy",
                message=evento,
                timeout=10
            )

# === Programa principal ===

agenda = cargar_agenda()

nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {nombre}! Bienvenido a tu agenda personal.\n")

# Mostrar recordatorios del día
mostrar_recordatorios(agenda)

# Bucle principal para ingresar nuevos eventos
while True:
    datos = input("Introduce una fecha (YYYY-MM-DD) o escribe 'salir' para terminar: ")
    if datos.lower() == 'salir':
        break

    try:
        año, mes, dia = map(int, datos.split('-'))
        fecha = datetime.date(año, mes, dia)
    except ValueError:
        print("Formato de fecha erroneo. Intenta de nuevo.")
        continue

    evento = input(f"¿Qué evento quieres guardar para el {fecha}? ")
    if fecha in agenda:
        agenda[fecha].append(evento)
    else:
        agenda[fecha] = [evento]

    print(f" Evento quedo guardado para el {fecha}.\n")

# Guardar agenda al salir
guardar_agenda(agenda)

print("\n Tu agenda de eventos:")
for fecha in sorted(agenda):
    print(f"{fecha}:")
    for i, evento in enumerate(agenda[fecha], 1):
        print(f"  {i}. {evento}")

print("\n Agenda guardada en 'agenda.json'. ¡Hasta pronto!")