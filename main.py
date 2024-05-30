Vocal= ("a", "e", "i", "o", "u")
nombre=input("¿Como te llamas? ")
i=0
while True:
 for vocal in nombre:
  if vocal in vocal:
   i=i+1


  if i>=3:
    print("Tu nombre tiene",i, "vocales")
    break
  else:
    print("Intentalo de nuevo")
    print("Tu nombre no tiene 3 o mas vocales")
    nombre=input("¿Como te llamas?")
    i=0