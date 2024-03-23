
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def rango_factorial(inicio,fin):
    valores=[]
    for i in range(inicio,fin+1):
        j= factorial(i)
        if j is not None:
            valores.append((i,j))

    return valores

if len(sys.argv) == 1:
    
    while True:
        try:
            n=input("Ingrese un rango desde-hasta que quiera evaluar: ")
            if n.startswith("-"):
                inicio=1
                fin=int(n.split("-")[1])
                break
            elif n.endswith("-"):
                inicio= int(n.split("-")[0])
                fin=60
                break
            elif "-" in n:
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

