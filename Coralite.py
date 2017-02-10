from flask import Flask
from flask import render_template
from Database import Kitchen

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def main():
    return render_template('index.html')


@app.route('/kitchens', methods=['GET'], defaults={'n': 0})
@app.route('/kitchens/<n>', methods=['GET'])
def kitchens(n):
    row = Kitchen.query.count()
    if int(n) is 0:
        description = []
        for num in range(1, row+1):
            data = Kitchen.query.filter_by(id=num).first()
            description.append(Kitchen.get_description(data))
        return render_template('Gallery Directory.html', portfolio='Kitchens', row=row, description=description)
    elif int(n) >= 1:
        data = Kitchen.query.filter_by(id=n).first()
        description = Kitchen.get_description(data)
        galleryId = Kitchen.get_galleryId(data)
        cpo = Kitchen.get_cpo(data)
        return render_template('Gallery Basic.html', portfolio='Kitchens', description=description, id=int(n),
                               galleryId=galleryId, cpo=cpo, row=row)


if __name__ == "__main__":
    app.run()
