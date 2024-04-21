#Cree una clase bajo el patrón cadena de responsabilidad donde los números del 1 al 100 
#sean pasados a las clases subscriptas en secuencia, 
#aquella que identifique la necesidad de consumir el número lo hará y caso contrario 
#lo pasará al siguiente en la cadena. Implemente una clase que consuma números primos y otra números pares. 
#Puede ocurrir que un número no sea consumido por ninguna clase en cuyo caso se marcará como no consumido. 

class Handler:
    """
    Clase base para implementar el patron Cadena de Responabilidad
    """
    def __init__(self,successor=None):
        self._successor= successor
    
    def handle_request(self, number):
        """
        Metodo para manejar una solicitud.Si el manejador actual no puede manejarla
        se la pasa al siguiente en la cadena
        """
        if self._successor:
            return self._successor.handle_request(number)
        return (f"Numero {number} no consumido")
    
class PrimeHandler(Handler):
    """
    Clase para manejar numeros primos en la cadena de responsabilidad
    """
    def handle_request(self, number):
        """
        Maneja un numero primo, de lo contrario, lo pasa al 
        siguiente manejador
        """
        if self.is_prime(number):
            print(f"Prime Handler consumed {number}")
        else:
            return super().handle_request(number)

    def is_prime(self,n):
        """
        Vereifica si es primo
        """
        if n<=1:
            return False
        if n<=3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i=5
        while i * i <=n:
            if n % i == 0 or n % (i+2) == 0:
                return False
            i+=6
        return True
    
class EvenHandler(Handler):
    """
    Clase para manejar nueros pares en la cadena
    """
    def handle_request(self, number):
        """
        Maneja un numero si es par,
        de lo contrario lo pasa al siguiente manejador"""
        if number % 2 == 0:
            print(f"Even Handler consumed {number}")
        else:
            return super().handle_request(number)
    
class NumberProcessor:
    """
    Clase para procesar los numeros
    """
    def __init__(self):
        self.handler_chain= EvenHandler(PrimeHandler())
    
    def process_numbers(self):
        """
        Procesa del 1 al 100 pasandolo a traves de la cadena de responsabilidad
        """
        for i in range(1,101):
            self.handler_chain.handle_request(i)


processor= NumberProcessor()
processor.process_numbers()
            
