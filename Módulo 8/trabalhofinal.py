import csv
import os
import getpass

# Arquivos para armazenar os dados
ARQUIVO_USUARIOS = "usuarios.csv"
ARQUIVO_PRODUTOS = "produtos.csv"

def carregar_usuarios():
    usuarios = {}
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) >= 3:
                    usuarios[linha[0].strip()] = {"senha": linha[1].strip(), "permissao": linha[2].strip()}
    return usuarios

def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for usuario, dados in usuarios.items():
            writer.writerow([usuario, dados["senha"], dados["permissao"]])

def carregar_produtos():
    produtos = []
    if os.path.exists(ARQUIVO_PRODUTOS):
        with open(ARQUIVO_PRODUTOS, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for linha in reader:
                if len(linha) >= 3:
                    try:
                        produtos.append({"nome": linha[0].strip(), "preco": float(linha[1]), "quantidade": int(linha[2])})
                    except ValueError:
                        print(f"Erro ao carregar produto: {linha}")
    return produtos

def salvar_produtos(produtos):
    with open(ARQUIVO_PRODUTOS, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        for produto in produtos:
            writer.writerow([produto["nome"], produto["preco"], produto["quantidade"]])

def login(usuarios):
    for _ in range(3):
        usuario = input("Nome de usuário: ").strip()
        try:
            senha = getpass.getpass("Senha: ").strip()
        except Exception:
            senha = input("Senha: ").strip()
        
        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            print(f"Bem-vindo, {usuario}!")
            return usuario, usuarios[usuario]["permissao"]
        print("Usuário ou senha incorretos. Tente novamente.")
    print("Muitas tentativas inválidas. Encerrando.")
    return None, None

def cadastrar_usuario(usuarios):
    nome = input("Nome do usuário: ").strip()
    try:
        senha = getpass.getpass("Senha: ").strip()
    except Exception:
        senha = input("Senha: ").strip()
    
    permissao = input("Permissão (admin/funcionario): ").strip().lower()
    if permissao not in ["admin", "funcionario"]:
        print("Permissão inválida! Use 'admin' ou 'funcionario'.")
        return
    usuarios[nome] = {"senha": senha, "permissao": permissao}
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso!")

def adicionar_produto(produtos):
    nome = input("Nome do produto: ").strip()
    try:
        preco = float(input("Preço: ").strip())
        quantidade = int(input("Quantidade: ").strip())
        produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})
        salvar_produtos(produtos)
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Erro: Preço e quantidade devem ser numéricos!")

def listar_produtos(produtos, ordenar_por="nome"):
    if ordenar_por == "preco":
        produtos.sort(key=lambda x: x["preco"])
    else:
        produtos.sort(key=lambda x: x["nome"].lower())
    if not produtos:
        print("Nenhum produto cadastrado.")
    for produto in produtos:
        print(f"{produto['nome']} - R${produto['preco']:.2f} - {produto['quantidade']} unidades")

def buscar_produto(produtos):
    nome = input("Nome do produto: ").strip()
    for produto in produtos:
        if produto["nome"].lower() == nome.lower():
            print(f"Encontrado: {produto['nome']} - R${produto['preco']:.2f} - {produto['quantidade']} unidades")
            return
    print("Produto não encontrado!")

def main():
    usuarios = carregar_usuarios()
    produtos = carregar_produtos()
    usuario, permissao = login(usuarios)
    if usuario:
        while True:
            print("\nMenu Principal")
            print("1. Cadastrar Usuário (Admin)")
            print("2. Adicionar Produto")
            print("3. Listar Produtos")
            print("4. Buscar Produto")
            print("5. Sair")
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1" and permissao == "admin":
                cadastrar_usuario(usuarios)
            elif opcao == "1":
                print("Apenas administradores podem cadastrar usuários!")
            elif opcao == "2":
                adicionar_produto(produtos)
            elif opcao == "3":
                listar_produtos(produtos, "nome")
            elif opcao == "4":
                buscar_produto(produtos)
            elif opcao == "5":
                print("Saindo do sistema. Até mais!")
                break
            else:
                print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()