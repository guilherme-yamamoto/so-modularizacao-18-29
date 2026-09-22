a = int(input("Insira o primeiro valor: "))
b = int(input("Insira o segundo valor: "))

def diferenca():
    global a, b
    if(a < b):
        a, b = b, a
    print(f"A diferença de {a} e {b} é {a - b}.")

def main():
    diferenca()

if(__name__ == "__main__"):
    main()