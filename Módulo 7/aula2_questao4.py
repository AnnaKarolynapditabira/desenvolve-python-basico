import re

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False

    # Verifica se contém pelo menos uma letra maiúscula
    if not re.search(r'[A-Z]', senha):
        return False

    # Verifica se contém pelo menos uma letra minúscula
    if not re.search(r'[a-z]', senha):
        return False

    # Verifica se contém pelo menos um número
    if not re.search(r'\d', senha):
        return False

    # Verifica se contém pelo menos um caractere especial
    if not re.search(r'[@#$%^&+=!]', senha):
        return False

    return True

# Solicita ao usuário que digite a senha com informações sobre os requisitos
print("A senha deve atender aos seguintes requisitos:")
print("- Pelo menos 8 caracteres de comprimento.")
print("- Deve conter pelo menos uma letra maiúscula (A-Z).")
print("- Deve conter pelo menos uma letra minúscula (a-z).")
print("- Deve conter pelo menos um número (0-9).")
print("- Deve conter pelo menos um caractere especial, como @, #, $, %, ^, &, +, =, ou !.")

senha_usuario = input("\nDigite a senha: ")

# Chama a função e exibe o resultado
if validador_senha(senha_usuario):
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve atender aos critérios acima.")
