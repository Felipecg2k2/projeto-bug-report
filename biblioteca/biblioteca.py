print("--- SISTEMA DE EMPRÉSTIMO DA BIBLIOTECA ---")
print("Regras: Infantil (0-12) | Jovem (13-17) | Adulto (18+)")

idade = int(input("Qual a sua idade?: "))

# BUG 1: O 12 e o 18 ficaram de fora do "range" (Problema de Valor Limite).
if idade < 12:
    print("Você pode acessar a seção INFANTIL.")
elif idade > 12 and idade < 18:
    print("Você pode acessar a seção JOVEM.")
elif idade > 18:
    print("Você pode acessar a seção ADULTA.")
else:
    # BUG 2: Este else vai capturar quem tiver 12 ou 18 anos exatos!
    print("ERRO: Idade inválida para empréstimo.")
