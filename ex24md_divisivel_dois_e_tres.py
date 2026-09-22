a = 0

def dois_tres():

    if(a % 2 == 0 and a % 3 == 0 and a != 0):
        print(f"O número {a} é divisível por 2 e por 3.")
    elif(a % 2 == 0 and a % 3 != 0):
        print(f"O número {a} é divisível por 2, mas não por 3.")
    elif(a % 2 != 0 and a % 3 == 0):
        print(f"O número {a} não é divisível por 2, mas é divisível por 3.")
    else:
        print(f"O número {a} não é divisível nem por 2, nem por 3.")


def main():
    global a
    a = int(input("Insira um número inteiro: "))
    dois_tres()

if(__name__ == "__main__"):
    main()