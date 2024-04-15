# Genere una clase donde se instancie una comida rápida “hamburguesa”
# que pueda ser entregada en mostrador, retirada por el cliente o enviada por delivery.
# A los efectos prácticos bastará que la clase imprima el método de entrega.
class Hamburguesa:
    def __init__(self, tipo):
        """
        Inicializa una hamburguesa con un tipo específico.

        Args:
            tipo (str): El tipo de hamburguesa.
        """
        self.tipo = tipo

    def entrega(self):
        """
        Método abstracto para indicar cómo se entrega la hamburguesa.
        """
        pass


class EntregaMostrador(Hamburguesa):
    def entrega(self):
        """
        Imprime un mensaje indicando que la hamburguesa está lista para ser recogida en el mostrador.
        """
        print(
            f"La hamburguesa {self.tipo} está lista para ser recogida en el mostrador")


class EntregaCliente(Hamburguesa):
    def entrega(self):
        """
        Imprime un mensaje indicando que la hamburguesa fue retirada por el cliente.
        """
        print(
            f"La hamburguesa {self.tipo} fue retirada por el cliente")


class EntregaDelivery(Hamburguesa):
    def entrega(self):
        """
        Imprime un mensaje indicando que la hamburguesa será enviada por delivery.
        """
        print(f"La hamburguesa {self.tipo} será enviada por delivery")


class HamburguesaFactory:
    def obtener_entrega(self, tipo_entrega, tipo_hamburguesa):
        """
        Obtiene una instancia de entrega de hamburguesa según el tipo de entrega y tipo de hamburguesa especificados.

        Args:
            tipo_entrega (str): El tipo de entrega deseado ("mostrador", "cliente" o "delivery").
            tipo_hamburguesa (str): El tipo de hamburguesa deseado.

        Returns:
            Hamburguesa: Una instancia de la clase de entrega correspondiente.
        """
        if tipo_entrega == "mostrador":
            return EntregaMostrador(tipo_hamburguesa)
        elif tipo_entrega == "cliente":
            return EntregaCliente(tipo_hamburguesa)
        elif tipo_entrega == "delivery":
            return EntregaDelivery(tipo_hamburguesa)
        else:
            raise ValueError("Tipo de entrega no válido")


# Crea una instancia de la fábrica
factory = HamburguesaFactory()

# Hamburguesa para recoger en el mostrador
hamburguesa_mostrador = factory.obtener_entrega("mostrador", "Simple")
hamburguesa_mostrador.entrega()

# Hamburguesa para retirar por el cliente
hamburguesa_cliente = factory.obtener_entrega("cliente", "Bacon")
hamburguesa_cliente.entrega()

# Hamburguesa para delivery
hamburguesa_delivery = factory.obtener_entrega("delivery", "Completa")
hamburguesa_delivery.entrega()
