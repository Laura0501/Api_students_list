from model.student import Student
from model.list_de_circle import List_de_cirle


class ListDeCircleService:

    cities = ["Manizales", "Pereira", "Chinchina", "Armenia"]
    def __init__(self):
        self.students = List_de_cirle()

    def get_all_students_circle_de(self):
        return self.students.get_all_students_circle_de()

    def add_circle_de(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_de_circle(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_to_start_de_circle(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start_de_circle(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def count_de_circle(self):
        if self.students.head ==None:
            return {"Message":"La lista esta vacia"}

        else:
            return {"El numero de estudiantes es:": self.students.count_de_circle()}