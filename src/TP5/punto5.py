# Modifique el programa IS2_taller_memory.py para que la clase tenga la
# capacidad de almacenar hasta 4 estados en el pasado y pueda recuperar los
# mismos en cualquier orden de ser necesario.
# El método undo deberá tener un argumento adicional
# indicando si se desea recuperar el inmediato anterior (0) y los anteriores a el (1,2,3).

import os


class Memento:
    """
    Clase que representa un memento para almacenar el estado de FIleWriterUtility
    """

    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    """
    Clase que proporciona utilidades para escribir en un archivo y gestionar sus estados anteriores.
    """

    def __init__(self, file):
        self.file = file
        self.content = ""
        self.mementos = []

    def write(self, string):
        """
        Añade una cadena al contenido del archivo.
        """
        self.content += string

    def save(self):
        """
        Guarda el estado actual del archivo en un memento y lo agrega a la lista de mementos.
        Si hay más de 4 mementos, elimina el más antiguo.
        """
        memento = Memento(self.file, self.content)
        self.mementos.append(memento)
        if len(self.mementos) > 4:
            del self.mementos[0]

    def undo(self, count=1):
        """
        Deshace la última acción realizada en el archivo, restaurando un estado anterior guardado en un memento.
        Puede deshacer múltiples acciones especificadas por count.
        """
        for _ in range(count):
            if self.mementos:
                memento = self.mementos.pop()
                self.file = memento.file
                self.content = memento.content


class FileWriterCaretaker:
    """
    Clase que actúa como un administrador para FileWriterUtility, permitiendo guardar y deshacer estados.
    """

    def save(self, writer):
        """
        Solicita al escritor que guarde su estado actual.
        """
        writer.save()

    def undo(self, writer, count=1):
        """
        Solicita al escritor que deshaga una o más acciones.
        """
        writer.undo(count)


if __name__ == '__main__':
    os.system("cls")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se invoca al <undo> para recuperar el estado inmediatamente anterior")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar los últimos 3 estados")
    caretaker.undo(writer, count=3)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar el estado inmediatamente anterior")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca al <undo> para recuperar el estado inmediatamente anterior")
    caretaker.undo(writer)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
