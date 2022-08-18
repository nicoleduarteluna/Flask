from flask import Flask, render_template, request, session, redirect, url_for
app = Flask("projeto")

# Criando uma chave de criptografia
app.secret_key = "ASDPOIZXCMNBQWEPIO123@@@#%$@."

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

# Rota Login Form
@app.route("/login")
def login():
    return render_template("login.html"), 200

# Rota para validar o formulário
@app.route("/login_validar", methods=["POST"])
def login_validar():
    if request.form["usuario"] == "nicole" and request.form["senha"] == "12345":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("acesso_restrito"))
    else:
        return "Usuário/senha inválidos, digite novamente.", 200

# Rota para a área restrita

@app.route("/restrito")
def acesso_restrito():
    if session["codigo"] == 1:
        return "Bem-vindo a área restrita!!<br>Usuário: {}<br>Código: {}".format(session["usuario"], session["codigo"]), 200
    else:
        return "Acesso inválido", 200

app.run()