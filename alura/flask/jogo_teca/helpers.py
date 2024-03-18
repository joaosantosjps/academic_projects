import os 
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField, validators

class FormularioJogo(FlaskForm):
    nome = SearchField("Nome do Jogo", [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = SearchField("Categpria", [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = SearchField("Console", [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField("Salvar")

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config["UPLOAD_PATH"]):
        if f"capa{id}" in nome_arquivo:
            return nome_arquivo
    
    return "capa_padrão.jpg"

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != "capa_padrão.jpg":
        os.remove(os.path.join(app.config["UPLOAD_PATH"], arquivo))