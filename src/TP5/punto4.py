#Modifique el programa IS2_taller_scanner.py para que además
#la secuencia de barrido de radios que tiene incluya la sintonía
#de una serie de frecuencias memorizadas tanto de AM como de FM.
#Las frecuencias estarán etiquetadas como M1, M2, M3 y M4.
#Cada memoria podrá corresponder a una radio de AM o de FM en sus 
#respectivas frecuencias específicas. 
#En cada ciclo de barrido se barrerán las cuatro memorias. 

import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos=0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self,radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.memories = {"M1": "1250", "M2": "1380", "M3": "1510", "M4": None}  # Frecuencias memorizadas
        self.pos = 0
        self.name = "AM"
    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def scan(self):
        super().scan()
        self.check_memories()

    def check_memories(self):
        for key, value in self.memories.items():
            if value:
                print("Memoria {} sintonizada en {}".format(key, value))


class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.memories = {"M1": "81.3", "M2": "89.1", "M3": "103.9", "M4": None}  # Frecuencias memorizadas
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def scan(self):
        super().scan()
        self.check_memories()

    def check_memories(self):
        for key, value in self.memories.items():
            if value:
                print("Memoria {} sintonizada en {}".format(key, value))


class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
        print("")
        
        