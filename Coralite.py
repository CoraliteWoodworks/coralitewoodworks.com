from flask import Flask
from flask import render_template
from Database import Additions, Basements, Builtins, Decks, Kitchens
from Database import db

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')


def show(n, Class, portfolio, portfolio_full):
    row = Class.query.count()
    if int(n) is 0:
        description = []
        for num in range(1, row + 1):
            data = Class.query.filter_by(id=num).first()
            description.append(Class.get_description(data))
        return render_template('Gallery Directory.html', portfolio=portfolio, portfolioFull=portfolio_full,
                               row=row, description=description)
    elif int(n) >= 1:
        data = Class.query.filter_by(id=n).first()
        description = Class.get_description(data)
        gallery_id = Class.get_gallery_id(data)
        cpo = Class.get_cpo(data)
        return render_template('Gallery Basic.html', portfolio=portfolio, portfolioFull=portfolio_full,
                               description=description,
                               id=int(n),
                               gallery_id=gallery_id, cpo=cpo, row=row)


@app.route('/additions', methods=['GET'], defaults={'n': 0})
@app.route('/additions/<n>', methods=['GET'])
def additions(n):
    return show(n, Additions, 'additions', 'Additions & Renovations')


@app.route('/basements', methods=['GET'], defaults={'n': 0})
@app.route('/basements/<n>', methods=['GET'])
def basements(n):
    return show(n, Basements, 'basements', 'Basements')


@app.route('/builtins', methods=['GET'], defaults={'n': 0})
@app.route('/builtins/<n>', methods=['GET'])
def builtins(n):
    return show(n, Builtins, 'builtins', 'Built-ins & Bookcases')


@app.route('/decks', methods=['GET'], defaults={'n': 0})
@app.route('/decks/<n>', methods=['GET'])
def decks(n):
    return show(n, Decks, 'decks', 'Decks & Porches')


@app.route('/kitchens', methods=['GET'], defaults={'n': 0})
@app.route('/kitchens/<n>', methods=['GET'])
def kitchens(n):
    return show(n, Kitchens, 'kitchens', 'Kitchens')


if __name__ == "__main__":
    db.create_all()
    app.run()
