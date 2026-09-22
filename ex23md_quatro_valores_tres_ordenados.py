n1 = 0
n2 = 0
n3 = 0
n4 = 0

def organizador():
    if(n4 >= n3):
        print(f"A ordem dos valores são: {n1}, {n2}, {n3}, {n4}")
    elif(n4 >= n2 and n4 < n3):
        print(f"A ordem dos valores são: {n1}, {n2}, {n4}, {n3}")
    elif(n4 >= n1 and n4 < n2):
        print(f"A ordem dos valores são: {n1}, {n4}, {n2}, {n3}")
    else:
        print(f"A ordem dos valores são: {n4}, {n1}, {n2}, {n3}")


def main():
    global n1, n2, n3, n4
    n1 = float(input("Insira os três primeiros valores em ordem crescente, o quarto é opcional.\nInsira o primeiro valor: "))
    n2 = float(input("Insira o segundo valor: "))
    while(n2 < n1):
        n2 = float(input(f"O valor precisa ser maior que o anterior ({n1}): "))
    n3 = float(input("Insira o terceiro valor: "))
    while(n3 < n2):
        n3 = float(input(f"O valor precisa ser maior que o anterior ({n2}): "))
    n4 = float(input("Insira o quarto valor: "))

    organizador()

if(__name__ == "__main__"):
    main()