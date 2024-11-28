print("##########################\n")
print("##  Bienvenido jugador  ##\n")
print("##########################\n")

print("#############################\n")
print("1. Empeazar a jugar \n ")
print("2. Salir\n ")
print("#############################\n")
in1 = int(input("Elije un numero: "))
if in1 == 1: 
  nombre = input("Cual es tu nombre jugador ? ") 
  edad = input("Cual es tu edad?\n")
  comida = input("Dime cual es tu comida favorita?\n")
                 
  print("Bienvenido {}\n".format(nombre))
    
  print("Ves tres puertas, en una de ellas pone {}, tu nombre\n".format(nombre))
  print("En la segunda pone {}, es tu edad \n".format(edad))
  print("En la tercer pone, no pone nada, solo el numero 3 ")
  
  puerta1 = int(input("¿Que puerta quieres entrar por?"))
  if puerta1 == 1:
      print("Te encuentras un cartel donde no pone nada, solo dice: {}\n".format(nombre))
  elif puerta1 == 2:
      print("Tras esta puerta te encuenteras {}, tu comida favorita y encima hay {} velas, una por cada año".format(comida,edad))
  elif puerta1 == 3: 
      print("No te encuentras nada, que te esperas ? No habia nada en la puerta para empezar")
  else:
      print("Eso no es un numero valido alcornoque")
elif in1 == 2: 
  print("Adios")

else: 
  print("No es un numero valido")
