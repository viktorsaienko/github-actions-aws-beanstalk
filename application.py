from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from z53rb65y Elastic Beanstalk CI-CD verification-202609221009507514"
