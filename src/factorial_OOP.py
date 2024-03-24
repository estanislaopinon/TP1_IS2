
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
class Factorial():
    def __init__(self, min, max):
        self.min= min
        self.max= max
        
    def calcular_factorial(self,num):
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
    
    def run(self):
        valores=[]#lista que almacena el numero y su respectivo factorial dentro del rango
        for i in range(self.min,self.max+1): #cicla por los valores dentro del rango
            j= self.calcular_factorial(i) #llama a la funcion factorial y guarda el valor
            if j is not None: #si j no esta vacio...
                print(f"El factorial de {i} es {j}")


    

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


factorizador= Factorial(inicio,fin)
factorizador.run()