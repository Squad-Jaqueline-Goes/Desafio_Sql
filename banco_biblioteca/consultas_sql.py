import sqlite3

#Lista todos os livros disponiveis
def listar_livros_disponiveis(conn):
    query = "SELECT * FROM Livros WHERE id IN (SELECT livro_id FROM Exemplares WHERE estado = 'disponível')"
    return conn.execute(query).fetchall()

#Encontra todos os livros emprestados no momento
def listar_livros_emprestados(conn):
    query = "SELECT * FROM Livros WHERE id IN (SELECT livro_id FROM Exemplares WHERE estado = 'emprestado')"
    return conn.execute(query).fetchall()

#Localiza os livros escritos por um autor específico:
def livros_por_autor(conn, nome_autor):
    query = """
        SELECT l.* FROM Livros l
        JOIN Livro_Autores la ON l.id = la.livro_id
        JOIN Autores a ON la.autor_id = a.id
        WHERE a.nome = ?
    """
    return conn.execute(query, (nome_autor,)).fetchall()


#Verifica o número de cópias disponíveis de um determinado livro.
def copias_disponiveis(conn, titulo_livro):
    query = """
        SELECT COUNT(*) FROM Exemplares e
        JOIN Livros l ON e.livro_id = l.id
        WHERE l.titulo = ? AND e.estado = 'disponível'
    """
    return conn.execute(query, (titulo_livro,)).fetchone()[0]

#Mostra os empréstimos em atraso.
def emprestimos_atrasados(conn):
    query = """
        SELECT e.*, u.nome FROM Emprestimos e
        JOIN Usuarios u ON e.usuario_id = u.id
        WHERE e.data_devolucao < DATE('now') AND e.estado = 'emprestado'
    """
    return conn.execute(query).fetchall()
