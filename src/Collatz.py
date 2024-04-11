import matplotlib.pyplot as plt


def iteracion_collatz(num):
    cont_iteraciones = 0
    while num != 1:
        if num % 2 == 0:
            num = num//2
        else:
            num = num*3+1

        cont_iteraciones += 1
    return cont_iteraciones


num = range(1, 10001)

iteraciones_valores = [iteracion_collatz(n)for n in num]

plt.figure(figsize=(10, 6))
plt.scatter(iteraciones_valores, num, marker=".", color="blue")
plt.title("Secuencia de Collatz")
plt.xlabel("Número de iteraciones")
plt.ylabel("Número inicial (n)")
plt.grid(True)
plt.show()
