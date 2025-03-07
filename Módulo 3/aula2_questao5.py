# Solicita os dados do usuário
genero = input("Digite seu gênero (M/F): ").strip().upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

# Verifica se a pessoa pode se aposentar
if genero == "F":
    pode_aposentar = idade > 60 or tempo_servico >= 30 or (idade == 60 and tempo_servico >= 25)
elif genero == "M":
    pode_aposentar = idade > 65 or tempo_servico >= 30 or (idade == 60 and tempo_servico >= 25)
else:
    pode_aposentar = False  # Gênero inválido

# Exibe o resultado
print(pode_aposentar)