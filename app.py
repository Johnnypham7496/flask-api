from flask import Flask

my_app = Flask(__name__)


@my_app.route('/')
def hello_world():
    return 'Johnny like pizza'


if __name__ == '__main__':
    my_app.run(host='localhost', port=5000, debug=True)
