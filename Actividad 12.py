numero1 = input("Ingrese el primer número: ")
numero2 = input("Ingrese el segundo número: ")


num1 = int(numero1)
num2 = int(numero2)
numeros_primo={2, 3, 5, 7}

diferencia = num1 - num2

if diferencia % 2 == 0:
    print("Es divisible entre dos y suma es:", num1 + num2)
if diferencia < 10 and diferencia in numeros_primo:
    print("es primo y su producto es:", num1 * num2)
diferencia_string = str(diferencia)
if diferencia_string[-1] == '4':
      print("Termina en 4 y sus dígitos son:")
      for numero in diferencia_string:
        print(numero)

  



