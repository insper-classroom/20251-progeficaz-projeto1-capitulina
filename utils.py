import json
import sqlite3
import os

def load_data():
    conn = get_db_connection()
    notes = conn.execute('SELECT id, titulo, detalhes FROM notes').fetchall()
    conn.close()
    return notes


def migrate_json_to_db():
    json_file = 'static/data/notes.json'
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            notes = json.load(file)

        conn = get_db_connection()
        for note in notes:
            conn.execute(
                'INSERT INTO notes (titulo, detalhes) VALUES (?, ?)',
                (note['titulo'], note['detalhes'])
            )
        conn.commit()
        conn.close()

        # Apos a migracao, remova o arquivo JSON para evitar duplicatas
        os.remove(json_file)
        print(f"✅{json_file} migrado com sucesso e removido.")


def load_template(temp):
    with open(f'static/templates/{temp}', 'r',encoding='utf-8') as f:
        return (f.read())


def add_note(new_note):
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO notes (titulo, detalhes) VALUES (?, ?)',
        (new_note['titulo'], new_note['detalhes'])
    )
    conn.commit()
    conn.close()

# Conexao com o banco de dados
def get_db_connection():
    conn = sqlite3.connect('static/data/notes.db')
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn


# Cria a tabela se nao existir
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            detalhes TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def delete_note(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM notes WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# 🔍 Busca a nota pelo ID
def get_note_by_id(note_id):
    conn = get_db_connection()
    note = conn.execute('SELECT * FROM notes WHERE id = ?', (note_id,)).fetchone()
    conn.close()
    return note

# 💾 Atualiza a nota no banco de dados
def update_note(note_id, titulo, detalhes):
    conn = get_db_connection()
    conn.execute(
        'UPDATE notes SET titulo = ?, detalhes = ? WHERE id = ?',
        (titulo, detalhes, note_id)
    )
    conn.commit()
    conn.close()

