from model.student import Student
from model.list_de import ListDe

class ListDeService:
    cities = ["Manizales", "Pereira", "Chinchina", "Armenia"]

    def __init__(self):
        self.students = ListDe()

    def get_all_students_de(self):
        return self.students.get_all_students_de()

    def add_de(self, data):
        student=Student(data)
        if data['city'] in self.cities:
            self.students.add_de(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_to_start_de(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start_de(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def reversed_list_de(self):
        if self.students.head == None:
            return {"message": "La lista está vacía"}
        else:
            self.students.reversed_list_de()
            return {"message": "Se ha invertido la lista"}

    def exchange_start_finally_de(self):
            if self.students.head == None:
                return {"message": "La lista esta vacia"}
            else:
                self.students.exchange_start_finally_de()
                return {"message": "Se han intercambiado los extremos de la lista"}

    def remove_data_id_de(self, id):
        if self.students.head == None:
            return {"message": "La lista esta vacia"}
        else:
            deleted_student = self.students.remove_data_id_de(id)
            if deleted_student == False:
                return {"message": "El estudiante no esta en la lista"}
            else:
                return {"message": "Se elimino exitosamente"}

    def remove_by_position_de(self, position):
        try:
            if self.students.head == None:
                return {"message": "La lista esta vacia"}
            else:
                self.students.remove_by_position_de(position)
                return {"message":"Se ha eliminado el estudiante en la posicion indicada"}

        except Exception as error:
            return {"message":str(error)}


    def add_to_position_de(self, position, data):
        student = Student(data)
        try:
            self.students.add_to_position_de(position,student)
            return {"message": "Se ha agregado el estudiante en la posicion solicitada"}

        except Exception as error:
            return {"message":str(error)}

    def get_womans_to_start_de(self):
        if self.students.head==None:
            return{"Message":"La lista esta vacia"}

        else:
            self.students.get_womans_to_start_de()
            return {"message":"Se ha ordenado la lista, mujeres de primero"}

    def get_list_for_genders_de(self):
        try:
            if self.students.head == None:
                return {"message": "La lista esta vacia"}

            else:
                self.students.get_list_for_genders_de()
                return{"Message":"Se ha ordenado la lista intercalada por generos "}

        except Exception as error:
            return {"Message":str(error)}

    def order_for_ages_genders_de(self):
        if self.students.head==None:
            return{"Message":"La lista esta vacia"}

        else:
            self.students.order_for_ages_genders_de()
            return {"message":"Se ha ordenado la lista, mujeres de primero de menor a mayor, luego "
                              "hombres de mayor a menor"}

    def kamikaze(self, position):
        try:
            if self.students.head == None:
                return {"message": "La lista esta vacia"}
            else:
                self.students.Kamikaze(position)
                return {"message":"Se ha eliminado el estudiante en la posicion indicada"}

        except Exception as error:
            return {"message":str(error)}



