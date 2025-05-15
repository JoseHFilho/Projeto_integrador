def adicionar_membro(grupo, membros):
    print("=== Adicionar novo membro ao grupo ===")
    novo_membro = input("Nome ou e-mail do novo membro: ")
    if novo_membro in membros:
        print("Este membro já está no grupo.")
    else:
        membros.append(novo_membro)
        print(f"{novo_membro} adicionado com sucesso ao grupo '{grupo}'!")

# Execução de exemplo
if __name__ == "__main__":
    grupo, esporte, membros = criar_grupo()
    adicionar_membro(grupo, membros)
    print("Membros atuais:", membros)
