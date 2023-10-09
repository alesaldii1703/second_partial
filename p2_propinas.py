#https://replit.com/join/fxaitpjtog-alejandrasaldiv
'''
Calculadora de Propinas con Excepciones:
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
