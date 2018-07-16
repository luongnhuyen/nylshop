from flask import *
from mongoengine import *
import mlab
from random import randint, choice
from models.service import Service
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')   


@app.route('/ao')
def ao():
    return render_template('page/ao.html')

@app.route('/new-service-input', methods= ["GET", "POST"])
def new_service_input():
    if request.method == "GET":
        return render_template('new_service_input.html')
    elif request.method == "POST":
        form = request.form
        name  = form ['name']
        type = form ['type']
        price = form ['price']
        link = form ['link']
        picture = form ['picture']
        service = Service(name=name, type=type, price=price, link=link, picture=picture)
        service.save()
        all_service = Service.objects()
        return render_template('service.html',all_service=all_service)

@app.route('/service')
def service():
    all_service = Service.objects()
    return render_template('service.html',all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for('service'))
    else:
        return render_template('service.html',all_service = all_service)

if __name__ == '__main__':
  app.run(debug=True)
