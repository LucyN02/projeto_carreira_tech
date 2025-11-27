from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre_equipe')
def sobre_equipe():
    return render_template('sobre_equipe.html')

@app.route('/carreiras/backend')
def carreira_backend():
    return render_template('back_end.html')

@app.route('/carreiras/frontend')
def carreira_frontend():
    return render_template('front_end.html')

@app.route('/carreiras/dados')
def carreira_dados():
    return render_template('dados.html')

@app.route("/gemini", methods=["GET", "POST"])
def gemini_page():
    client = genai.Client(api_key='AIzaSyDf_doDoxjDyeGrC-0ralSxUyRtfHTtbuQ')
    render_template('gemini.html')

    if request.method == "POST":
        pergunta = request.form["pergunta"]

        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=pergunta)

    return render_template("gemini.html", resposta=response.text)


# client = genai.Client(api_key='AIzaSyDf_doDoxjDyeGrC-0ralSxUyRtfHTtbuQ')
#
# user_message = input("Qual a sua pergunta?: ")
#
# prompt = f"""Voce é um professor de programacao experiente e didatico.
# sua missao é ajudar estudantes a aprender a programacao de frma clara e objetiva.
#
#        pergunta do aluno:{user_message}
#
# forneça uma resposta educativa, com exemplos praticos quando relevante."""
#
# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents=prompt
# )
#
# print(response.text)

app.run()

