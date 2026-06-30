print("--- GESTOR DE ESTACIONAMENTO ---")
print("Valor fixo: R$ 5,00 a hora")

entrada = int(input("Que horas o carro entrou? (apenas a hora ex: 14): "))
saida = int(input("Que horas o carro saiu? (ex: 16): "))

horas_estacionadas = saida - entrada

# BUG 1: Se ele entrar 14 e sair 14, vai multiplicar 0 * 5, dando R$ 0. (Deveria cobrar mínimo de 1 hora)
valor_pagar = horas_estacionadas * 5

# BUG 2: Se o usuário digitar saída MENOR que entrada (ex: erro de digitação), gera valor negativo.
print(f"O carro ficou {horas_estacionadas} horas.")
print(f"Total a pagar: R$ {valor_pagar}")