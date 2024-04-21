#Implemente una clase bajo el patrón observer donde una serie de clases están subscriptas,
#cada clase espera que su propio ID (una secuencia arbitraria de 4 caracteres) 
#sea expuesta y emitirá un mensaje cuando el ID emitido y el propio coinciden. 
#Implemente 4 clases de tal manera que cada una tenga un ID especifico. 
#Emita 8 ID asegurándose que al menos cuatro de ellos coincidan con ID 
#para el que tenga una clase implementada. 
class Observer:
    """
    Clase base para el patrón Observer
    """
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        metodo para subscribir un observador
        """ 
        self._observers.append(observer)
    
    def notify(self, event):
        """
        metodo para notificar a todos los observadores
        """
        for observer in self._observers:
            observer.update(event)

class ConcreteObserver(Observer):
    """
    Clase concreta para los observadores
    """
    def __init__(self,observer_id):
        super().__init__()
        self._observer_id= observer_id
    
    def update(self, event):
        """
        metodo para manejar el evento
        """
        if self._observer_id== event:
            print(f"Observer with ID {self._observer_id} received the event: {event}")
    
if __name__ == "__main__":
    # Creamos las instancias de las clases observadoras
    observer1 = ConcreteObserver("ABCD")
    observer2 = ConcreteObserver("EFGH")
    observer3 = ConcreteObserver("WXYZ")
    observer4 = ConcreteObserver("1234")

    # Creamos una instancia del sujeto (el que emite eventos)
    subject = Observer()

    # Suscribimos las clases observadoras al sujeto
    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)
    subject.attach(observer4)

    # Emitimos eventos
    events = ["1234", "ABCD", "WXYZ", "EFGH", "5678", "9012", "3456", "EFGH"]

    # Notificamos a los observadores sobre los eventos
    for event in events:
        subject.notify(event)