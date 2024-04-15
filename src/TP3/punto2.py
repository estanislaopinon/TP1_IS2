# Importamos Singletonmeta desde el modulo singleton
from singleton import SingletonMeta


class Singleton_Calculadora(metaclass=SingletonMeta):
    # Metodo para calcular la suma total de impuestos
    def Calculadora(self, base):
        # Calculamos IVA, impuesto a los ingresos brutos (IIBB)
        # y las contribucines municipales
        iva = base*0.21
        iibb = base*0.05
        contrib_municipales = base*0.012
        # calculamos el total de impuestos
        total = iva+iibb+contrib_municipales
        return total


if __name__ == '__main__':
    # Creamos dos instancias Songletton_Calculadora
    s1 = Singleton_Calculadora()
    s2 = Singleton_Calculadora()
    # Definimos base sobre la cual calculamos los impuestos
    base = 120
    # Mostramos la suma total de los impuestos
    print(f'la suma del total de los impuestos es: {s1.Calculadora(base)}')
