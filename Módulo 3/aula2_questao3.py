# Solicita os dados do usuário
idade = int(input("Digite sua idade: "))
jogou_3_jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? (True/False): ").strip().lower() == "true"
vitorias = int(input("Quantos jogos já venceu? "))

# Verifica se a pessoa pode ingressar no clube
apto = 16 <= idade <= 18 and jogou_3_jogos and vitorias >= 1

# Exibe o resultado
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto}")