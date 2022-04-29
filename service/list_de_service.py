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



