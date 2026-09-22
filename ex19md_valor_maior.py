a = float(input("Insira o primeiro valor: "))
b = float(input("Insira o segundo valor: "))

def maior():
    global a, b
    if(a > b):
        print(f"Entre {a} e {b}, {a} é o maior valor.")
    elif(b > a):
        print(f"Entre {a} e {b}, {b} é o maior valor.")
    else:
        print(f"Ambos os valores são iguais. Valem {a}")

def main():
    maior()

if(__name__ == "__main__"):
    main()