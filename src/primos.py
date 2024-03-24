
# Python program to display all the prime numbers within an interval
# Se establecen limites del intervalo
lower = 1
upper = 100
# Muestra el mensaje indicando el intervalo
print("Prime numbers between", lower, "and", upper, "are:")

#Itera a traves de todos los numeros en el intervalo
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       #Verifica si el numero es primo
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           #Si el numero no tiene divisiores excepto 1 y si mismo, lo imprime como primo
           print(num)

