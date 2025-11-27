@app.route("/gemini", methods=["GET", "POST"])
def gemini_page():
    resposta = None

    if request.method == "POST":
        pergunta = request.form["pergunta"]

        modelo = genai.GenerativeModel("gemini-1.5-flash")
        resposta = modelo.generate_content(pergunta).text

    return render_template("gemini.html", resposta=resposta)
