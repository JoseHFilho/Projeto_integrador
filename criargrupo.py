def criar_grupo():
    print("=== Criar Grupo de Jogo ===")
    nome_grupo = input("Nome do grupo: ")
    esporte = input("Esporte praticado: ")
    criador = input("Seu nome ou e-mail: ")

    print(f"\nGrupo '{nome_grupo}' de {esporte} criado por {criador} com sucesso!")
    return nome_grupo, esporte, [criador]
