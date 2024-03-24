
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): #funcion para sacar el factorial de un numero
    if num < 0: #control que evita sacar el factorial de un numero negativo
        print("Factorial de un número negativo no existe")

    elif num == 0: #Si num no contiene un valor, retorna 1
        return 1
        
    else: 
        fact = 1
        while(num > 1): #bucle que realiza el factorial de num
            fact *= num 
            num -= 1
        return fact #retorna el factorial 

def rango_factorial(inicio,fin): # funcion que realiza el factorial del rango de numeros asignados
    valores=[]#lista que almacena el numero y su respectivo factorial dentro del rango
    for i in range(inicio,fin+1): #cicla por los valores dentro del rango
        j= factorial(i)#llama a la funcion factorial y guarda el valor
        if j is not None: #si j no esta vacio...
            valores.append((i,j))#se lo añade a la lista

    return valores

if len(sys.argv) == 1:# verifica si se proporciona un argumento en la linea de comando
    
    while True:#mientras el if sea verdadero
        try:
            n=input("Ingrese un rango desde-hasta que quiera evaluar: ")
            if n.startswith("-"):#caso -hasta
                inicio=1
                fin=int(n.split("-")[1])
                break
            elif n.endswith("-"):#caso desde-
                inicio= int(n.split("-")[0])
                fin=60
                break
            elif "-" in n:#caso desde-hasta
                inicio, fin= map(int,n.split("-"))
                break
            else:
                raise ValueError 

        
        except ValueError: 
            print("Debe ingresar un rango valido")

factorial=rango_factorial(inicio,fin)
if factorial:
    for i,j in factorial:
        print(f"El factorial de {i} es {j}")
else:
    print("No se han encontrado factoriales en el rango especificado")

