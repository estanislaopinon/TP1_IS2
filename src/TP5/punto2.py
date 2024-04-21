#Implemente una clase bajo el patrón iterator que almacene una cadena de caracteres 
#y permita recorrerla en sentido directo y reverso. 

from _collections_abc import Iterable, Iterator
from typing import Any, List

class WordsCollection(Iterable):
    """
    Clase que implementa la interfaz Iterable para permitir
    la iteracion sobre la colección
    """
    def __init__(self, collection: List[Any]= []) -> None:
        self._collection = collection
    
    def __iter__(self) -> 'Alphabetica10rderIterator':
        """
        Retorna un iterador para recorrer la coleccion en orden ascendente
        """
        return Alphabetica10rderIterator(self._collection)
    
    def get_reverse_iterator(self) -> 'Alphabetica10rderIterator':
       """
       Retorna uniterador para recorrer la coleccion de forma descendente
       """
       return Alphabetica10rderIterator(self._collection, True)
    
    def add_item(self, item: Any):
        self._collection.append(item)

class Alphabetica10rderIterator(Iterator):
    """
    Clase que representa un iterador para recorrer
    una colección de palabras alfabeticamente
    """
    _position: int = 0

    _reverse: bool = False

    def __init__(self,collection: WordsCollection, reverse:bool = False) -> None:
        self._colelection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0
    
    def __next__(self):
        try:
            value = self._colelection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        
        return value
    


if __name__=="__main__":
    #Cargo las palabras a la colección
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")
    #itera sobre la colección en orden ascendente
    print("Straight traversal:")
    for item in collection:
        print(item)
    print("")

    #itera sobre la colección en orden descendente
    print("Reverse traversal:")
    for item in collection.get_reverse_iterator():
        print(item)
