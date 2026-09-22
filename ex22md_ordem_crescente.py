a = 0
b = 0

def crescente():
    global a, b, VERDE
    if(a > b):
        a, b = b, a
        print(f"Os valores em ordem são: {a}, {b}.\n")
    elif(a == b):
        print("Os valores não podem ser iguais.\n")
    else:
        print(f"Os valores em ordem são: {a}, {b}.\n")

def main():
    global a, b
    a = int(input("Lembre-se: Os dois valores não podem ser iguais.\nInsira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))
    crescente()

if(__name__ == "__main__"):
    main()