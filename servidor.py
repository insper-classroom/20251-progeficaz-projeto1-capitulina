from flask import Flask, render_template_string, request, redirect
import views
from utils import init_db
from utils import init_db, migrate_json_to_db


app = Flask(__name__)


# Configurando a pasta de arquivos estaticos
app.static_folder = 'static'


@app.route('/')
def index():
    return render_template_string(views.index())


@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  # Obtem o valor do campo 'titulo'
    detalhes = request.form.get('detalhes')  # Obtem o valor do campo 'detalhes'

    views.submit(titulo, detalhes)
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete_note_route(id):
    return views.delete(id)


# 📝 Rota GET para carregar a página de edição da nota
@app.route('/edit/<int:note_id>', methods=['GET'])
def edit_note_route(note_id):
    nota = views.get_note_by_id(note_id)  # Busca a nota pelo ID
    return render_template_string(
        views.edit_note_page(nota['id'], nota['titulo'], nota['detalhes'])
    )

 
 
# 📝 Rota POST para salvar as alterações feitas na nota
@app.route('/update', methods=['POST'])
def update_note_route():
    note_id = request.form['id']
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']

    views.update_note(note_id, titulo, detalhes)  # Atualiza a nota
    return redirect('/')  # Redireciona para a página inicial
 

if __name__ == '__main__':
    init_db()                # Inicializa o banco, se necessario
    migrate_json_to_db()     # 🚀 Migra as anotacoes antigas
    app.run(debug=True)

