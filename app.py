from flask import Flask, render_template

import data

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html', page=data)


@app.route('/departures/<departure>/')
def render_departure(departure):
    return render_template('departure.html', departure=departure, page=data,
                            tours=list(filter(lambda x: x["departure"] == departure,
                                              data.tours.values())))


@app.route('/tours/<int:tour_id>/')
def render_tours(tour_id):
    try:
        return render_template('tour.html', tour=data.tours[tour_id], page=data)
    except KeyError:
        return "Нет такого тура!!"


@app.errorhandler(404)
def render_not_found():
    return "Ничего не нашлось! Вот неудача, отправляйтесь на главную"


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим:\n{}".format(error), 404


# Run server
if __name__ == '__main__':
    app.run()
