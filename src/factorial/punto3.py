from abc import ABC, abstractmethod

class EntregaFactory(ABC):
    def entrega(self):
        pass

class Entrega_mostrador(EntregaFactory):
    def entrega(self):
        print("La hamburguesa esta para retirarla por el mostrador")

class Entrega_cliente(EntregaFactory):
    def entrega(self):
        print("La hamburguesa esta siendo entregada al cliente")

class Entrega_delivery(EntregaFactory):
    def entrega(self):
        print("La hamburguesa esta en camino, será entregada por el delivery")

# Clase Hamburguesa que utiliza el Factory para la entrega
class Hamburguesa:
    def __init__(self, tipo_hamburguesa):
        self.tipo_hamburguesa = tipo_hamburguesa

    def entregar_hamburguesa(self, entrega_factory):
        entrega = entrega_factory.entregar()
        print(f"Hamburguesa {self.tipo_hamburguesa}: {entrega}")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una hamburguesa
    hamburguesa = Hamburguesa("Simple")

    # Entrega en mostrador
    entrega_mostrador = Entrega_mostrador()
    hamburguesa.entregar_hamburguesa(entrega_mostrador)

    # Entrega al cliente
    entrega_cliente = Entrega_cliente()
    hamburguesa.entregar_hamburguesa(entrega_cliente)

    # Entrega por delivery
    entrega_delivery = Entrega_delivery()
    hamburguesa.entregar_hamburguesa(entrega_delivery)