from flask import Flask, jsonify
import data_parser
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

def parse_data(dataItems):
    itemList = []
    for item in dataItems:
        option = item['Option']
        price = item['Price']

        parseable_item = {
            'option': option,
            'price': price,
        }
        itemList.append(parseable_item)

    return itemList

def parse_toppings_list(dataItems):
    itemList = []
    for item in dataItems:
        option = item['Topping']
        price = item['Selected']

        parseable_item = {
            'topping': option,
            'selected': price,
        }
        itemList.append(parseable_item)

    return itemList

@app.route('/size')
def get_size():
    sizeData = data_parser.get_item_data('size.csv')
    return jsonify(parse_data(sizeData))

@app.route('/crust')
def get_crust():
    crustData = data_parser.get_item_data('crust.csv')
    return jsonify(parse_data(crustData))

@app.route('/toppings')
def get_toppings():
    toppingData = data_parser.get_item_data('toppings.csv')
    return jsonify(parse_data(toppingData))

@app.route('/toppingsList')
def get_toppings_list():
    toppingsList = data_parser.get_item_data('toppingsList.csv')
    return jsonify(parse_toppings_list(toppingsList))

if __name__ == '__main__':
    app.run()