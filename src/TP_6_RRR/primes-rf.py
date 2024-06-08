#!/usr/bin/python3
# Python program to display all the prime numbers within an interval
# copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados
import sys
import os
#*---------------------------
#*--- Nueva clase primes
#*---------------------------
class ClassPrimes:

	def compute(self,numero_maximo):

		n=numero_maximo
		if n>1:
			for i in range(2,n):
				if (n % i) == 0:
					return False
				else:
					continue
			#else:
			return True
		else:
			return False
#*------------------------------------------------------
#* Clase de abstracción
#*------------------------------------------------------
class BranchByAbstract:
	def AbstractLayer(self,u):

		nc=ClassPrimes()
		nprimo=u
		print("La verificación de número primo para (%d) da (%s)" % (nprimo,nc.compute(nprimo)))



#*------------------------------------------------------
#*------- Main del programa
#*------------------------------------------------------

os.system("clear")

print("Programa %s copyright UADER_FCyT_IS2 © 2022,2024 todos los derechos reservados" % (sys.argv[0]))

#*--- Extrae el número máximo a calcular desde los argumentos

upper=int(sys.argv[1])

#*---- Crea la clase de abstracción

s1=BranchByAbstract()

#*--- Ejecuta la verificación

s1.AbstractLayer(upper)
