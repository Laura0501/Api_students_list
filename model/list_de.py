from .student import Student
from .node_de import NodeDe

class ListDe:
    def __init__(self):
        self.head= None
        self.count=0

    def get_all_students_de(self):
        if self.head!=None:
            list = []
            temp = self.head
            while temp.next != None:
                list.append(temp.data)
                temp = temp.next
            list.append(temp.data)
            return list

    def add_de(self, data):
        date=Student(data)
        if self.head == None:
            self.head = NodeDe(date)
        else:
            if self.validate_exist_de(date.identification):
                raise Exception("Ya existe un estudiante con la identificacion")

            temp = self.head
            while temp.next != None:
                temp = temp.next

            # posicionandonos en el ultimo
            new_node = NodeDe(date)
            temp.next = new_node
            new_node.prev = temp
        self.count += 1

    def add_to_start_de(self, data):
        date = Student(data)
        if self.head == None:
            self.head = NodeDe(date)
        else:
            if self.validate_exist_de(date.identification):
                raise Exception("Ya existe un estudiante con la identificacion")
            temp = NodeDe(date)
            temp.next = self.head
            self.head = temp
        self.count += 1

    def validate_exist_de(self, id):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def reversed_list_de(self):
        if self.head != None:
            list_copy = ListDe()
            temp = self.head
            while temp != None:
                list_copy.add_to_start_de(temp.data)
                temp = temp.next
            self.head = list_copy.head




