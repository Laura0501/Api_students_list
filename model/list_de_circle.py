from .student import Student
from .node_de import NodeDe

class List_de_cirle:
    def __init__(self):
        self.head = None
        self.count=0

    def get_all_students_circle_de(self):
        if self.head!=None:
            temp = self.head
            list = []
            while temp.next != self.head:
                list.append(temp.data)
                temp = temp.next
            list.append(temp.data)
            return list

    def add_de_circle(self, data):
        date=Student(data)
        if self.head == None:
            self.head = NodeDe(date)
            self.head.next = self.head
        else:
            if self.validate_exist_de(date.identification):
                raise Exception("Ya existe un estudiante con la identificacion")

            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            # posicionandonos en el ultimo
            new_node = NodeDe(date)
            temp.next = new_node
            temp.next.next=self.head
            new_node.previous = temp
        self.count += 1

    def add_to_start_de_circle(self, data):
        date = Student(data)
        if self.head == None:
            self.head = NodeDe(date)
            self.head.next=self.head
        else:
            if self.validate_exist_de(date.identification):
                raise Exception("Ya existe un estudiante con la identificacion")

            temp = NodeDe(date)
            temp.next = self.head
            self.head = temp
            self.head.next=self.head
        self.count += 1

    def validate_exist_de(self, id):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def count_de_circle(self):
        count = 0
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            count += 1
        count+= 1
        return count