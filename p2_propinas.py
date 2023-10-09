#https://replit.com/join/fxaitpjtog-alejandrasaldiv
'''
Calculadora de Propinas con Excepciones:
p2_propinas.py

Crea un programa que solicite al usuario el costo de una comida en un restaurante y el servicio recibido (bueno, regular o malo). Si el servicio es "malo", no aplica propina. Si el servicio es "regular", aplica una propina del 10%. Si el servicio es "bueno", aplica una propina del 15%. Además, maneja excepciones para asegurarte de que el usuario ingrese un servicio válido.
1- Pedirle al usuario el costo de la comida CHECK
2- Pedirle al usuario si el servicio fue bueno, regular o malo. CHECK
3- Hacer mi condicional (malo=0%,regular=10%,bueno=15%) CHECK
4- Hacer la operación del propinas
5- Desplegar el resultado
'''
#Paso 1 y 2
costo_comida = float(input("Dame el costo de la comida."))
calidad_servicio = input("Ingresa si el servicio fue bueno, malo o regular.")
#Paso 3
if calidad_servicio == "malo":
  propina = 0
  #Paso 4 y 5
  costo_propina = costo_comida*(propina/100) 
  costo_total = costo_comida+costo_propina
  print("El costo total es de: ",costo_total)
elif calidad_servicio == "bueno":
  propina = 15
  #Paso 4 y 5
  costo_propina = costo_comida*(propina/100) 
  costo_total = costo_comida+costo_propina
  print("El costo total es de: ",costo_total)
elif calidad_servicio == "regular":
  propina = 10
  #Paso 4 y 5
  costo_propina = costo_comida*(propina/100) 
  costo_total = costo_comida+costo_propina
  print("El costo total es de: ",costo_total)
else:
  print("Lo siento, esa opción no es válida. Por favor escribe bueno, malo o regular.")
