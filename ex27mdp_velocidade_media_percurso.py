def velocidade(voltas, distancia, duracao):
    velocidade_media = ((distancia * voltas) / (duracao * 60)) * 3.6
    print(f"A velocidade média é de {velocidade_media:.2f} km/h")

def main():
    voltas = int(input("Insira a quantidade de voltas do percurso: "))
    distancia = float(input("Insira a distância do percurso: "))
    duracao = float(input("Insira a duração do percurso: "))
    velocidade(voltas, distancia, duracao)

if(__name__ == "__main__"):
    main()