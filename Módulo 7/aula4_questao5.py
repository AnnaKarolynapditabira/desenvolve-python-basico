# aula4_questao5.py
livros = [
    ["Título", "Autor", "Ano de publicação", "Número de páginas"],
    ["O Caçador de Pipas", "Khaled Hosseini", "2003", "368"],
    ["Torto Arado", "Itamar Vieira Junior", "2019", "264"],
    ["1984", "George Orwell", "1949", "328"],
    ["Dom Casmurro", "Machado de Assis", "1899", "256"],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "96"],
    ["A Revolução dos Bichos", "George Orwell", "1945", "152"],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", "1997", "223"],
    ["O Hobbit", "J.R.R. Tolkien", "1937", "310"],
    ["Senhor dos Anéis", "J.R.R. Tolkien", "1954", "1178"],
    ["Percy Jackson e o Ladrão de Raios", "Rick Riordan", "2005", "400"]
]

with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    for livro in livros:
        arquivo.write(",".join(livro) + "\n")