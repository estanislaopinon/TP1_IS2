# Extienda el ejemplo visto en el taller en clase de forma
# que se pueda utilizar para construir aviones en lugar de vehículos.
# Para simplificar suponga que un avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje.

import os
# *--------------------------------------------------------------------
# * La clase Director orquesta la construcción del objeto indicando
# * el orden en que deben llamarse sus componentes, los mismos son
# * genéricos y dependerán del builder específico utilizado sus
# * valores concretos
# *--------------------------------------------------------------------


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getPlane(self):
        plane = Plane()

        # Cuerpo del avion
        body = self.__builder.getBody()
        plane.setBody(body)

        # Construccion turbinas del avion (2)
        engine1, engine2 = self.__builder.getEngines()
        plane.setEngines(engine1, engine2)

        # Construccion de alas del avion(2):
        wing1, wing2 = self.__builder.getWings()
        plane.setWings(wing1, wing2)

        # Construccion del tren de aterrizaje del avion
        landing_gear = self.__builder.getLandingGear()
        plane.setLandingGear(landing_gear)

        # Retorna avion completo
        return plane

# *----------------------------------------------------------------
# * Esta es la definición de un objeto avion inicializando
# * todos sus atributos
# *----------------------------------------------------------------


class Plane:
    def __init__(self):
        self.__engines = []
        self.__wings = []
        self.__landing_gear = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def setEngines(self, engine1, engine2):
        self.__engines.append(engine1)
        self.__engines.append(engine2)

    def setWings(self, wing1, wing2):
        self.__wings.append(wing1)
        self.__wings.append(wing2)

    def setLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Cuerpo: %s" % (self.__body.shape))
        print("Turbinas: %d" % len(self.__engines))
        print("Alas: %d" % len(self.__wings))
        print("Tren de Aterrizaje: %s" % self.__landing_gear.type)

# *-----------------------------------------------------------------
# * Builder
# * Clase genérica que solo define la interfaz de los métodos que el
# * Builder específico tiene que implementar
# *-----------------------------------------------------------------


class Builder:

    def getBody(self): pass
    def getEngines(self): pass
    def getWings(self): pass
    def getLandingGear(self): pass


# *-----------------------------------------------------------------
# * Esta es la hoja de ruta para construir un Avión
# * Establece instancias para tomar turbinas(engines), alas, chasis y tren de aterrizaje
# * estableciendo las partes específicas que (en un Avion)
# * deben tener esas partes
# *-------------------------------------------------------

# Builder especifico para aviones
class PlaneBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "Aerodinamico"
        return body

    def getEngines(self):
        engine1 = Engine()
        engine2 = Engine()
        return engine1, engine2

    def getWings(self):
        wing1 = Wing()
        wing2 = Wing()
        return wing1, wing2

    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Convencional"
        return landing_gear


# *----------------------------------------------------------------
# * Define partes genéricas para un avion (sin inicializar)
# *----------------------------------------------------------------


class Engine:
    pass


class Wing:
    pass


class Body:
    pass


class LandingGear:
    pass

# *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
# * Esta es la estructura main()
# *=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=


def main():

    # *----------------------------------------------------------------
    # * Instancia la clase que será el resultado y la que guiará el
    # * proceso de construcción
    # *----------------------------------------------------------------
    plane_builder = PlaneBuilder()  # initializing the class
    director = Director()

# *----------------------------------------------------------------
# * Pasa al director la hoja de ruta para construir un avion
# *----------------------------------------------------------------
    director.setBuilder(plane_builder)

# *----------------------------------------------------------------
# * Ordena al director agregar los componentes de un avion según
# * la hoja de ruta
# *----------------------------------------------------------------
    plane = director.getPlane()

# *---------------------------------------------------------------
# * Finalizada la construcción verifica que sea completa
# *---------------------------------------------------------------
    plane.specification()
    print("\n\n")


# *----------------------------------------------------------------------
# * Se detecta el entry point y se lo deriva a una sección main() propia
# *----------------------------------------------------------------------
if __name__ == "__main__":
    os.system("cls  ")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avion\n")
    main()
