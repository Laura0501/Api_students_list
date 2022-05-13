from flask import Flask, jsonify
from controller.student_controller import app_student
from controller.list_se_controller import app_list_se
from controller.list_se_circle_controller import app_list_se_circle
from controller.list_de_controller import app_list_de
from controller.list_de_circle_controller import app_list_de_circle

app = Flask(__name__)

app.register_blueprint(app_student)
app.register_blueprint(app_list_se)
app.register_blueprint(app_list_se_circle)
app.register_blueprint(app_list_de)
app.register_blueprint(app_list_de_circle)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hola Mundo!'

if __name__ == '__main__':
    app.run()
