# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms
medidas_cliente = float(input("Por favor, ingresar las medidas de la pieza del mueble (en cms): "))

# Paso 2: Convertir las medidas de centímetros a pulgadas
medidas_pulgadas = medidas_cliente / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario 
print("Las medidas en pulgadas son: ", medidas_pulgadas)