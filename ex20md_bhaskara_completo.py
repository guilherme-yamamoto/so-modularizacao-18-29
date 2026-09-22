import math

A = 0
B = 0
C = 0

def bhaskara():
    delta = (B**2 - 4 * A * C)
    if(delta < 0):
        print(f"Delta vale {delta} e é menor que 0, portanto, não existe raiz real.")
    else:
        x1 = (-B + math.sqrt(delta)) / (2 * A)
        x2 = (-B - math.sqrt(delta)) / (2 * A)

    if(delta > 0):
        print(f"Delta vale {delta} e é maior que 0, portanto, existem duas raízes reais: {x1:.2f} e {x2:.2f}.")
    elif(delta == 0):
        print(f"Delta vale {delta}, portanto, existe apenas uma raiz real: {x1:.2f}.")

def main():
    global A, B, C
    A = int(input("Insira o coeficiente A: "))
    B = int(input("Insira o coeficiente B: "))
    C = int(input("Insira o coeficiente C: "))
    bhaskara()

if(__name__ == "__main__"):
    main()