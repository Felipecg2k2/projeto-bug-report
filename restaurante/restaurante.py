def dividir_conta():
    print("--- Calculadora de Conta de Restaurante ---")
    valor_str = input("Qual o valor total da conta? R$ ")
    try:
        valor = float(valor_str)
    except ValueError:
        print("Valor inválido.")
        return

    taxa_servico = input("Deseja incluir os 10% do garçom? (S/N): ").upper()
    if taxa_servico == 'S':
        valor += valor * 0.10
        
    pessoas_str = input("Dividir a conta para quantas pessoas? ")
    try:
        pessoas = int(pessoas_str)
    except ValueError:
        print("Número de pessoas inválido.")
        return
        
    valor_por_pessoa = valor / pessoas
    
    print(f"\nO total com taxa (se aplicável) ficou R$ {valor:.2f}")
    print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")

if __name__ == "__main__":
    dividir_conta()
