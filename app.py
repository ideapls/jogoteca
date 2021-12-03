from flask import Flask, render_template, request, redirect

#  O Jinja2 é o motor de templates do Flask

"""Se eu quiser usar a porta 8080 para aplicação ou até mesmo permitir acessos externos à 
aplicação definindo o host como 0.0.0.0 devo setar a configuração abaixo"""

#  trecho da app
#  app.run(host='0.0.0.0', port=8080)

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Super Mario', 'Aventura', 'SNES')
jogo2 = Jogo('Pokémon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'Xbox/PC/PS')
lista = [jogo1, jogo2, jogo3]


@app.route('/')
def index():  # put application's code here
    return render_template('lista.html', titulo='Jogos',
                           jogos=lista)


@app.route('/novo')
def new():
    return render_template('novo.html', titulo='Novo jogo')


@app.route('/criar', methods=['POST', ])
def create():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
