from model.student import Student


class StudentService:
    students=[]
    cities=["Manizales","Pereira", "Chinchina", "Armenia"]

    def __init__(self):
        self.students=[]

        self.students.append(Student({"identification": "234567456", "gender": 2,"salary": 2036573,
                                      "job": True, "name":"Manuela Tabares","age": 19, "zone":"Urbana",
                                      "city":self.cities[2]}))

        self.students.append(Student({"identification": "1053802424", "gender": 1,"salary": 1036573,
                                      "job": True, "name":"Felipe Alvaran","age": 28, "zone":"Rural",
                                      "city":self.cities[3]}))

        self.students.append(Student({"identification": "1053807435","gender": 1,"salary": 3540899,
                                      "job": True, "name":"Camilo Villegas","age": 26, "zone":"Urbana",
                                      "city":self.cities[0]}))

        self.students.append(Student({"identification": "30318536","gender": 2,"salary": 1358900,
                                      "job": True, "name":"Gloria Cuellar","age": 35, "zone":"Rural",
                                      "city":self.cities[0]}))


    def get_all_students(self):
        return self.students


    def get_percentage_students_by_gender(self,gender):
        if gender>2 or gender<=0:
            return {"Error":"El genero ingresado no existe, 1=Hombres, 2=Mujeres"}

        counts = 0
        for student in self.students:
            if student.gender == gender:
                counts = counts+1
        return {"El porcentaje del genero solicitado es ": counts/len(self.students)}


    def gender_percentage_students_avg_salary(self,gender):
        counts_persons_work=0
        sum_salary=0
        for student in self.students:
            if student.job == True and student.gender == gender:
                    counts_persons_work = counts_persons_work+1
                    sum_salary= sum_salary + student.salary

        if counts_persons_work>0:
            return  {"Salario Promedio": sum_salary/counts_persons_work,
                    "La cantidad de personas del genero ": counts_persons_work ,
                     "% trabajan": counts_persons_work/len(self.students)}

        else:
            return {"Error":"La consulta no genero resultados"}

#EJERCICIO 1

    def get_list_students_higher_salarys(self,gender, salary):
        list_students=[]
        students=0
        for student in self.students:
            if student.job==True and student.gender==gender:
                if student.salary>salary:
                    students=students+1
                    list_students.append(student)

        if students>0:
            return list_students

        else:
            return {"Error":"Ningun estudiante cumple las condiciones"}


#EJERCICIO 2
    def get_man_woman_higher_salary(self):
        man={}
        woman={}
        higher_salary_man=0
        higher_salary_woman=0
        for student in self.students:
            if student.gender==1 and student.salary>higher_salary_man:
                higher_salary_man=student.salary
                man=student

            if student.gender==2 and student.salary>higher_salary_woman:
                higher_salary_woman=student.salary
                woman=student

        if higher_salary_woman>0 and higher_salary_man>0:
            return {"la mujer con mayor salario es":woman, "El hombre con mayor salario es":man}

        if higher_salary_woman<=0 and higher_salary_man>0:
            return {"Error":"No se encontro mujer que trabaje","El hombre con mayor salario es":man}

        if higher_salary_man<=0 and higher_salary_woman>0:
            return {"Error":"No se encontro hombre que trabaje","la mujer con mayor salario es":woman }

        if higher_salary_woman<=0 and higher_salary_man<=0:
            return {"Error":"No se encontro hombre y mujer que trabajen"}

#EJERCICIO 3

    def list_students_salary_in_range(self, range1, range2):

        if range2>range1:
            return {"Error": "El rango 1 debe ser mayor al rango 2"}

        list_students_salary_range=[]
        students=0

        for student in self.students:
            if student.salary<=range1 and student.salary>=range2:
                list_students_salary_range.append(student)
                students=students+1

        if students>0:
            return list_students_salary_range

        else:
            return {"Error": "No se encontraron estudiantes en el rango solicitado"}

#EJERCICIO 4

    def get_avrg_salary_woman_man(self):
        amount_man=0
        amount_woman=0
        salarys_man=0
        salarys_woman=0
        for student in self.students:
            if student.job== True and student.gender==1:
                amount_man=amount_man+1
                salarys_man=salarys_man+student.salary

            if student.job==True and student.gender==2:
                amount_woman=amount_woman+1
                salarys_woman=salarys_woman+student.salary

        if amount_man>0 and amount_woman>0:
            return {"El promedio salarial de mujeres es": salarys_woman/amount_woman,
                    "El promedio salarial de hombres es": salarys_man/amount_man}

        if amount_man<=0 and amount_woman>0:
            return {"Error": "No se encontraron hombres que trabajen",
                    "El promedio salarial de mujeres es": salarys_woman/amount_woman }

        if amount_woman<=0 and amount_man>0:
            return {"Error": "No se encontraron mujeres que trabajen",
                    "El promedio salarial de hombres es": salarys_man/amount_man}

        if amount_man<=0 and amount_woman<=0:
            return {"No hay resultados": "No se encontraron hombres y mujeres que trabajen"}

#SUSTENTACION

#EDAD PROMEDIO

    def get_avrg_age_students(self):
        suma_edades=0
        for student in self.students:
            suma_edades=suma_edades+student.age

        return  suma_edades/len(self.students)

#ESTUDIANTES CON MAYOR EDAD AL PROMEDIO Y ESTA EN ZONA RURAL

    def get_student_higher_age_avrg_rural(self):
        promedio=self.get_avrg_age_students()
        list_students=[]
        count_student=0
        for student in self.students:
            if student.zone=="Rural" and student.age>promedio:
                count_student=count_student+1
                list_students.append(student)

        if count_student>0:
            return list_students

        else:
            return {"NNGUN ESTUDIANTE CUMPLE LA CONDICON"}

#CREAR ESTRUCTURA VACIA

    def get_dict_cities(self):
        dict_cities={}
        for city in self.cities:
            dict_cities[city]=[0,0]
        return  dict_cities

    def get_students_by_city(self):
        dict_cities=self.get_dict_cities()
        for student in self.students:
            if student.job:
                dict_cities[student.city][0]= dict_cities[student.city][0]+1
            else:
                dict_cities[student.city][1] = dict_cities[student.city][1] + 1

        return dict_cities
