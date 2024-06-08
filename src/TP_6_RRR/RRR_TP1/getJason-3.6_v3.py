"""
    Extractor de token para acceso API Servicios Banco XXX (versión 1.0)
    Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.
"""

import abc
import json
import sys
COPYRIGHT_MESSAGE = "copyright UADERFCyT-IS2©2024 todos los derechos reservados"
"""
Extractor de token para acceso API Servicios Banco XXX (versión 1.0)
(c) UADERFCyT-IS2©2024 todos los derechos reservados

Este programa permite extraer la clave de acceso API para utilizar los servicios del 
Banco XXX.

El programa operará como un microservicio invocado mediante:

    {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

    ej.
    ./getJason.pyc ./sitedata.json token1

El token podrá recuperarse mediante el standard output de ejecución en el formato

   {1.0}XXXX-XXXX-XXXX-XXXX

Para obtener un mensaje de ayuda detallado ejecutar

   ./getJason.pyc -h

Excepciones

Todas las condiciones de error del programa deben producir un mensaje de error bajo 
su control antes de terminar.
"""
VERSION = "versión 1.1"


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


class OriginalJSONLoader(JSONLoaderInterface):
    """
    Cargador de JSON que carga un archivo JSON cada vez que se instancia.
    Este cargador no implementa ningún patrón de diseño particular.
    """

    def __init__(self, jsonfile):
        """
        Inicializa el OriginalJSONLoader con el archivo JSON especificado.

        jsonfile: Ruta al archivo JSON.
        """
        self.jsonfile = jsonfile
        self.data = self.load_json()

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
        return: El valor asociado a la clave.
        """
        if key in self.data:
            return self.data[key]

        self.print_error(
            f"Error: La clave {key} no se encuentra en el sitedata")

    @staticmethod
    def print_error(message):
        """
        Imprime un mensaje de error y termina la ejecución del programa.

        message: El mensaje de error a imprimir.
        """
        print(message)
        sys.exit(1)


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


def message_help():
    """
    Muestra el mensaje de ayuda del programa.

    Este mensaje explica cómo utilizar el programa y sus opciones.
    """
    message = """
    Extractor de token para acceso API Servicios Banco XXX (versión 1.0)

    Este programa permite extraer la clave de acceso API para utilizar los servicios del 
    Banco XXX.

    El programa operará como un microservicio invocado mediante:

        {path ejecutable}/getJason.pyc {path archivo JSON}/{nombre archivo JSON}.json

        ej.
        ./getJason.pyc ./sitedata.json token1 o token2

    El token podrá recuperarse mediante el standard output de ejecución en el formato

       {1.0}XXXX-XXXX-XXXX-XXXX

    Para obtener un mensaje de ayuda detallado ejecutar

       ./getJason-3.6_v3.py -h
    
    para obtener la version ejecutar:
        ./getJason-3.6_v3.py -v

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
    if len(sys.argv) not in [3, 4]:
        if len(sys.argv) == 2 and sys.argv[1] == "-h":
            message_help()
        elif len(sys.argv) == 2 and sys.argv[1] == "-v":
            print(VERSION)
        else:
            print('Error: Número de argumentos no válido.')
            print('Use ./getJason.pyc -h para obtener ayuda.')
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    if not jsonfile.endswith('.json'):
        print(f"Error: El archivo {jsonfile} no es un archivo JSON.")
        sys.exit(1)

    if len(sys.argv) == 4:
        loader_type = sys.argv[3]
        if loader_type == 'original':
            json_loader = OriginalJSONLoader(jsonfile)
        elif loader_type == 'singleton':
            json_loader = SingletonJSONLoader(jsonfile)
        else:
            print(
                f"Error: Tipo de loader {loader_type} no válido. Use 'original' o 'singleton'.")
            sys.exit(1)
    else:
        # Default to OriginalJSONLoader
        json_loader = OriginalJSONLoader(jsonfile)

    value = json_loader.get_value(jsonkey)
    print(f"{1.0}{value}")


if __name__ == "__main__":
    main()
