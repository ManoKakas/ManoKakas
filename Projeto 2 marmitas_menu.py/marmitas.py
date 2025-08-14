# Bem-vindo ao restaurante do Kauã :)
print("Bem-vindos ao restaurante do Kauã :)")
print("Cardápio:")
print("Bife Acebolado (BA)")
print(" - P: R$16")
print(" - M: R$18")
print(" - G: R$22")
print("Filé de Frango (FF)")
print(" - P: R$15")
print(" - M: R$17")
print(" - G: R$21\n")

total = 0

while True:
    sabor = input("Digite o sabor (BA para Bife Acebolado ou FF para Filé de Frango): ").upper()
    if sabor != "BA" and sabor != "FF":
        print("Sabor inválido. Tente novamente.\n")
        continue

    tamanho = input("Digite o tamanho (P, M ou G): ").upper()
    if tamanho not in ["P", "M", "G"]:
        print("Tamanho inválido. Tente novamente.\n")
        continue

    if sabor == "BA":
        preco = {"P": 16, "M": 18, "G": 22}[tamanho]
    else:
        preco = {"P": 15, "M": 17, "G": 21}[tamanho]

    print(f"Você escolheu {sabor} tamanho {tamanho}. Valor: R$ {preco:.2f}\n")
    total += preco

    mais = input("Deseja pedir mais alguma coisa? (S para sim / N para não): ").upper()
    if mais != "S":
        break

print(f"\nValor total do seu pedido: R$ {total:.2f}")
print("Obrigado por comprar com a gente! :)")
