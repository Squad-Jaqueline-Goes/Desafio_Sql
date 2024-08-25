import sqlite3
import criacao_tabelas

def inserir_dados():
    #conexao
    conexao = sqlite3.connect('banco_biblioteca.db')
    cursor = conexao.cursor()
    
    #inserção de dados
    #pessoa
    pessoas = [
        ("Selma Maia Marica", 6635628737, "Brasileira"), 
        ("Sarah Graley", 1111111111, "Britânica"), 
        ("Chimamanda Ngozi Adichie", 1112345678, "Nigeriana"),
        ("Simone de Beauvoir", 2223455678, "Francesa"), 
        ("Carlos Silva", 2199887766, "Brasileiro"),
        ("Maria Fernandez", 3434567890, "Espanhola"), 
        ("Liam O'Connor", 3531234567, "Irlandês"), 
        ("Giovanni Rossi", 3944445555, "Italiano"), 
        ("Aiko Tanaka", 817891234, "Japonesa"), 
        ("Hans Müller", 4933332222, "Alemão"),
        ("Zhang Wei", 8655556666, "Chinês"),
        ("Amélie Dubois", 3377778888, "Francesa"), 
        ("Carolina Maria de Jesus", 1111111111, "Brasileira"), 
        ("Clarice Lispector", 1111111111, "Brasileira"), 
        ("Patricia Melo", 1111111111, "Brasileira"), 
        ("Lygia Fagundes Telles", 1111111111, "Brasileira"), 
        ("Margaret Atwood", 1111111111, "Canadense"), 
        ("Conceição Evaristo", 1111111111, "Brasileira")
    ]
    cursor.executemany('INSERT INTO Pessoa(nome, telefone, nacionalidade) VALUES (?, ?, ?)', pessoas)
    
    #usuario
    usuarios = [
        ("Selma Maia Marica", 6635628737, "Brasileira"),
        ("Carlos Silva", 2199887766, "Brasileiro"),
        ("Maria Fernandez", 3434567890, "Espanhola"),
        ("Liam O'Connor", 3531234567, "Irlandês"),
        ("Giovanni Rossi", 3944445555, "Italiano"),
        ("Aiko Tanaka", 817891234, "Japonesa"),
        ("Hans Müller", 4933332222, "Alemão"),
        ("Zhang Wei", 8655556666, "Chinês"),
        ("Amélie Dubois", 3377778888, "Francesa")
    ]
    cursor.executemany('INSERT INTO Usuario(nome, telefone, nacionalidade) VALUES (?, ?, ?)', usuarios)
    
    #autor
    autores = [
        ("Carolina Maria de Jesus", "Brasileira"),
        ("Clarice Lispector", "Brasileira"),
        ("Patricia Melo", "Brasileira"),
        ("Lygia Fagundes Telles", "Brasileira"),
        ("Margaret Atwood", "Canadense"),
        ("Conceição Evaristo", "Brasileira"),
        ("Sarah Graley", 1111111111, "Britânica"), 
        ("Chimamanda Ngozi Adichie", 1112345678, "Nigeriana"),
        ("Simone de Beauvoir", 2223455678, "Francesa"),
    ]
    cursor.executemany('INSERT INTO Autor(nome, nacionalidade) VALUES (?, ?)', autores)
    
    #livro
    livros = [
        ("A Hora de Estrela", "Livraria José Olympio Editora"),
        ("O Conto da Aia", "Editora Rocco"),
        ("Inferno", "Editora Rocco"),
        ("Hibisco Roxo", "Companhia das Letras"),
        ("Kim Reaper - Grim Beginnings","OniPress"),
        ("O Matador", "Editora Rocco"),
        ("As Meninas", "Companhia das Letras"),
        ("Quarto de Despejo","Francisco Alves"),
        ("Poemas da Recordação e outros movimentos", "Malê Editora"),
        (10, "O Segundo Sexo","Nova Fronteira")
    ]
    cursor.executemany('INSERT INTO Livro (titulo, editora) VALUES (?, ?)', livros)
    
    #genero
    generos = [
        ("Conto"), 
        ("Distopia"), 
        ("Ficção"), 
        ("Romance"), 
        ("Mistério"), 
        ("Aventura"), 
        ("Drama"),
        ("Bioagrafia"),
        ("Poesia"),
        ("Filosofia")
    ]
    cursor.executemany('INSERT INTO Genero(genero) VALUES (?)', generos)
    
    #livro_genero
    livro_genero = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10)
    ]
    cursor.executemany('INSERT INTO Livro_Genero(id_livro, id_genero) VALUES (?, ?)', livro_genero)
    
    #autor_livro
    autor_livro = [
        (1,2),
        (2,5),
        (3,3),
        (4,8),
        (5,7),
        (6,3),
        (7,4),
        (8,1),
        (9,6),
        (10,9)
    ]
    cursor.executemany('INSERT INTO Autor_Livro(id_livro, id_autor) VALUES (?, ?)', autor_livro)
    
    #ItemBiblioteca
    itens = [
        ("A Hora de Estrela", 1), #1 disponivel, 0 indisponivel
        ("O Conto da Aia", 1),
        ("Inferno", 0),
        ("Hibisco Roxo", 0),
        ("Kim Reaper - Grim Beginnings",0),
        ("O Matador", 1),
        ("As Meninas", 1),
        ("Quarto de Despejo",1),
        ("Poemas da Recordação e outros movimentos", 0),
        ("O Segundo Sexo", 0)
    ]
    cursor.executemany('INSERT INTO ItemBiblioteca(titulo, disponivel) VALUES (?, ?)', itens)
    
    #Exemplar - num max renovação = 3
    exemplares = [
        ("A Hora de Estrela", "Disponível", 0, 1),
        ("O Conto da Aia", "Disponível", 0, 2),
        ("Inferno", "Indisponível", 2, 3),
        ("Hibisco Roxo", "Indisponível", 1, 4),
        ("Kim Reaper - Grim Beginnings", "Indisponível", 3, 5),
        ("O Matador", "Disponível", 0, 6),
        ("As Meninas", "Disponível", 0, 7),
        ("Quarto de Despejo","Disponível", 0, 8),
        ("Poemas da Recordação e outros movimentos", "Indisponível", 1, 9),
        ("O Segundo Sexo", "Indisponível", 1, 10)
    ]
    cursor.executemany('INSERT INTO Exemplar(titulo, estado, max_renovacoes, id_livro) VALUES (?, ?, ?, ?, ?)', exemplares)
    
    #Empréstimo
    emprestimos = [
        ("2024-08-05", "2024-08-19", 1, 1), # livro 1 - usuario 1
        ("2024-07-15", "2024-07-29", 2, 2), # livro 2 usuario 2
        ("2024-06-25", "2024-07-09", 3, 3), # livro 3 usuario 3
        ("2024-05-20", "2024-06-03", 4, 4), # livro 4 usuario 4
        ("2024-04-05", "2024-04-19", 5, 5)# livro 5 usuario 5
    ]
    cursor.executemany('INSERT INTO Exemplar(data_emprestimo, data_devolucao, id_usuario, id_exemplar) VALUES (?, ?, ?, ?)', emprestimos)
    
    #comando parar enviar as informações para o bd
    conexao.commit()
    #fechando a conexao
    conexao.close
    
#chamando a função
inserir_dados()