from model.student import Student
from model.list_se_circle import List_se_cirle


class ListSeCircleService:

    cities = ["Manizales", "Pereira", "Chinchina", "Armenia"]
    def __init__(self):
        self.students = List_se_cirle()

    def get_all_students_circle(self):
        return self.students.get_all_students_circle()

    def add_circle(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_circle(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def add_to_start_circle(self, data):
        student = Student(data)
        if data['city'] in self.cities:
            self.students.add_to_start_circle(student)
        else:
            raise Exception("La ciudad no está en la lista")

    def count(self):
        if self.students.head ==None:
            return {"Message":"La lista esta vacia"}

        else:
            return {"El numero de estudiantes es:": self.students.count()}