def carregar_dados():
    dados = []

    arquivo = open("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv", "r")

    cabecalho = arquivo.readline()

    for linha in arquivo:
        linha = linha.strip()
        valores = linha.split(",")

        dados.append(valores)

    arquivo.close()

    return dados


dados = carregar_dados()

print("Quantidade de registros:", len(dados))

primeira_data = dados[0][0]

data_separada = primeira_data.split("/")

dia = int(data_separada[0])
mes = int(data_separada[1])
ano = int(data_separada[2])

mes_inicial = int(input("Informe o mês inicial (1 a 12): "))

while mes_inicial < 1 or mes_inicial > 12:
    print("Mês inválido!")
    mes_inicial = int(input("Informe o mês inicial (1 a 12): "))

ano_inicial = int(input("Informe o ano inicial (1961 a 2016): "))

while ano_inicial < 1961 or ano_inicial > 2016:
    print("Ano inválido!")
    ano_inicial = int(input("Informe o ano inicial (1961 a 2016): "))

mes_final = int(input("Informe o mês final (1 a 12): "))

while mes_final < 1 or mes_final > 12:
    print("Mês inválido!")
    mes_final = int(input("Informe o mês final (1 a 12): "))

ano_final = int(input("Informe o ano final (1961 a 2016): "))

while ano_final < 1961 or ano_final > 2016:
    print("Ano inválido!")
    ano_final = int(input("Informe o ano final (1961 a 2016): "))

while ano_final < ano_inicial or (ano_final == ano_inicial and mes_final < mes_inicial):
    print("Período inválido! A data final não pode ser anterior à data inicial.")

    mes_final = int(input("Informe o mês final (1 a 12): "))

    while mes_final < 1 or mes_final > 12:
        print("Mês inválido!")
        mes_final = int(input("Informe o mês final (1 a 12): "))

    ano_final = int(input("Informe o ano final (1961 a 2016): "))

    while ano_final < 1961 or ano_final > 2016:
        print("Ano inválido!")
        ano_final = int(input("Informe o ano final (1961 a 2016): "))

print("\nO que deseja visualizar?")
print("1 - Todos os dados")
print("2 - Precipitação")
print("3 - Temperatura")
print("4 - Umidade e vento")

opcao = int(input("Escolha uma opção: "))

while opcao < 1 or opcao > 4:
    print("Opção inválida!")
    opcao = int(input("Escolha uma opção: "))

for registro in dados:
    data = registro[0].split("/")

    mes = int(data[1])
    ano = int(data[2])

    depois_inicio = ano > ano_inicial or (ano == ano_inicial and mes >= mes_inicial)
    antes_fim = ano < ano_final or (ano == ano_final and mes <= mes_final)

    if depois_inicio and antes_fim:

        if opcao == 1:
            print(registro)

        elif opcao == 2:
            print("Data:", registro[0], "- Precipitação:", registro[1])

        elif opcao == 3:
            print(
                "Data:", registro[0],
                "- Máxima:", registro[2],
                "- Mínima:", registro[3],
                "- Média:", registro[5]
            )

        elif opcao == 4:
            print(
                "Data:", registro[0],
                "- Umidade:", registro[6],
                "- Vento:", registro[7]
            )    