from flask import Flask
from Resources.APITest import APITest_Blueprint

app = Flask(__name__)
app.register_blueprint(APITest_Blueprint, url_prefix="/apitest")

app.run()

