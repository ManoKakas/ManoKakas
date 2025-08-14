# Bem-vindo à fábrica de camisetas do Kauã
print("Bem-vindo à fábrica de camisetas do Kauã.")

def escolha_modelo():
    while True:
        print("\nModelos disponíveis:")
        print("MCS - Manga Curta Simples (R$1.80)")
        print("MLS - Manga Longa Simples (R$2.10)")
        print("MCE - Manga Curta com Estampa (R$2.90)")
        print("MLE - Manga Longa com Estampa (R$3.20)")
        modelo = input("Digite o código do modelo: ").upper()
        if modelo == "MCS":
            return 1.80
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido. Tente de novo.\n")

def num_camisetas():
    while True:
        try:
            qtd = int(input("Digite a quantidade de camisetas: "))
            if qtd > 20000:
                print("Não aceitamos pedidos com mais de 20000 camisetas.\n")
            elif qtd < 20:
                return qtd
            elif qtd < 200:
                return qtd * 0.95
            elif qtd < 2000:
                return qtd * 0.93
            else:
                return qtd * 0.88
        except:
            print("Digite um número válido.\n")

def frete():
    while True:
        print("\nOpções de frete:")
        print("0 - Retirar na fábrica (R$0)")
        print("1 - Transportadora (R$100)")
        print("2 - Sedex (R$200)")
        tipo = input("Escolha o tipo de frete: ")
        if tipo == "0":
            return 0
        elif tipo == "1":
            return 100
        elif tipo == "2":
            return 200
        else:
            print("Frete inválido. Tente de novo.\n")

# Execução principal
preco_unitario = escolha_modelo()
quantidade = num_camisetas()
valor_frete = frete()
total = (preco_unitario * quantidade) + valor_frete

print(f"\nTotal a pagar: R$ {total:.2f}")
