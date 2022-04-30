from flask import Response, Blueprint, jsonify, json, request
from service.list_se_service import ListSE_service
from util.util_encoder import util_encoder

app_list_se=Blueprint("app_list_se", __name__)

list_se_service = ListSE_service()


@app_list_se.route('/list_se/all')
def get_all_students():
    return Response(status=200, response=json.dumps(list_se_service.get_all_students(), cls=util_encoder),
                    mimetype='aplication/json')

#Agregar el estudiante desde postman

@app_list_se.route('/list_se', methods=['POST'])
def save_students():
    try:
        data= request.json
        list_se_service.add(data)
        return Response(status=200, response=json.dumps({"message":"Adicionado exitosamente"}),
                    mimetype='aplication/json')

    except Exception as error:
        return Response(status=409, response=json.dumps({"message": str(error)}),
                        mimetype='aplication/json')

@app_list_se.route('/list_se/addtostart',methods=['POST'])
def add_to_start():
    try:
        data = request.json
        list_se_service.add_to_start(data)
        return Response(status=200,
                        response=json.dumps({"message": "Adicionado exitosamente"}),
                        mimetype="application/json")
    except Exception as error:
        return Response(status=409,
                        response=json.dumps({"message": str(error)}),
                        mimetype="application/json")

@app_list_se.route('/list_se/all/inversed')
def get_reversed_list():
    return Response(status=200, response=json.dumps(list_se_service.reversed_list(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_se.route('/list_se/exchange_start_finally')
def exchange_start_finally():
    return Response(status=200,
                    response=json.dumps(list_se_service.exchange_start_finally()),
                    mimetype="application/json")

@app_list_se.route('/list_se/delete_by_data/<id>')
def remove_data_id(id):
    return Response(status=200,
                    response=json.dumps(list_se_service.remove_data_id(id)),
                    mimetype="application/json")

@app_list_se.route('/list_se/remove_by_position/<position>')
def remove_by_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_service.remove_by_position(int(position))),
                    mimetype="application/json")

@app_list_se.route('/list_se/add_to_position/<position>',methods=['POST'])
def add_to_position(position):
    return Response(status=200,
                    response=json.dumps(list_se_service.add_to_position(int(position),request.json)),
                    mimetype="application/json")

@app_list_se.route('/list_se/get_womans_to_start')
def get_womans_to_start():
    return Response(status=200, response=json.dumps(list_se_service.get_womans_to_start(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_se.route('/list_se/get_list_for_genders')
def get_list_for_genders():
    return Response(status=200, response=json.dumps(list_se_service.get_list_for_genders(), cls=util_encoder),
                    mimetype='aplication/json')

@app_list_se.route('/list_se/order_for_ages_genders')
def order_for_ages_genders():
    return Response(status=200, response=json.dumps(list_se_service.order_for_ages_genders(), cls=util_encoder),
                    mimetype='aplication/json')

