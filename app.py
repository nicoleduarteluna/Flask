from flask import Flask, render_template, request
app = Flask("projeto")

@app.route ("/")
def ola_mundo ():
    # return "Olá mundo! Esse é meu primeiro projeto Flask!!", 200
    nome = "Nicole Duarte Luna"
    produtos = [
        {
            "nome": "Ração",
            "preco": "15,00"
        },
        {
            "nome": "Playstation",
            "preco": "4.999,99"
        }
    ]
    return render_template("alo.html", n = nome, aProdutos = produtos), 200


# Nova Rota Teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel):
    return "Nova rota teste <br> Variável: {}".format(variavel), 200

# Rota formulário
@app.route("/form")
def form():
    return render_template("form.html"), 200

# Rota tratamento do formulário
@app.route("/form_recebe", methods = ["GET", "POST"])
def form_recebe():
    name = ""
    if request.method == "POST":
        name = request.form["nome"]
        return "Nome: {}".format(name), 200
    else:
        return "Não pode chamar direto no GET!", 200

app.run()