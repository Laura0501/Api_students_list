from flask import Response, Blueprint, jsonify, json, request
from service.list_de_service import ListDe
from util.util_encoder import util_encoder

app_list_de=Blueprint("app_list_de", __name__)

list_de_service=ListDe()

@app_list_de.route('/list_de/all')
def get_all_students_de():
    return Response(status=200, response=json.dumps(list_de_service.get_all_students_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/add', methods=['POST'])
def add_de():
    try:
        data = request.json
        list_de_service.add_de(data)
        return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

    except Exception as error:
        return Response(status=409, response=json.dumps({"message": str(error)}),
                        mimetype='aplication/json')

@app_list_de.route('/list_de/add_to_start', methods=['POST'])
def add_to_start_de():
    try:
        data = request.json
        list_de_service.add_to_start_de(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_de.route('/list_de/inversed')
def reversed_list_de():
    return Response(status=200, response=json.dumps(list_de_service.reversed_list_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/exchange_start_finally')
def exchange_start_finally_de():
    return Response(status=200,
                    response=json.dumps(list_de_service.exchange_start_finally_de()),
                    mimetype="application/json")
