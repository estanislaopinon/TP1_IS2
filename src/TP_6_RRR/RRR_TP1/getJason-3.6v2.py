import json
import sys


def help():
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

       ./getJason.pyc -h

    Excepciones

    Todas las condiciones de error del programa deben producir un mensaje de error bajo su control antes de
    terminar.

    """
    print(message)


class JSONLoaderSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(JSONLoaderSingleton, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, jsonfile):
        if not self._initialized:
            self.jsonfile = jsonfile
            self.data = self.load_json()
            self._initialized = True

    def load_json(self):
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
        if key in self.data:
            return self.data[key]
        else:
            self.print_error(
                f"Error: La clave {key} no se encuentra en el sitedata")

    @staticmethod
    def print_error(message):
        print(message)
        sys.exit(1)


def main():
    if len(sys.argv) != 3:
        if len(sys.argv) == 2 and sys.argv[1] == "-h":
            help()
        else:
            print('Error: Número de argumentos no válido.')
            print('Use ./getJason.pyc -h para obtener ayuda.')
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    if not jsonfile.endswith('.json'):
        print(f"Error: El archivo {jsonfile} no es un archivo JSON.")
        sys.exit(1)

    json_loader = JSONLoaderSingleton(jsonfile)
    value = json_loader.get_value(jsonkey)
    print(f"{1.0}{value}")


if __name__ == "__main__":
    main()
