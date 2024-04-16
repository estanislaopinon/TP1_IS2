# Implemente una clase que permita a un número cualquiera imprimir su valor,
# luego agregarle sucesivamente.
# a. Sumarle 2.
# b. Multiplicarle por 2.
# c. Dividirlo por 3.
# Mostrar los resultados de la clase sin agregados y
# con la invocación anidada a las clases con las diferentes operaciones.
# Use un patrón decorator para implementar.

# Clase base para el número
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def imprimir(self):
        print(f"Valor actual: {self.valor}")

# Decorador base


class Decorador(Numero):
    def __init__(self, numero):
        self.numero = numero

    def imprimir(self):
        self.numero.imprimir()

# Decorador para sumar 2 al número


class SumarDosDecorator(Decorador):
    def imprimir(self):
        super().imprimir()
        print(
            f"Después de sumar 2: {self.numero.valor + 2 if hasattr(self.numero, 'valor') else 'No se puede realizar la operación'}")

# Decorador para multiplicar por 2 al número


class MultiplicarPorDosDecorator(Decorador):
    def imprimir(self):
        super().imprimir()
        print(f"Después de multiplicar por 2: {self.numero.valor * 2}")

# Decorador para dividir por 3 al número


class DividirPorTresDecorator(Decorador):
    def imprimir(self):
        super().imprimir()
        print(f"Después de dividir por 3: {self.numero.valor / 3}")


# Ejemplo de uso
numero = Numero(5)

print("Sin operaciones adicionales:")
numero.imprimir()

print("\nCon operaciones adicionales:")
numero_con_operaciones = DividirPorTresDecorator(
    MultiplicarPorDosDecorator(SumarDosDecorator(numero)))
numero_con_operaciones.imprimir()
