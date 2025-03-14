def mes_por_extenso(data):
    meses = {
        "01": "janeiro", "02": "fevereiro", "03": "março", "04": "abril",
        "05": "maio", "06": "junho", "07": "julho", "08": "agosto",
        "09": "setembro", "10": "outubro", "11": "novembro", "12": "dezembro"
    }

    partes = data.split('/')
    dia = partes[0]
    mes = partes[1]
    ano = partes[2]

    if mes in meses:
        print(f"Você nasceu em {dia} de {meses[mes]} de {ano}.")
    else:
        print("Data inválida.")

# Entrada do usuário
data_usuario = input("Digite sua data de nascimento (dd/mm/aaaa): ")
mes_por_extenso(data_usuario)
