from flask import Flask

my_app = Flask(__name__)


@my_app.route('/')
def hello_world():
    return 'Johnny like pizza'


@my_app.route('/secret')
def hello_world():
    return 'Get outta here. Its my secret'


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000, debug=True)
