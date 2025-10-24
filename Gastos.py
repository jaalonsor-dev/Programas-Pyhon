gastos = [
    ("2025-10-01", "comida", 12.50),
    ("2025-10-01", "transporte", 3.75),
    ("2025-10-02", "comida", 8.90),
    ("2025-10-03", "entretenimiento", 15.00),
    ("2025-10-04", "comida", 6.75),
    ("2025-10-04", "transporte", 2.50),
]

# Diccionario para acumular los totales por categoría
totales = {}

for fecha, categoria, monto in gastos:
    if categoria not in totales:
        totales[categoria] = 0
    totales[categoria] += monto

# Mostrar totales por categoría
for categoria, total in totales.items():
    print(f"{categoria.capitalize()}: {total:.2f}")

# Calcular y mostrar el total general
total_general = sum(totales.values())
print(f"Total general: {total_general:.2f}")
