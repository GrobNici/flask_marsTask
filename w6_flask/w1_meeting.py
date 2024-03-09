from flask import Flask

app = Flask(__name__)


@app.route('/')
def mission():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/promotion')
def promoting():
    promote = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
             "Мы сделаем обитаемыми безжизненные пока планеты.",
             'И начнем с Марса!', 'Присоединяйся!']
    return '<br>'.join(promote)


@app.route('/index')
def index_message():
    return 'И на Марсе будут яблони цвести!'


@app.route("/image_mars")
def image_mars():
    TEMPLATE = """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1>Жди нас, Марс!</h1>
        <img src="static/img/mars.png" alt="Фото Марса украли инопланетяне" 
        height=500 width=500>
        <br>Вот она какая, красная планета.
    </body>
</html>"""
    return TEMPLATE


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')