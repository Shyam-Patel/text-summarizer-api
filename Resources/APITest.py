from flask import Blueprint
from flask import jsonify

APITest_Blueprint = Blueprint('test', __name__)


@APITest_Blueprint.route("/greet", methods=['GET'])
def greet():
    return jsonify("Greetings!")
