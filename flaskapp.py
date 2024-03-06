from flask import Flask
from flask import Response
flask_app = Flask('flaskapp')


@flask_app.route('/hello')
def hello_world():
    return Response(
        'Айти блог !\n'
        'Настя тумкина сайт : скандалы и расследования читать далее\n'
        'Девочка по имени Ангелина взломала Пентагон - читать далее',
        mimetype='text/plain'
    )

app = flask_app.wsgi_app