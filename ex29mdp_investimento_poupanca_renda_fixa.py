def investimento(tipo, valor):
    if(tipo == 1):
        rendimento = valor * 1.03
        print(f"Os R${valor:.2f} investidos renderam 3% em 1 mês, que equivale a R${(rendimento - valor):.2f}, e totalizou {rendimento:.2f}")
    elif(tipo == 2):
        rendimento = valor * 1.05
        print(f"Os R${valor:.2f} investidos renderam 5% em 1 mês, que equivale a R${(rendimento - valor):.2f}, e totalizou {rendimento:.2f}")

def main():
    tipo = int(input("Digite o tipo de investimento:\n[1 - Poupança, 2 - Renda Fixa] -> "))
    while(tipo != 1 and tipo != 2):
        print(f"O valor inserido ({tipo}) não é válido.\n")
        tipo = int(input("Digite novamente o tipo de investimento:\n[1 - Poupança, 2 - Renda Fixa] -> "))

    valor = float(input("Insira o valor a ser investido: "))
    investimento(tipo, valor)

if(__name__ == "__main__"):
    main()