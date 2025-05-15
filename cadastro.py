def cadastrar_usuario():
    print("=== Cadastro de Usuário ===")
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu e-mail: ")
    cpf = input("Digite o seu CPF (somente números): ")
    senha = input("Digite a sua senha: ")

    print("\nCadastro realizado!")

    return nome, email, cpf, senha


def verificar_login(cpf_cadastrado, senha_cadastrada, nome):
    print("\n=== Verificação de Cadastro ===")
    vercpf = input("Digite novamente o seu CPF: ")
    versenha = input("Digite novamente a sua senha: ")

    if vercpf == cpf_cadastrado and versenha == senha_cadastrada:
        print(f"\nBem-vindo(a), {nome}!")
    else:
        print("\nDados incorretos. Tente novamente!")
