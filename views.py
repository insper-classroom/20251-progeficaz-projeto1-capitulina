from utils import load_data, load_template, add_note, delete_note, get_note_by_id, update_note
from flask import redirect

def index():
    note_template = load_template('components/note.html')
    # 🚀 Para cada anotação do banco, substitui {title} e {details}
    notes_li = [
        note_template.format(id=dados['id'], title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)  # Junta todas as anotações em uma string HTML

    # 🚀 Insere a string de anotações dentro do index.html
    return load_template('index.html').format(notes=notes)


def submit(titulo, detalhes):
    if not titulo or not detalhes:
        return "Erro: título e detalhes são obrigatórios", 400
    
    add_note({"titulo": titulo, "detalhes": detalhes})
    return "Anotação adicionada com sucesso!", 200

def delete(id):
    delete_note(id)
    return redirect('/')

def edit_note_page(note_id, titulo, detalhes):
    template = load_template('edit_note.html')
    return template.format(id=note_id, titulo=titulo, detalhes=detalhes)






