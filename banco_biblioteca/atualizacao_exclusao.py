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
