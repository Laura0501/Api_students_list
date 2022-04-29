from flask import Response, Blueprint, jsonify, json
from service.student_service import StudentService
from util.util_encoder import util_encoder

#Response dominar el tipo de datos, json convertir objetos a json

app_student=Blueprint("app_student", __name__)

@app_student.route('/student/all')
def get_all_students():
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_all_students(), cls=util_encoder),
                    mimetype='application/json')

#cls antes pasando por mi util encoder, que clase se va utilizar, mimetype de json


@app_student.route('/student/percentagebygender/<gender>')
def get_percentage_students_by_gender(gender):
    student_service = StudentService()
    return str(student_service.get_percentage_students_by_gender(int(gender)))

@app_student.route('/student/per_students_job_avgsalary/<gender>')
def get_per_students_job_avgsalary(gender):
    student_service = StudentService()
    return jsonify(student_service.gender_percentage_students_avg_salary(int(gender)))

#RUTA EJERCICIO 1

@app_student.route('/student/higher_salarys/<gender>/<salary>')
def get_list_students_higher_salarys(gender, salary):
    try:
        student_service = StudentService()
        return Response(status=200, response=json.dumps(student_service.get_list_students_higher_salarys(int(gender), int(salary)),
                    cls=util_encoder) ,mimetype='aplication/json')
    except ValueError:
        return Response(status=200, response=json.dumps({"Error":"Debes ingresar números"}),
                    mimetype='aplication/json')


#RUTA EJERCICIO 2

@app_student.route('/student/man_woman_higher_salary')
def get_man_woman_higher_salary():
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.get_man_woman_higher_salary(), cls=util_encoder)
        , mimetype='aplication/json')

#RUTA EJERCICIO 3

@app_student.route('/students/salary_in_range/<range1>/<range2>')
def list_students_salary_in_range(range1, range2):
    student_service = StudentService()
    return Response(status=200, response=json.dumps(student_service.list_students_salary_in_range(int(range1), int(range2)),
                    cls=util_encoder), mimetype='aplication/json')

#RUTA EJERCICIO 4
@app_student.route('/student/avrg_salary_woman_man')
def get_avrg_salary_woman_man():
    try:
        student_service = StudentService()
        return jsonify(student_service.get_avrg_salary_woman_man())
    except ValueError:
        return Response(status=200, response=json.dumps({"Error":"Debes ingresar números"}),
                    mimetype='aplication/json')

#SUSTENTACION

#RETORNAR PROMEDIO DE EDADES

@app_student.route('/student/avrg_age_students')
def get_avrg_age_students():
    student_service=StudentService()
    return Response(status=200, response=json.dumps(student_service.get_avrg_age_students(), cls=util_encoder),
                    mimetype='aplication/json')

@app_student.route('/student/higher_age_avrg_rural')
def get_student_higher_age_avrg_rural():
    student_service=StudentService()
    return Response(status=200, response=json.dumps(student_service.get_student_higher_age_avrg_rural(), cls=util_encoder),
                    mimetype='aplication/json')


@app_student.route('/student/get_students_by_city')
def get_students_by_city():
    student_service = StudentService()
    return jsonify(student_service.get_students_by_city())
