# Represente la lista de piezas componentes de un ensamblado con sus relaciones jerárquicas.
# Empiece con un producto principal formado por tres sub-conjuntos los que a su vez tendrán cuatro piezas cada uno.
# Genere clases que representen esa configuración y la muestren.
# Luego agregue un subconjunto opcional adicional también formado por cuatro piezas. (Use el patrón composite).
from abc import ABC, abstractmethod


class Componente(ABC):
    @abstractmethod
    def mostrar(self, nivel):
        pass


class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel):
        print(" " * nivel + f"Pieza: {self.nombre}")


class Subconjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel):
        print(" " * nivel + f"Subconjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)


# Producto Principal
producto_principal = Subconjunto("Producto Principal")

# Subconjuntos internos
subconjunto_1 = Subconjunto("Subconjunto 1")
subconjunto_2 = Subconjunto("Subconjunto 2")
subconjunto_3 = Subconjunto("Subconjunto 3")

# Agregamos piezas a los subconjuntos

for i in range(4):
    subconjunto_1.agregar(Pieza(f"Pieza{i+1}"))
    subconjunto_2.agregar(Pieza(f"Pieza{i+5}"))
    subconjunto_3.agregar(Pieza(f"Pieza{i+9}"))

# Agregamos subconjuntos al productop principal

producto_principal.agregar(subconjunto_1)
producto_principal.agregar(subconjunto_2)
producto_principal.agregar(subconjunto_3)

# Mostrar la estructura del producto principal
producto_principal.mostrar(0)

# Agregar un subconjunto opcional adicional
subconjunto_opcional = Subconjunto("Subconjunto Opcional")
for i in range(4):
    subconjunto_opcional.agregar(Pieza(f"Pieza Opcional {i+1}"))

producto_principal.agregar(subconjunto_opcional)

print("\nEstructura del producto principal con subconjunto opcional: ")
producto_principal.mostrar(0)
