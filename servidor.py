from flask import Flask, render_template_string, request, redirect
import views
from utils import init_db, migrate_json_to_db


app = Flask(__name__)


app.static_folder = 'static'


@app.route('/')
def index():
    return render_template_string(views.index())


@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    
    resposta, status_code = views.submit(titulo, detalhes)
    if status_code == 404:
        return render_template_string(resposta), 404  # Mostra a pagina de erro
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete_note_route(id):
    return views.delete(id)


# Rota GET para carregar a pagina de edicao da nota
@app.route('/edit/<int:note_id>', methods=['GET'])
def edit_note_route(note_id):
    nota = views.get_note_by_id(note_id)  # Busca a nota pelo ID
    return render_template_string(
        views.edit_note_page(nota['id'], nota['titulo'], nota['detalhes'])
    )

 
# Rota POST para salvar as alteracoes feitas na nota
@app.route('/update', methods=['POST'])
def update_note_route():
    note_id = request.form['id']
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']

    views.update_note(note_id, titulo, detalhes)  # Atualiza a nota
    return redirect('/')  # Redireciona para a página inicial
 
@app.errorhandler(404)
def page_not_found(error):
    return views.page_not_found()  # Chama a função que retorna o 404.html

if __name__ == '__main__':
    init_db()                # Inicializa o banco, se necessario
    migrate_json_to_db()     # Migra as anotacoes antigas
    app.run(debug=True)




