from flask import Response, Blueprint, jsonify, json, request
from service.list_de_service import ListDeService
from util.util_encoder import util_encoder

app_list_de=Blueprint("app_list_de", __name__)

list_de_service=ListDeService()

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
    list_de_service.reversed_list_de()
    return Response(status=200, response=json.dumps(list_de_service.get_all_students_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/exchange_start_finally')
def exchange_start_finally_de():
    return Response(status=200,
                    response=json.dumps(list_de_service.exchange_start_finally_de()),
                    mimetype="application/json")

@app_list_de.route('/list_de/delete_by_data/<id>')
def remove_data_id(id):
    return Response(status=200,
                    response=json.dumps(list_de_service.remove_data_id_de(id)),
                    mimetype="application/json")

@app_list_de.route('/list_de/remove_by_position/<position>')
def remove_by_position_de(position):
    return Response(status=200,
                    response=json.dumps(list_de_service.remove_by_position_de(int(position))),
                    mimetype="application/json")

@app_list_de.route('/list_de/add_to_position/<position>',methods=['POST'])
def add_to_position_de(position):
    return Response(status=200,
                    response=json.dumps(list_de_service.add_to_position_de(int(position),request.json)),
                    mimetype="application/json")

@app_list_de.route('/list_de/get_womans_to_start')
def get_womans_to_start():
    return Response(status=200, response=json.dumps(list_de_service.get_womans_to_start_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/get_list_for_genders')
def get_list_for_genders():
    return Response(status=200, response=json.dumps(list_de_service.get_list_for_genders_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/order_for_ages_genders')
def order_for_ages_genders():
    return Response(status=200, response=json.dumps(list_de_service.order_for_ages_genders_de(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_de.route('/list_de/kamikaze/<position>')
def kamikaze(position):
    return Response(status=200,
                    response=json.dumps(list_de_service.kamikaze(int(position))),
                    mimetype="application/json")
