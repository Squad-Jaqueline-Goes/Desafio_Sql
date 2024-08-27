import sqlite3

def marcar_como_devolvido(conn, emprestimo_id, exemplar_id):
    # Atualiza o estado do exemplar para 'disponível'
    query_exemplar = "UPDATE Exemplares SET estado = 'disponível' WHERE id = ?"
    conn.execute(query_exemplar, (exemplar_id,))
    
    # Atualiza o empréstimo para incluir a data de devolução
    query_emprestimo = "UPDATE Emprestimos SET data_devolucao = DATE('now') WHERE id = ?"
    conn.execute(query_emprestimo, (emprestimo_id,))
    
    conn.commit()

#Remove um autor do banco de dados
def remover_autor(conn, autor_id):
    query = "DELETE FROM Autores WHERE id = ?"
    conn.execute(query, (autor_id,))
    conn.commit()

#Remover um livro do banco de dados
def remover_livro(conn, livro_id):
    query = "DELETE FROM Livros WHERE id = ?"
    conn.execute(query, (livro_id))
    conn.commit()
    
#Atualizar informações do usuario
def atualizar_usuario(conn, usuario_id, novo_nome, novo_email):
    query = "UPDATE Usuario SET nome = ?, email = ? WHERE id_usuario = ?"
    conn.execute(query, (novo_nome, novo_email, usuario_id))
    conn.commit()
    
#Atualizar informações do autor
def atualizar_autor(conn, autor_id, novo_nome=None, nova_nacionalidade=None):
    if novo_nome is not None:
        query = "UPDATE Autor SET nome = ? WHERE id_autor = ?"
        conn.execute(query, (novo_nome, autor_id))
    if nova_nacionalidade is not None:
        query = "UPDATE Autor SET nacionalidade = ? WHERE id_autor = ?"
        conn.execute(query, (nova_nacionalidade, autor_id))
    conn.commit()
    
#Remover emprestimo
def remover_emprestimo(conn, emprestimo_id):
    query = "DELETE FROM Emprestimo WHERE id_emprestimo = ?"
    conn.execute(query, (emprestimo_id,))
    conn.commit()


