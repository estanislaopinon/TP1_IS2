# Extractor de Token para Acceso API Servicios Banco "xxx"

## Descripción
Este programa se encarga de extraer el token necesario para acceder a los servicios API del banco "xxx". El programa busca dentro de un archivo JSON (`sitedata_v4.json`) el valor asociado a una clave específica y realiza un pedido de pago de $500 desde la cuenta con el mayor balance.

## Archivos del Proyecto

- **getJason-3.6_v4.py**: Script principal que realiza la extracción del token y el pedido de pago.
- **README_v4.md**: Archivo de documentación del proyecto.
- **COMPILE.sh**: Script para compilar los archivos.
- **sitedata_v4.json**: Archivo JSON que contiene dos tokens (`token1` y `token2`) y sus valores.

## Uso

Para ejecutar el programa, usa el siguiente comando en la terminal:
"python ./getJason-3.6_v4.py ./sitedata_v4.json (token1 o token2)"

## Argumentos
- **sitedata_v4.json**: Archivo JSON que contiene las cuentas y sus balances.

## Ejemplo
python getJason-ri.py sitedata.json

Este comando procesará el archivo sitedata.json, buscará la cuenta con el mayor balance y descontará $500 de dicha cuenta. El resultado será impreso en la terminal.

## Manejo de Errores
    -Si no se proporciona un archivo JSON como argumento, el programa mostrará un mensaje de error y terminará la ejecución.
    -Si el archivo proporcionado no tiene la extensión .json, el programa mostrará un mensaje de error y terminará la ejecución.
    -Si el archivo JSON no existe, el programa mostrará un mensaje de error y terminará la ejecución.

## Versión
Este programa está en la versión 1.2. Para mostrar dicha versión, ejecutar el siguiente comando:
"python ./getJason-3.6_v4.py -v"