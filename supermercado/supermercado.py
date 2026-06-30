def caixa_supermercado():
    print("--- Caixa Aberto ---")
    total = 0.0
    while True:
        preco_str = input("Digite o preço do item (ou 0 para finalizar): ")
        try:
            preco = float(preco_str)
        except ValueError:
            print("Valor inválido.")
            continue
            
        if preco == 0:
            break
            
        total += preco
        print(f"Subtotal: R$ {total:.2f}")
        
    print(f"\nTotal da compra: R$ {total:.2f}")
    pagamento_str = input("Valor recebido em dinheiro: R$ ")
    try:
        pagamento = float(pagamento_str)
        troco = pagamento - total
        print(f"Troco a devolver: R$ {troco:.2f}")
    except ValueError:
        print("Valor recebido inválido.")
    print("--- Caixa Fechado ---")

if __name__ == "__main__":
    caixa_supermercado()
