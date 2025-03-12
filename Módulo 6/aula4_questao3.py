# Dados das horas trabalhadas
horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

# Cálculo dos pagamentos com compreensão de lista
pagamentos = [ganho_por_hora * min(h, 40) + hora_extra * max(0, h - 40) for h in horas_trabalhadas]

# Exibição dos pagamentos
print("Pagamentos:", pagamentos)
