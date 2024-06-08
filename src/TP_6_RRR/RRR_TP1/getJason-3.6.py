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


def main():
    if len(sys.argv) != 3:
        if len(sys.argv) == 2 and sys.argv[1] == "-h":
            help()
        else:
            print('Error. Numero de argumentos no valido.')
            print('Use ./getJason-3.6.py -h para obtener ayuda.')
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()

        obj = json.loads(data)
        if jsonkey in obj:
            print(f"{1.0}{obj[jsonkey]}")
        else:
            print(f"Error: La clave {jsonkey} no se encuentra en el sitedata")
            sys.exit(1)
    except FileNotFoundError:
        print(f"Error: el archivo no existe")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: el archivo {jsonfile} no contiene un JSON valido")
        sys.exit(1)
    except Exception as e:
        print(f"Error no esperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
