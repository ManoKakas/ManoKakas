# Bem-vindo à loja do Kauã
print("Bem-vindos à loja do Kauã.")

# Entrada de dados
valorDoPedido = float(input("Digite o valor do pedido: R$ "))
quantidadeParcelas = int(input("Digite a quantidade de parcelas: "))

# Cálculo de juros conforme quantidade de parcelas
if quantidadeParcelas < 4:
    juros = 0 / 100
elif quantidadeParcelas >= 4 and quantidadeParcelas < 6:
    juros = 4 / 100
elif quantidadeParcelas >= 6 and quantidadeParcelas < 9:
    juros = 8 / 100
elif quantidadeParcelas >= 9 and quantidadeParcelas < 13:
    juros = 16 / 100
else:
    juros = 32 / 100

# Cálculo do valor total e das parcelas
valorTotalParcelado = valorDoPedido * (1 + juros)
valorDaParcela = valorTotalParcelado / quantidadeParcelas

# Saída de dados
print("\nResumo do pedido:")
print("Valor original do pedido: R$ {:.2f}".format(valorDoPedido))
print("Quantidade de parcelas: {}".format(quantidadeParcelas))
print("Juros aplicado: {}%".format(int(juros * 100)))
print("Valor total com juros: R$ {:.2f}".format(valorTotalParcelado))
print("Valor de cada parcela: R$ {:.2f}".format(valorDaParcela))
