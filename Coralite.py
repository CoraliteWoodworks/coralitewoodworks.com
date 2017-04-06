from flask import render_template
from Database import *

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


@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')


@app.route('/additions', methods=['GET'], defaults={'n': 0})
@app.route('/additions/<n>', methods=['GET'])
def additions(n):
    return show(n, Additions, 'additions', 'Additions & Renovations')


@app.route('/bars', methods=['GET'], defaults={'n': 0})
@app.route('/bars/<n>', methods=['GET'])
def bars(n):
    return show(n, Bars, 'bars', 'Bars & Wine Storage')


@app.route('/basements', methods=['GET'], defaults={'n': 0})
@app.route('/basements/<n>', methods=['GET'])
def basements(n):
    return show(n, Basements, 'basements', 'Basements')


@app.route('/bathrooms', methods=['GET'], defaults={'n': 0})
@app.route('/bathrooms/<n>', methods=['GET'])
def bathrooms(n):
    return show(n, Bathrooms, 'bathrooms', 'Bathrooms & Vanities')


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


@app.route('/mantels', methods=['GET'], defaults={'n': 0})
@app.route('/mantels/<n>', methods=['GET'])
def mantels(n):
    return show(n, Mantels, 'mantels', 'Mantels')


@app.route('/mudrooms', methods=['GET'], defaults={'n': 0})
@app.route('/mudrooms/<n>', methods=['GET'])
def mudrooms(n):
    return show(n, Mudrooms, 'mudrooms', 'Mudrooms & Closets')


@app.route('/offices', methods=['GET'], defaults={'n': 0})
@app.route('/offices/<n>', methods=['GET'])
def offices(n):
    return show(n, Offices, 'offices', 'Desks & Offices')


@app.route('/paneling', methods=['GET'], defaults={'n': 0})
@app.route('/paneling/<n>', methods=['GET'])
def paneling(n):
    return show(n, Paneling, 'paneling', 'Paneling & Wainscoting')


@app.route('/stock', methods=['GET'], defaults={'n': 0})
@app.route('/stock/<n>', methods=['GET'])
def stock(n):
    return show(n, Stock, 'stock', 'Stock Cabinets')


@app.route('/tv', methods=['GET'], defaults={'n': 0})
@app.route('/tv/<n>', methods=['GET'])
def tv(n):
    return show(n, TV, 'tv', 'TV Entertainment Centers')


if __name__ == "__main__":
    db.create_all()
    app.run()
