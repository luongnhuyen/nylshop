from flask import *
from mongoengine import *
import mlab
from random import randint, choice
from models.service import Service
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ao')
def ao():
    return render_template('items/ao.html')

if __name__ == '__main__':
  app.run(debug=True)
