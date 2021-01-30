from flask import Flask, render_template
import requests

app = Flask(__name__)


def make_bold(function):
    def wrapping_f(user):
        return '<b>' + function(user)+ '</b>'
    return wrapping_f


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/username/<user>')
@make_bold
def user(user):
    return f"hello {user} <img src='https://media4.giphy.com/media/26uf43dkw9ByWsjLi/giphy.gif?cid=ecf05e47eerqhntyk88pb9xtzy2mjzl8yi9d3i8xpy0twhh7&rid=giphy.gif'/>"

@app.route('/guess/<name>')
def guess(name):
    gres = requests.get('https://api.genderize.io/?name=' + name).json()
    ares = requests.get('https://api.agify.io/?name=' + name).json()
    return render_template('guess.html', gender=gres['gender'], age=ares['age'], name=name)

if __name__ == '__main__':
    app.run()
