# Função para obter o signo do zodíaco com base na data de nascimento
def obter_signo(dia, mes):
    signos = [
        {"signo": "Capricórnio", "inicio": {"dia": 22, "mes": 12}, "fim": {"dia": 20, "mes": 1}},
        {"signo": "Aquário", "inicio": {"dia": 21, "mes": 1}, "fim": {"dia": 19, "mes": 2}},
        {"signo": "Peixes", "inicio": {"dia": 20, "mes": 2}, "fim": {"dia": 20, "mes": 3}},
        {"signo": "Áries", "inicio": {"dia": 21, "mes": 3}, "fim": {"dia": 20, "mes": 4}},
        {"signo": "Touro", "inicio": {"dia": 21, "mes": 4}, "fim": {"dia": 20, "mes": 5}},
        {"signo": "Gêmeos", "inicio": {"dia": 21, "mes": 5}, "fim": {"dia": 20, "mes": 6}},
        {"signo": "Câncer", "inicio": {"dia": 21, "mes": 6}, "fim": {"dia": 22, "mes": 7}},
        {"signo": "Leão", "inicio": {"dia": 23, "mes": 7}, "fim": {"dia": 22, "mes": 8}},
        {"signo": "Virgem", "inicio": {"dia": 23, "mes": 8}, "fim": {"dia": 22, "mes": 9}},
        {"signo": "Libra", "inicio": {"dia": 23, "mes": 9}, "fim": {"dia": 22, "mes": 10}},
        {"signo": "Escorpião", "inicio": {"dia": 23, "mes": 10}, "fim": {"dia": 21, "mes": 11}},
        {"signo": "Sagitário", "inicio": {"dia": 22, "mes": 11}, "fim": {"dia": 21, "mes": 12}}
    ]

    for s in signos:
        if ((mes == s["inicio"]["mes"] and dia >= s["inicio"]["dia"]) or
                (mes == s["fim"]["mes"] and dia <= s["fim"]["dia"])):
            return s["signo"]
    return "Signo desconhecido"

# Função para obter as comemorações do dia e mês especificados
def obter_comemoracoes(dia, mes):
    comemoracoes = {
        (1, 1): ["Ano Novo"],
        (6, 1): ["Dia de Reis"],
        (20, 1): ["Dia de São Sebastião"],
        (25, 1): ["Aniversário da Cidade de São Paulo"],
        (2, 2): ["Dia de Iemanjá"],
        (8, 3): ["Dia Internacional da Mulher"],
        (19, 3): ["Dia de São José"],
        (20, 3): ["Início do Outono"],
        (1, 4): ["Dia da Mentira"],
        (7, 4): ["Dia Mundial da Saúde"],
        (21, 4): ["Tiradentes"],
        (22, 4): ["Descobrimento do Brasil"],
        (23, 4): ["Dia de São Jorge"],
        (24, 4): ["Dia do Chimarrão e Dia do Churrasco"],
        (1, 5): ["Dia do Trabalhador"],
        (13, 5): ["Abolição da Escravatura"],
        (31, 5): ["Dia Mundial sem Tabaco"],
        (5, 6): ["Dia Mundial do Meio Ambiente"],
        (12, 6): ["Dia dos Namorados"],
        (13, 6): ["Dia de Santo Antônio"],
        (20, 6): ["Dia do Refugiado"],
        (24, 6): ["Dia de São João"],
        (29, 6): ["Dia de São Pedro"],
        (2, 7): ["Dia do Bombeiro Brasileiro"],
        (9, 7): ["Revolução Constitucionalista de 1932"],
        (20, 7): ["Dia do Amigo e Internacional da Amizade"],
        (26, 7): ["Dia dos Avós"],
        (11, 8): ["Dia do Estudante"],
        (15, 8): ["Assunção de Nossa Senhora"],
        (22, 8): ["Dia do Folclore"],
        (25, 8): ["Dia do Soldado"],
        (7, 9): ["Independência do Brasil"],
        (20, 9): ["Revolução Farroupilha"],
        (21, 9): ["Dia da Árvore"],
        (23, 9): ["Início da Primavera"],
        (4, 10): ["Dia de São Francisco de Assis"],
        (12, 10): ["Dia de Nossa Senhora Aparecida", "Dia das Crianças"],
        (15, 10): ["Dia do Professor"],
        (28, 10): ["Dia do Funcionário Público"],
        (2, 11): ["Dia de Finados"],
        (15, 11): ["Proclamação da República"],
        (19, 11): ["Dia da Bandeira"],
        (20, 11): ["Dia da Consciência Negra"],
        (8, 12): ["Dia de Nossa Senhora da Conceição"],
        (21, 12): ["Início do Verão"],
        (24, 12): ["Véspera de Natal"],
        (25, 12): ["Natal"],
        (31, 12): ["Véspera de Ano Novo"]
    }

    return comemoracoes.get((dia, mes), ["Nenhuma comemoração encontrada para este dia"])

# Função para obter a estação do ano com base na data de nascimento
def obter_estacao(dia, mes):
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia < 21):
        return "Verão"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia < 21):
        return "Outono"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia < 23):
        return "Inverno"
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia < 21):
        return "Primavera"
    return "Estação desconhecida"

# Função principal para executar o programa
def executar_programa():
    nome = input("Digite seu nome: ")
    data_nascimento = input("Digite sua data de nascimento (dd/mm): ")
    dia, mes = map(int, data_nascimento.split("/"))

    signo = obter_signo(dia, mes)
    estacao = obter_estacao(dia, mes)
    comemoracoes = obter_comemoracoes(dia, mes)

    print(f"Olá {nome},\nNo seu dia {dia} de {mes}, você tem o signo {signo} e está na estação {estacao}.\nSão comemorados: {', '.join(comemoracoes)}.")

executar_programa()
