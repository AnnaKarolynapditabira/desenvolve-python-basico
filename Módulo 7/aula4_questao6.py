# aula4_questao6.py
import csv

# Abrir e processar arquivo
with open("spotify-2023.csv", "r", encoding="latin-1") as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho

    # Criar dicionário para armazenar as músicas mais tocadas por ano
    top_musicas = {}

    for linha in leitor:
        try:
            track_name, artist_name, _, released_year, _, _, _, _, streams, _ = linha
            released_year = int(released_year)
            streams = int(streams)

            # Considerar apenas anos de 2012 a 2022
            if 2012 <= released_year <= 2022:
                if released_year not in top_musicas or streams > top_musicas[released_year][3]:
                    top_musicas[released_year] = [track_name, artist_name, released_year, streams]
        except ValueError:
            continue  # Ignora linhas inválidas

# Criar lista ordenada por ano
musicas_top10 = [top_musicas[ano] for ano in sorted(top_musicas.keys())]

# Exibir resultado
print(musicas_top10)
