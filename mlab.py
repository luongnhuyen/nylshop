import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds139251.mlab.com:39251/nylshop

host = "ds139251.mlab.com"
port = 39251
db_name = "nylshop"
user_name = "admin1"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
