from utils import load_data, load_template, add_note


from utils import load_data, load_template

def index():
    note_template = load_template('components/note.html')
    # 🚀 Para cada anotação do banco, substitui {title} e {details}
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
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

