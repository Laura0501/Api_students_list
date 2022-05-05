from flask import Response, Blueprint, jsonify, json, request
from service.list_de_circle_service import ListDeCircleService
from util.util_encoder import util_encoder

app_list_de_circle=Blueprint("app_list_se_circle", __name__)

list_de_circle_service=ListDeCircleService()

@app_list_de_circle.route('/list_se_circle/all')
def get_all_students_circle_de():
    return Response(status=200, response=json.dumps(list_de_circle_service.get_all_students_circle_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de_circle.route('/list_se_circle_add', methods=['POST'])
def add_circle_de():
    try:
        data= request.json
        list_de_circle_service.add_circle_de(data)
        return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

    except Exception as error:
        return Response(status=409, response=json.dumps({"message": str(error)}),
                        mimetype='aplication/json')

@app_list_de_circle.route('/list_se_circle/addtostart',methods=['POST'])
def add_to_start_de_circle():
    try:
        data = request.json
        list_de_circle_service.add_to_start_de_circle(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de_circle.route('/list_se_circle/count')
def count():
    return Response(status=409, response=json.dumps(list_de_circle_service.count_de_circle(), cls=util_encoder),
                        mimetype='aplication/json')