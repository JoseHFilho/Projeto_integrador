def avaliar(entidade):
    print(f"=== Avaliação de {entidade} ===")
    nota = int(input("Dê uma nota de 1 a 5: "))
    comentario = input("Deixe um comentário (opcional): ")

    if 1 <= nota <= 5:
        print(f"\nObrigado! Você avaliou {entidade} com nota {nota}.")
        if comentario:
            print(f"Comentário: \"{comentario}\"")
    else:
        print("Nota inválida. Tente novamente.")
