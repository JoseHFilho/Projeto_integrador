def exibir_horarios_disponiveis(horarios):
    print("\nHorários disponíveis para agendamento:")
    for hora in range(14, 23):  # 14h até 22h
        status = "Disponível" if not horarios[hora] else f"Reservado por {horarios[hora]}"
        print(f"{hora}:00 - {status}")


def agendar_quadra(horarios):
    nome = input("\nDigite seu nome para agendar a quadra: ")

    try:
        hora_desejada = int(input("Escolha um horário (14-22): "))
        if hora_desejada < 14 or hora_desejada > 22:
            print("Horário inválido. Escolha entre 14 e 22.")
            return
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return

    if horarios[hora_desejada] == "":
        horarios[hora_desejada] = nome
        print(f"Quadra agendada com sucesso para {hora_desejada}:00 por {nome}!")
    else:
        print(f"Horário {hora_desejada}:00 já está reservado por {horarios[hora_desejada]}.")


def main():
    horarios = {hora: "" for hora in range(14, 23)}  # 14h até 22h

    while True:
        exibir_horarios_disponiveis(horarios)
        agendar_quadra(horarios)

        continuar = input("\nDeseja fazer outro agendamento? (s/n): ").lower()
        if continuar != 's':
            print("\nEncerrando sistema de agendamento. Obrigado!")
            break
