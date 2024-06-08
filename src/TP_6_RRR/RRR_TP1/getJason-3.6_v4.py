"""
    Extractor de token para acceso API Servicios Banco XXX (versión 1.2)
    Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.
"""

import abc
import json
import sys
from collections import deque

COPYRIGHT_MESSAGE = "copyright UADERFCyT-IS2©2024 todos los derechos reservados"
VERSION = "versión 1.2"


class JSONLoaderInterface(abc.ABC):
    """
    Interfaz abstracta para cargadores de JSON.
    Define los métodos básicos que deben implementar los cargadores de JSON.
    """
    @abc.abstractmethod
    def load_json(self):
        """
        Carga el archivo JSON.
        Este método debe ser implementado por cualquier clase que herede de JSONLoaderInterface.
        """

    @abc.abstractmethod
    def get_value(self, key):
        """
        Obtiene el valor asociado a una clave específica en el JSON.
        :param key: La clave para buscar en el JSON.
        :return: El valor asociado a la clave.
        """


class SingletonJSONLoader(JSONLoaderInterface):
    """
    Cargador de JSON que sigue el patrón de diseño Singleton.
    Asegura que solo exista una instancia del cargador en toda la aplicación.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Crea una nueva instancia del SingletonJSONLoader si no existe.
        :return: La única instancia del SingletonJSONLoader.
        """
        if cls._instance is None:
            cls._instance = super(SingletonJSONLoader, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, jsonfile):
        """
        Inicializa el SingletonJSONLoader con el archivo JSON especificado.
        :param jsonfile: Ruta al archivo JSON.
        """
        if not self._initialized:
            self.jsonfile = jsonfile
            self.data = self.load_json()
            self._initialized = True

    def load_json(self):
        """
        Carga y devuelve los datos del archivo JSON.
        :return: Los datos del JSON como un diccionario.
        """
        try:
            with open(self.jsonfile, 'r') as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            self.print_error(f"Error: el archivo {self.jsonfile} no existe")
        except json.JSONDecodeError:
            self.print_error(
                f"Error: el archivo {self.jsonfile} no contiene un JSON válido")
        except Exception as e:
            self.print_error(f"Error no esperado: {e}")

    def get_value(self, key):
        """
        Obtiene el valor asociado a una clave específica en el JSON.
        :key: La clave para buscar en el JSON.
        :return: El valor asociado a la clave.
        """
        if key in self.data:
            return self.data[key]
        self.print_error(
            f"Error: La clave {key} no se encuentra en el sitedata")

    @staticmethod
    def print_error(message):
        """
        Imprime un mensaje de error y termina la ejecución del programa.
        :param message: El mensaje de error a imprimir.
        """
        print(message)
        sys.exit(1)


class PaymentHandler:
    """
    Clase que maneja los pagos utilizando el patrón de diseño "Cadena de responsabilidad".
    """

    def __init__(self, balances):
        self.balances = balances
        self.payments = deque()
        self.current_index = 0

    def handle_payment(self, order_number, amount):
        """
        Maneja un pago seleccionando la cuenta automáticamente.
        :param order_number: Número de pedido.
        :param amount: Monto del pago.
        """
        banks = list(self.balances.keys())
        for _ in range(len(banks)):
            bank = banks[self.current_index]
            if self.balances[bank] >= amount:
                self.balances[bank] -= amount
                self.payments.append((order_number, bank, amount))
                self.current_index = (self.current_index + 1) % len(banks)
                return f"Pago realizado: Pedido {order_number}, Token {bank}, Monto ${amount}"
            self.current_index = (self.current_index + 1) % len(banks)
        return f"Error: No hay suficiente saldo para el pedido {order_number}"

    def list_payments(self):
        """
        Lista todos los pagos realizados en orden cronológico.
        """
        return list(self.payments)


def message_help():
    """
    Muestra el mensaje de ayuda del programa.
    Este mensaje explica cómo utilizar el programa y sus opciones.
    """
    message = """
    Extractor de token para acceso API Servicios Banco XXX (versión 1.2)

    Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.

    El programa operará como un microservicio invocado mediante:

        {path ejecutable}/getJason-3.6_v4.py {path archivo JSON}/{nombre archivo JSON}.json

        ej.
        ./getJason-3.6_v4.py ./sitedata_v4.json token1 o token2

    El token podrá recuperarse mediante el standard output de ejecución en el formato

       {1.0}XXXX-XXXX-XXXX-XXXX

    Para obtener un mensaje de ayuda detallado ejecutar

       ./getJason-3.6_v4.py -h
    
    para obtener la version ejecutar:
        ./getJason-3.6_v4.py -v

    Excepciones

    Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
    terminar.
    """
    print(message)


def main():
    """
    Función principal del programa.
    Esta función maneja la lógica principal de ejecución, incluyendo la validación de argumentos,
    carga del archivo JSON y recuperación del valor solicitado.
    """
    print(COPYRIGHT_MESSAGE)
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            message_help()
            sys.exit(0)
        elif sys.argv[1] == "-v":
            print(VERSION)
            sys.exit(0)
        else:
            jsonfile = 'sitedata_v4.json'  # Default file
            jsonkey = sys.argv[1]
    elif len(sys.argv) == 3:
        jsonfile = sys.argv[1]
        jsonkey = sys.argv[2]
    else:
        print('Error: Número de argumentos no válido.')
        print('Use ./getJason-3.6_v4.py -h para obtener ayuda.')
        sys.exit(1)

    if not jsonfile.endswith('.json'):
        print(f"Error: El archivo {jsonfile} no es un archivo JSON.")
        sys.exit(1)

    json_loader = SingletonJSONLoader(jsonfile)
    value = json_loader.get_value(jsonkey)
    print(f"{1.0}{value}")

    balances = {"token1": 1000, "token2": 2000}
    payment_handler = PaymentHandler(balances)

    # Ejemplo de pedidos de pago
    print(payment_handler.handle_payment(1, 500))
    print(payment_handler.handle_payment(2, 500))
    print(payment_handler.handle_payment(3, 500))
    print(payment_handler.handle_payment(4, 500))

    # Listar todos los pagos realizados
    for payment in payment_handler.list_payments():
        print(payment)


if __name__ == "__main__":
    main()
