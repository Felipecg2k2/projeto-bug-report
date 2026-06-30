def cadastro_academia():
    print("--- Cadastro de Alunos - Academia Forma Física ---")
    nome = input("Nome do aluno: ")
    idade_str = input("Idade: ")
    
    try:
        idade = int(idade_str)
    except ValueError:
        print("Idade deve ser um número inteiro.")
        return

    if idade > 14:
        print(f"Cadastro aprovado! Bem-vindo(a), {nome}.")
        peso_str = input("Peso atual (kg): ")
        try:
            peso = float(peso_str)
            print(f"Dados salvos com sucesso. Aluno: {nome}, Idade: {idade}, Peso: {peso}kg.")
        except ValueError:
            print("Erro ao registrar o peso.")
    else:
        print("Cadastro negado. A idade mínima para matrícula é 14 anos.")

if __name__ == "__main__":
    cadastro_academia()