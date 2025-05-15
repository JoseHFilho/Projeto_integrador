def cancelar_agendamento():
    print("=== Cancelar Agendamento ===")
    confirmar = input("Deseja mesmo cancelar seu agendamento? (s/n): ")

    if confirmar.lower() == "s":
        print("Agendamento cancelado com sucesso.")
    else:
        print("Cancelamento abortado.")

