from model.student import Student
from model.list_se import ListSE

class ListSE_service:
    cities = ["Manizales", "Pereira", "Chinchina", "Armenia"]

    def __init__(self):
        self.students=ListSE()

        """camilo=Student("1053807435", 1, 3540899, True, "Camilo Villegas", 26, "Urbana", self.cities[1])


      gloria=Student({"identification":"30318536", "name": "Gloria Cuellar", "gender": 2, "salary":1250678,
                        "job":True, "age": 35, "zone":"Urbana", "city":self.cities[0]})

        self.students.add(gloria)

        self.students.add({"identification":"1053802424", "name": "Felipe Alvaran", "gender": 1, "salary":1178000,
                        "job":True, "age": 28, "zone":"Urbana", "city":self.cities[1]})"""


    #Agregar el estudiante a la cabeza

    def get_all_students(self):
        return self.students.head

    #Agregar un estudiante desde postman

    def add(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add(student)
        else:
            raise Exception("La ciudad no está en el listado")

    def add_to_start(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start(student)
        else:
            raise Exception("La ciudad no está en la lista")


    #Invertir la lista
    def reversed_list(self):
        if self.students.head == None:
            return {"message": "La lista está vacía"}
        else:
            self.students.reversed_list()
            return {"message": "Se ha invertido la lista"}


    def exchange_start_finally(self):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            self.students.exchange_start_finally()
            return {"message": "Se han intercambiado los extremos de la lista"}


    def remove_data_id(self, id):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            deleted_student = self.students.remove_data_id(id)
            if deleted_student == True:
                return {"message": "Se ha eliminado el estudiante de la lista"}
            else:
                return {"message": "El estudiante no esta en la lista"}


    def remove_by_position(self, position):
        try:
            if self.students.head == None:
                return {"message": "La lista esta vacia"}
            else:
                self.students.remove_by_position(position)
                return {"message":"Se ha eliminado el estudiante en la posicion indicada"}

        except Exception as error:
            return {"message":str(error)}


    def add_to_position(self, position, data):
        student = Student(data)
        try:
            self.students.add_to_position(position,student)
            return {"message": "Se ha agregado el estudiante en la posicion solicitada"}

        except Exception as error:
            return {"message":str(error)}

    def get_womans_to_start(self):
        if self.students.head==None:
            return{"Message":"La lista esta vacia"}

        else:
            self.students.get_womans_to_start()
            return {"message":"Se ha ordenado la lista, mujeres de primero"}

    def get_list_for_genders(self):
        try:
            if self.students.head == None:
                return {"message": "La lista esta vacia"}

            else:
                self.students.get_list_for_genders()
                return{"Message":"Se ha ordenado la lista intercalada por generos "}

        except Exception as error:
            return {"Message":str(error)}
