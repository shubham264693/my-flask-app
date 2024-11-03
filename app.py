# app.py

from flask import Flask 
from urllib.parse import quote 

def create_app():
    x=10
    y=100
    z=30
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Wow CI-CD Pipeline is been developed updated Hurrayyyyy..'

    return app

def test():
    print("hi")
    test()

def sum(z,y):
    return z+y

def add(a,b):
    return a+b

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=80, debug=True)
