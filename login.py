
def iniciar_sesion(usuario, contrasena):
    if usuario == "admin" and contrasena == "1234":
        return "Inicio de sesión exitoso"
    else:
        return "Usuario o contraseña incorrectos"

print(iniciar_sesion("admin", "1234"))
