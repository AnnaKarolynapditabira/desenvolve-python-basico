# Solicita ao usuário um valor inteiro em reais
valor = int(input("Digite um valor inteiro em reais: "))

# Lista das notas disponíveis
notas = [100, 50, 20, 10, 5, 2, 1]

# Percorre a lista de notas e calcula a quantidade necessária de cada uma
for nota in notas:
    quantidade = valor // nota  # Calcula quantas notas desse valor são necessárias
    valor %= nota  # Atualiza o valor restante
    print(f"{quantidade} nota(s) de R${nota},00")
