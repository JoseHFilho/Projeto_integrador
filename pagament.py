def pagamento_antecipado():
    print("=== Pagamento Antecipado ===")
    valor = float(input("Digite o valor da reserva (R$): "))
    metodo = input("Forma de pagamento (Pix/Cartão): ").lower()

    if metodo in ["pix", "cartão"]:
        print(f"Pagamento de R${valor:.2f} realizado com sucesso via {metodo.capitalize()}!")
    else:
        print("Forma de pagamento inválida.")
