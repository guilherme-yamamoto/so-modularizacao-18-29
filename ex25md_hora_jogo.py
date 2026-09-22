hora_inicial = 0
minuto_inicial = 0
hora_final = 0
minuto_final = 0

def tempo_jogo():
    if(hora_final >= hora_inicial):
        hora = hora_final - hora_inicial
    elif(hora_final < hora_inicial):
        hora = 24 - hora_inicial + hora_final

    if(minuto_final >= minuto_inicial):
        minuto = minuto_final - minuto_inicial
    elif(minuto_final < minuto_inicial):
        minuto = 60 - minuto_inicial + minuto_final
        hora = hora - 1

    print(f"O jogo vai durar {hora} hora(s) e {minuto} minuto(s).")

def main():
    global hora_inicial, minuto_inicial, hora_final, minuto_final
    hora_inicial = int(input("Insira a hora inicial do jogo: "))
    hora_final = int(input("Insira a hora final do jogo: "))
    minuto_inicial = int(input("Insira o minuto inicial do jogo: "))
    minuto_final = int(input("Insira o minuto final do jogo: "))

    while(hora_final > 24 or hora_inicial > 24 or minuto_final > 60 or minuto_inicial > 60):
        hora_inicial = int(input("\nO valor inserido é inválido, tente novamente.\nInsira a hora inicial do jogo: "))
        hora_final = int(input("Insira a hora final do jogo: "))
        minuto_inicial = int(input("Insira o minuto inicial do jogo: "))
        minuto_final = int(input("Insira o minuto final do jogo: "))
            
    tempo_jogo()

if(__name__ == "__main__"):
    main()