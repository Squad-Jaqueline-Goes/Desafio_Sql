import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('banco_biblioteca.db')
    cursor = conexao.cursor()

    # Tabela Pessoa
    cursor.execute('CREATE TABLE IF NOT EXISTS Pessoa '
                   '(nome TEXT NOT NULL,'
                   ' telefone INTEGER NOT NULL'
                   ', nacionalidade TEXT NOT NULL)')

    # Tabela Usuario
    cursor.execute('CREATE TABLE IF NOT EXISTS Usuario '
                   '(nome TEXT NOT NULL,'
                   ' telefone INTEGER NOT NULL,'
                   ' nacionalidade TEXT NOT NULL)')

    # Tabela Autor
    cursor.execute('CREATE TABLE IF NOT EXISTS Autor '
                   '(nome TEXT NOT NULL,'
                   ' nacionalidade TEXT NOT NULL)')

    # Tabela Livro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Livro (
            id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(100) NOT NULL,
            editora VARCHAR(100) NOT NULL,
            num_maximo_renovacoes INTEGER DEFAULT 3
        );
    ''')

    # Tabela Genero
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Genero (
            id_genero INTEGER PRIMARY KEY AUTOINCREMENT,
            genero VARCHAR(100) NOT NULL
        );
    ''')

    # Tabela Livro_Genero
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Livro_Genero (
            id_livro INTEGER NOT NULL,
            id_genero INTEGER NOT NULL,
            PRIMARY KEY (id_livro, id_genero),
            FOREIGN KEY (id_livro) REFERENCES Livro(id_livro),
            FOREIGN KEY (id_genero) REFERENCES Genero(id_genero)
        );
    ''')

    # Tabela Autor_Livro
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Autor_Livro (
            id_livro INTEGER NOT NULL,
            id_autor INTEGER NOT NULL,
            PRIMARY KEY (id_livro, id_autor),
            FOREIGN KEY (id_livro) REFERENCES Livro(id_livro),
            FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
        );
    ''')

    # Tabela ItemBiblioteca
    cursor.execute('CREATE TABLE IF NOT EXISTS item_biblioteca '
                   '(id INTEGER PRIMARY KEY,'
                   ' titulo TEXT NOT NULL,'
                   ' disponivel INTEGER NOT NULL)')

    # Tabela Exemplar
    cursor.execute('CREATE TABLE IF NOT EXISTS Exemplar '
                   '(id INTEGER PRIMARY KEY,'
                   ' titulo TEXT NOT NULL,'
                   ' estado TEXT NOT NULL,'
                   ' max_renovacoes INTEGER NOT NULL)')

    # Tabela Empréstimo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Emprestimo (
            id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
            data_emprestimo DATE NOT NULL,
            data_devolucao DATE NOT NULL,
            id_usuario INTEGER NOT NULL,
            id_exemplar INTEGER NOT NULL,
            FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
            FOREIGN KEY (id_exemplar) REFERENCES Exemplar(id_exemplar)
        );
    ''')

    conexao.commit()
    conexao.close()