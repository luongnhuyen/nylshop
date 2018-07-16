from flask import *
from mongoengine import *
import mlab
from random import randint, choice
from models.service import Service
app = Flask(__name__)

mlab.connect()

@app.route('/')
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        all_food = Service.objects(type = "food",price__lte = food*1000000/90).limit(6)

        all_book = Service.objects(type = "book",price__lte = n2*1000000).limit(6)
        all_luxury = Service.objects(type = "luxury",price__lte = n3*1000000).limit(6)
        all_charity = Service.objects(type = "charity",price__lte = n4*1000000).limit(6)
        all_invest = Service.objects(type = "invest",price__lte = n5*1000000).limit(6)
        count_food = len(all_food)
        count_book = len(all_book)
        count_luxury = len(all_luxury)
        count_charity = len(all_charity)
        count_invest = len(all_invest)
        return render_template('spending.html',
                                food = food,
                                go = go,
                                life =life,
                                other =other,
                                book = book,
                                training = training,
                                all_food = all_food,
                                all_book = all_book,
                                all_luxury = all_luxury,
                                all_charity = all_charity,
                                all_invest = all_invest,
                                count_food = count_food,
                                count_book = count_book,
                                count_luxury = count_luxury,
                                count_charity = count_charity,
                                count_invest = count_invest
                                )    


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
