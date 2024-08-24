import sqlite3

def inserir_dados():
    pass

conexao = sqlite3.connect('banco_biblioteca/banco_biblioteca')
cursor = conexao.cursor()

autores = [
    (10, 'Stephen King', 'Americana'),
    (11, 'Edgar Allan Poe', 'Americana'),
    (12, 'Anne Rice', 'Americana'),
    (14, 'George Orwell', 'Britânica'),
    (13, 'Clarice Lispector', 'Brasileira'),
    (15, 'Stephenie Meyer', 'Americana')
]

cursor.executemany("INSERT INTO Autor (id_autor, nome, nacionalidade) VALUES (?, ?, ?)", autores)

genero = [
    (13, 'Terror',),
    (14, 'Contos',),
    (15, 'Ficção Científica',)
]

cursor.executemany("INSERT INTO Genero (id_genero, genero) VALUES (?, ? )", genero)


autor_livro = [
    (20, 10),
    (21, 10),
    (22, 10),
    (23, 10),
    (24, 10),
    (25, 11),
    (26, 11),
    (27, 11),
    (28, 11),
    (29, 12),
    (30, 12),
    (31, 12),
    (32, 12),
    (33, 12),
    (34, 13),
    (35, 13),
    (36, 13),
    (37, 13),
    (38, 13),
    (39, 13),
    (40, 11),
    (41, 11),
    (42, 11),
    (43, 11),
    (44, 10),
    (45, 14),
    (46, 14),
    (47, 14),
    (48, 14),
    (49, 14),
    (50, 14),
    (51, 15),
    (52, 15),
    (53, 15)
]

cursor.executemany("INSERT INTO Autor_Livro (id_livro, id_autor) VALUES (?, ? )", autor_livro)

livro_genero = [
    (20, 13),
    (21, 13),
    (22, 13),
    (23, 13),
    (24, 13),
    (25, 13),
    (26, 13),
    (27, 13),
    (28, 13),
    (29, 13),
    (30, 13),
    (31, 13),
    (32, 13),
    (33, 13),
    (34, 14),
    (35, 14),
    (36, 14),
    (37, 14),
    (38, 14),
    (39, 14),
    (40, 14),
    (41, 14),
    (42, 14),
    (43, 14),
    (44, 15),
    (45, 15),
    (46, 15),
    (47, 15),
    (48, 15),
    (49, 15),
    (50, 15),
    (51, 15),
    (52, 15),
    (53, 15)
]

cursor.executemany("INSERT INTO Livro_Genero (id_livro, id_genero) VALUES (?, ? )", livro_genero)

livros = [
    (20, "O Iluminado", "Doubleday"),
    (21, "Carrie", "Doubleday"),
    (22, "It A coisa", "Viking"),
    (23, "Misery", "Viking"),
    (24, "Cemitério Maldito", "Doubleday"),
    (25, "O Gato Preto", "The Saturday Evening Post"),
    (26, "A Queda da Casa de Usher", "Burton's Gentleman's Magazine"),
    (27, "O Coração Denunciador", "The Pioneer"),
    (28, "O Barril de Amontillado", "Godey's Lady's Book"),
    (29, "Entrevista com o Vampiro", "Alfred A. Knopf"),
    (30, "O Vampiro Lestat", "Alfred A. Knopf"),
    (31, "A Rainha dos Condenados", "Alfred A. Knopf"),
    (32, "A História do Ladrão de Corpos", "Alfred A. Knopf"),
    (33, "O Vampiro Armand", "Alfred A. Knopf"),
    (34, "Laços de Família", "Francisco Alves"),
    (35, "Amor", "Rocco"),
    (36, "Felicidade Clandestina", "Rocco"),
    (37, "O Crime do Professor de Matemática", "Rocco"),
    (38, "A Menor Mulher do Mundo", "Rocco"),
    (39, "A Imitação da Rosa", "Rocco"),
    (40, "O Escaravelho de Ouro", "Martin Claret"),
    (41, "Os Assassinatos na Rua Morgue", "Graham's Magazine"),
    (42, "A Carta Roubada", "Martin Claret"),
    (43, "Duque de l'Omelette", "Martin Claret"),
    (44, "A Zona Morta", "Viking"),
    (45, "1984", "Secker & Warburg"),
    (46, "A Revolução dos Bichos", "Secker & Warburg"),
    (47, "O Caminho para Wigan Pier", "Victor Gollancz Ltd"),
    (48, "A Flor da Inglaterra", "Gollancz"),
    (49, "Dias na Birmânia", "Harper & Brothers"),
    (50, "A Aventura Sem Paralelo de um Certo Hans Pfaall", "Martin Claret"),
    (51, "Crepúsculo", "Intrínseca"),
    (52, "Lua Nova", "Intrínseca"),
    (53, "A Hospedeira", "Intrínseca")
]

cursor.executemany("INSERT INTO Livro (id_livro, titulo, editora) VALUES (?, ?, ?)", livros)

conexao.commit()

conexao.close()