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
        return render_template_string(resposta), 404  
    return redirect('/')


@app.route('/delete/<int:id>', methods=['POST'])
def delete_note_route(id):
    return views.delete(id)



@app.route('/edit/<int:note_id>', methods=['GET'])
def edit_note_route(note_id):
    nota = views.get_note_by_id(note_id)  
    return render_template_string(
        views.edit_note_page(nota['id'], nota['titulo'], nota['detalhes'])
    )


@app.route('/update', methods=['POST'])
def update_note_route():
    note_id = request.form['id']
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']

    views.update_note(note_id, titulo, detalhes) 
    return redirect('/')  
 
@app.errorhandler(404)
def page_not_found(error):
    return views.page_not_found()  

if __name__ == '__main__':
    init_db()                
    migrate_json_to_db()     
    app.run(debug=True)




