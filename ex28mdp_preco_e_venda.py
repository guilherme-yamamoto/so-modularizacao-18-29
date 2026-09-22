def novo_preco(venda, preco):
    if(venda < 500 and preco < 30):
        valor_final = preco * 1.10
        print(f"O preço novo terá 10% de aumento. R${preco:.2f} -> R${valor_final:.2f}.")
    elif(venda >= 500 and venda < 1000 and preco >= 30 and preco < 80):
        valor_final = preco * 1.15
        print(f"O preço novo terá 15% de aumento. R${preco:.2f} -> R${valor_final:.2f}.")
    elif(venda >= 1000 and preco >= 80):
        valor_final = preco * 0.95
        print(f"O preço novo terá 5% de desconto. R${preco:.2f} -> R${valor_final:.2f}.")
    else:
        valor_final = preco
        print(f"O preço permanecerá igual. R${preco:.2f}.")

def main():
    venda = int(input("Insira a quantidade de vendas mensais: "))
    preco = float(input("Insira o preço atual: "))
    novo_preco(venda, preco)

if(__name__ == "__main__"):
    main()