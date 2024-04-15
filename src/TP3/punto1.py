# Importamos la metaclase SingltonMeta desde el modulo singleton
from singleton import SingletonMeta

# Definimos nuestra clase SingletonFactorial y se le asigna la metaclase SingletonMeta


class SingletonFactorial(metaclass=SingletonMeta):

    # calcula el factorial de un numero
    def factorial(self, num):
        if num < 0:  # controla si el numero es negativo
            print("Factorial de un número negativo no existe")
        elif num == 0:  # Si num no contiene un valor, retorna 1
            return 1
        else:
            fact = 1
            while (num > 1):  # bucle que realiza el factorial de num
                fact *= num
                num -= 1
            return fact  # retorna el factorial


if __name__ == '__main__':
    # cCreamos dos instancias SingletonFactorial
    s1 = SingletonFactorial()
    s2 = SingletonFactorial()
    # Solicitamos al usuario un numero
    num = int(input('Ingrese un numero: '))
    print(f'El factorial de es: {s1.factorial(num)}')
    # Comparamos si s1 y s2 son la misma instancia
    if s1 == s2:
        print('True')
