#Primer proyecto de Python

carlos = "Carlos"
print(carlos)
print("Hola, " + carlos + "! ¿Cómo estás?")

# Imprimir un mensaje de bienvenida
print("¡Bienvenido al mundo de Python, " + carlos + "!")

# Desarrollar un programa que imprima un mensaje personalizado
def mensaje_personalizado(nombre):
    print("¡Hola, " + nombre + "! Bienvenido a tu primer programa en Python.")
# Llamar a la función con el nombre "Carlos"
mensaje_personalizado(carlos)
# Desarrollar un programa que imprima un mensaje de despedida
def despedida(nombre):
    print("¡Hasta luego, " + nombre + "! Espero que hayas disfrutado de tu primer programa en Python.")
# Llamar a la función con el nombre "Carlos"
despedida(carlos)