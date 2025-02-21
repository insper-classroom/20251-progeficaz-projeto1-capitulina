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


if __name__ == '__main__':
    init_db()                # Inicializa o banco, se necessario
    migrate_json_to_db()     # 🚀 Migra as anotacoes antigas
    app.run(debug=True)
