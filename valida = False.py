valida = False

while not valida:
    contraseña1 = input("Ingrese su contraseña: ")

    if len(contraseña1) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        continue

    tiene_mayuscula = any(c.isupper() for c in contraseña1)
    tiene_minuscula = any(c.islower() for c in contraseña1)
    tiene_numero = any(c.isdigit() for c in contraseña1)
    tiene_simbolo = any(c in "!@#$%^&*()-_+=" for c in contraseña1)

    if not (tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_simbolo):
        print("La contraseña debe contener al menos:")
        print("- Una letra mayúscula")
        print("- Una letra minúscula")
        print("- Un número")
        print("- Un símbolo (!@#$%^&*()-_+=)")
        continue

    contraseña2 = input("Repita su contraseña: ")

    if contraseña1 == contraseña2:
        print("Gracias, bienvenido")
        valida = True
    else:
        print("Las contraseñas no coinciden. Intente nuevamente.")
