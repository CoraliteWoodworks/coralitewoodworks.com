from flask import Flask
from flask import render_template
from Database import Kitchens, Decks, Builtins
from Database import db

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')


@app.route('/builtins', methods=['GET'], defaults={'n': 0})
@app.route('/builtins/<n>', methods=['GET'])
def builtins(n):
    row = Builtins.query.count()
    if int(n) is 0:
        description = []
        for num in range(1, row + 1):
            data = Builtins.query.filter_by(id=num).first()
            description.append(Builtins.get_description(data))
        return render_template('Gallery Directory.html', portfolio='builtins', portfolioFull='Built-ins & Bookcases',
                               row=row, description=description)
    elif int(n) >= 1:
        data = Builtins.query.filter_by(id=n).first()
        description = Builtins.get_description(data)
        gallery_id = Builtins.get_gallery_id(data)
        cpo = Builtins.get_cpo(data)
        return render_template('Gallery Basic.html', portfolio='builtins', portfolioFull='Built-ins & Bookcases',
                               description=description,
                               id=int(n),
                               gallery_id=gallery_id, cpo=cpo, row=row)


@app.route('/decks', methods=['GET'], defaults={'n': 0})
@app.route('/decks/<n>', methods=['GET'])
def decks(n):
    row = Decks.query.count()
    if int(n) is 0:
        description = []
        for num in range(1, row + 1):
            data = Decks.query.filter_by(id=num).first()
            description.append(Decks.get_description(data))
        return render_template('Gallery Directory.html', portfolio='decks', portfolioFull='Decks & Porches', row=row,
                               description=description)
    elif int(n) >= 1:
        data = Decks.query.filter_by(id=n).first()
        description = Decks.get_description(data)
        gallery_id = Decks.get_gallery_id(data)
        cpo = Decks.get_cpo(data)
        return render_template('Gallery Basic.html', portfolio='decks', portfolioFull='Decks & Porches', description=description,
                               id=int(n),
                               gallery_id=gallery_id, cpo=cpo, row=row)


@app.route('/kitchens', methods=['GET'], defaults={'n': 0})
@app.route('/kitchens/<n>', methods=['GET'])
def kitchens(n):
    row = Kitchens.query.count()
    if int(n) is 0:
        description = []
        for num in range(1, row + 1):
            data = Kitchens.query.filter_by(id=num).first()
            description.append(Kitchens.get_description(data))
        return render_template('Gallery Directory.html', portfolio='kitchens', portfolioFull='Kitchens', row=row,
                               description=description)
    elif int(n) >= 1:
        data = Kitchens.query.filter_by(id=n).first()
        description = Kitchens.get_description(data)
        gallery_id = Kitchens.get_gallery_id(data)
        cpo = Kitchens.get_cpo(data)
        return render_template('Gallery Basic.html', portfolio='kitchens', portfolioFull='Kitchens',
                               description=description, id=int(n),
                               gallery_id=gallery_id, cpo=cpo, row=row)


if __name__ == "__main__":
    db.create_all()
    app.run()
