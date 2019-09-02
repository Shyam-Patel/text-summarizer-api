from flask import Blueprint

APITest_Blueprint = Blueprint('test', __name__)

@APITest_Blueprint.route("/greet", methods=['GET'])
def greet():
    return "Greetings!"

@APITest_Blueprint.route("/compliment", methods=['GET'])
def tell():
    return "You look nice today"