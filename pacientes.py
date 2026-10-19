
def registrar_paciente(nombre, edad):
    paciente = {
        "nombre": nombre,
        "edad": edad
    }
    return paciente

paciente1 = registrar_paciente("Ana", 25)
print(paciente1)
