import sqlite3

def inserir_dados():
    conexao = sqlite3.connect('banco_biblioteca/banco_biblioteca')
    cursor = conexao.cursor()

    # Tabela Pessoa
    cursor.execute('''
                   INSERT INTO Pessoa (id_pessoa, nome, telefone, nacionalidade)
                   VALUES (1, "Ludmylla", "(94) 94002-8922", "Brasileira"),
                          (2, "Alice", "(61) 99063-4025", "Brasileira"),
                          (3, "Ana", "(62) 99302-1920", "Brasileira"),
                          (4, "Yasmin", "(91) 99012-9067", "Brasileira"),
                          (5, "Fernanda", "(21) 99002-3018", "Brasileira"),
                          (6, "J. R. R. Tolkien", "(79)2022-7575", "Britânca"),
                          (7, "J. D. Salinger", "(69) 3032-4643", "Norte-Americana"),
                          (8, "Jane Austen", "(75) 2678-9107", "Inglesa"),
                          (9, "Agatha Christie", "(88) 2621-7087", "Britânca"),
                          (10, "H. P Lovecraft", "(47) 2696-7868", "Norte-Americana"),
                          (11, "Aldous Huxley", "(69) 3695-6476", "Inglesa");
                   ''')

    # Tabela Usuario
    cursor.execute('''
                   INSERT INTO Usuario (id_usuario, nome, telefone, nacionalidade)
                   VALUES (1, "Ludmylla", "(94)94002-8922", "Brasileira"),
                          (2, "Alice", "(61)99063-4025", "Brasileira"),
                          (3, "Ana", "(62)99302-1920", "Brasileira"),
                          (4, "Yasmin", "(91)99012-9067", "Brasileira"),
                          (5, "Fernanda", "(21)99002-3018", "Brasileira");
                   ''')

    # Tabela Autor
    cursor.execute('''
                   INSERT INTO Autor (id_autor, nome, nacionalidade)
                   VALUES (1, "J. R. R. Tolkien", "Britânca"),
                          (2, "J. D. Salinger", "Norte-Americana"),
                          (3, "Jane Austen", "Inglesa"),
                          (4, "Agatha Christie", "Britânca"),
                          (5, "H. P Lovecraft", "Norte-Americana"),
                          (6, "Aldous Huxley", "Inglesa");
    ''')

    # Tabela Livro
    cursor.execute('''
                    INSERT INTO Livro (id_livro, titulo, editora)
                    VALUES (1, "O Senhor dos Anéis: A sociedade do Anel", "Martin Claret"),
                           (2, "Nove histórias", "Todavia"),
                           (3, "Emma", "Martin Claret"),
                           (4, "O Silmarillion", "Martin Claret"),
                           (5, "Um corpo na biblioteca", "Harper Collins"),
                           (6, "A cor que caiu do céu", "Pandorga Editora"),
                           (7, "Admirável Mundo Novo", "Biblioteca Azul");
    ''')

    # Tabela Genero
    cursor.execute('''
                    INSERT INTO Genero (id_genero, genero)
                    VALUES (1, "Ficção Científica"),
                           (2, "Romance"),
                           (3, "Fantasia"),
                           (4, "Ficção Policial"),
                           (5, "Horror"),
                           (6, "Conto");
    ''')

    # Tabela Livro_Genero
    cursor.execute('''
                    INSERT INTO Livro_Genero (id_livro, id_genero)
                    VALUES (1, 3), -- O Senhor dos anéis - Fantasia
                           (2, 6), -- Nove Histórias - Conto
                           (3, 2), -- Emma - Romance
                           (4, 3), -- O Silmarillion - Fantasia
                           (5, 4), -- Um corpo na Biblioteca - Ficção Policial
                           (6, 5), -- A cor que caiu do céu - Horror
                           (7, 1); -- Admirável Mundo Novo - Ficção Científica
    ''')

    # Tabela Autor_Livro
    cursor.execute('''
                    INSERT INTO Autor_Livro (id_livro, id_autor)
                    VALUES (1, 1), -- O Senhor dos anéis - J. R. R. Tolkien
                           (2, 2), -- Nove Histórias - J. D. Salinger
                           (3, 3), -- Emma - Jane Austen
                           (4, 1), -- O Silmarillion - J. R. R. Tolkien
                           (5, 4), -- Um corpo na Biblioteca - Agatha Christie
                           (6, 5), -- A cor que caiu do céu - H. P Lovecraft 
                           (7, 6); -- Admirável Mundo Novo - Aldous Huxley 
    ''')

    # Tabela ItemBiblioteca
    cursor.execute('''
                   INSERT INTO ItemBiblioteca (id, titulo, disponivel)
                    VALUES (1, "O Senhor dos Anéis: A sociedade do Anel", 2),
                           (2, "Nove histórias", 3),
                           (3, "Emma", 1),
                           (4, "O Silmarillion", 1),
                           (5, "Um corpo na biblioteca", 3),
                           (6, "A cor que caiu do céu", 1),
                           (7, "Admirável Mundo Novo", 2);
                   ''')

    # Tabela Exemplar
    cursor.execute('''
                   INSERT INTO Exemplar (id, titulo, estado, max_renovacoes, id_livro)
                   VALUES (1, "A cor que caiu do céu", "Emprestado", 2, 6),
                          (2, "A cor que caiu do céu", "Emprestado", 2, 6),
                          (3, "A cor que caiu do céu", "Emprestado", 2, 6),
                          (4, "Admirável Mundo Novo", "Devolvido", 3, 7),
                          (5, "Emma", "Devolvido", 3, 3),
                          (6, "Admirável Mundo Novo", "Emprestado", 2, 7),
                          (7, "O Silmarillion", "Devolvido", 3, 4),
                          (8, "Um corpo na biblioteca", "Devolvido", 3, 5),
                          (9, "A cor que caiu do céu", "Devolvido", 3, 6);
                   ''')

    # Tabela Empréstimo
    cursor.execute('''
                    INSERT INTO Emprestimo (id_emprestimo, data_emprestimo, data_devolucao, id_usuario, id_exemplar)
                    VALUES (1, '2024-03-10', '2024-05-06', 1, 4),
                           (2, '2024-04-15', '2024-06-02', 2, 5),
                           (3, '2024-05-23', '2024-07-10', 3, 7),
                           (4, '2024-05-23', '2024-08-15', 4, 8),
                           (5, '2024-07-23', '2024-08-23', 5, 9);
    ''')

    conexao.commit()
    conexao.close()
    pass