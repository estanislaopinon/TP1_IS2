# Para un producto láminas de acero de 0.5” de espesor y
# 1,5 metros de ancho dispone de dos trenes laminadores,
# uno que genera planchas de 5 mts y otro de 10 mts.
# Genere una clase que represente a las láminas en forma genérica al cual se le pueda indicar
# que a que tren laminador se enviará a producir. (Use el patrón bridge en la solución).
from abc import ABC, abstractmethod


class Lamina(ABC):
    def __init__(self, espesor, ancho) -> None:
        self.espesor = espesor
        self.ancho = ancho

    def producir(self):
        pass


class Lamina5Metros(Lamina):
    def producir(self):
        print(
            f"Lamina de {self.espesor} pulgadas de espesor y {self.ancho} metros de ancho producida en el tren de 5 metros.")


class Lamina10Metros(Lamina):
    def producir(self):
        print(
            f"Lamina de {self.espesor} pulgadas de espesor y {self.ancho} metros de ancho producida en el tren de 10 metros.")


class FabricaLaminas:
    def __init__(self, lamina):
        self.lamina = lamina

    def enviar_a_producir(self):
        self.lamina.producir()


lamina_5m = Lamina5Metros(0.5, 1.5)
lamina_10m = Lamina10Metros(0.5, 1.5)

fabrica_lamina_5m = FabricaLaminas(lamina_5m)
fabrica_lamina_5m.enviar_a_producir()

fabrica_lamina_10m = FabricaLaminas(lamina_10m)
fabrica_lamina_10m.enviar_a_producir()
