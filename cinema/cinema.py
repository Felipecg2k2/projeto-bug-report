print("--- BILHETERIA DO CINEMA ---")
qtd = int(input("Quantos ingressos deseja comprar? (R$ 20,00 cada): "))
estudante = input("Você é estudante? (s/n): ")
dinheiro = float(input("Qual valor em dinheiro você entregou?: "))

valor_total = qtd * 20

# BUG 1: A meia entrada dá 10% de desconto em vez de 50%
if estudante.lower() == 's':
    valor_total = valor_total * 0.90
    print(f"Meia entrada aplicada. Novo total: R$ {valor_total}")
else:
    print(f"Total: R$ {valor_total}")

# BUG 2: Cálculo de troco invertido
troco = valor_total - dinheiro
print(f"Seu troco é: R$ {troco}")
print("Bom filme!")
