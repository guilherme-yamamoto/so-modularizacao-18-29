nota1 = 0
nota2 = 0
nota3 = 0
nota4 = 0

def calc_nota():
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print(f"As notas do bimestre foram {nota1}, {nota2}, {nota3} e {nota4}, e a média é {media}")
    if(media >= 6):
        print("APROVADO.")
    elif(media < 6 and media >= 3):
        print("EXAME.")
    elif(media < 3):
        print("RETIDO, se fudeu.")

def main():
    global nota1, nota2, nota3, nota4 
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))
    nota4 = float(input("Insira a quarta nota: "))
    calc_nota()

if(__name__ == "__main__"):
    main()