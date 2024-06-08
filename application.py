from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    print('Enter your name:')
    x = input()
    print('Hello, ' + x) 