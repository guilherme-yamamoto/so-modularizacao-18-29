a = 0
b = 0

def maior_mult_menor():
    global a, b
    if(a < b):
        a, b = b, a
    if(a % b == 0):
        print(f"{a} é múltiplo de {b}.")
    elif(a % b != 0):
        print(f"{a} NÃO é múltiplo de {b}.")

def main():
    global a, b
    a = int(input("Insira o primeiro valor: "))
    b = int(input("Insira o segundo valor: "))
    maior_mult_menor()

if(__name__ == "__main__"):
    main()