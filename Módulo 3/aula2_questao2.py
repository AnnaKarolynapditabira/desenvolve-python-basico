# Solicitar as idades de Juliana e Cris
idade_juliana = int(input("Digite a idade de Juliana: "))
idade_cris = int(input("Digite a idade de Cris: "))

# Verifica se pelo menos um dos dois é maior de idade (>17)
pode_entrar = idade_juliana > 17 or idade_cris > 17

# Exibe o resultado
print(pode_entrar)