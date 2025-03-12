# Listas de alunos e notas
alunos = ["Maria", "Jose", "Carla", "Sol"]
notas = [35, 50, 20, 80]

# Lista de aprovados com compreensão de lista
aprovados = [alunos[i] for i in range(len(notas)) if notas[i] >= 60]

# Exibição dos aprovados
print("Alunos aprovados:", aprovados)
