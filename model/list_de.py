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

        if self.head == None:
            self.head = NodeDe(data)
        else:
            if self.validate_exist_de(data.identification):
                raise Exception("Ya existe un estudiante con la identificacion")

            temp = self.head
            while temp.next != None:
                temp = temp.next

            # posicionandonos en el ultimo
            new_node = NodeDe(data)
            temp.next = new_node
            new_node.previous = temp
        self.count += 1

    def add_to_start_de(self, data):

        if self.head == None:
            self.head = NodeDe(data)
        else:
            if self.validate_exist_de(data.identification):
                raise Exception("Ya existe un estudiante con la identificacion")
            temp = NodeDe(data)
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

    def exchange_start_finally_de(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        date_temporal = self.head.data
        self.head.data = temp.data
        temp.data = date_temporal

#Eliminar por dato

    def remove_data_id_de(self, id: str):
        temp=self.head
        if temp.data.identification==id:
            if temp.next==None:
                self.head=None
            else:
                temp.next.previous=None
                self.head=temp.next
            return True

        else:
            while temp.next != None:
                if temp.next.data.identification == id:
                    temp.next = temp.next.next
                    if temp.next.next.previous != None:
                        temp.next.next.previous = temp.next.previous
                    else:
                        temp.next.next.previous = None
                    return True
                    break
                temp = temp.next
            temp.next = None
            return False


#Eliminar por posicion
    def remove_by_position_de(self, position: int):
        if position > 0 and position <= self.count :
            temp = self.head
            if position==1:
                if temp.next == None:
                    self.head = None
                else:
                    temp.next.previous = None
                    self.head=temp.next

            else:
                count=1
                while temp.next != None:
                    if count == position - 1:
                        temp.next = temp.next.next
                        if temp.next.next.previous != None:
                            temp.next.next.previous = temp.next.previous
                        else:
                            temp.next.next.previous = None
                        return True
                        break
                    count += 1
                    temp = temp.next
        else:
            raise Exception("La posición no es válida")

#Adicionar por posicion

    def add_to_position_de(self, position: int, data:Student):
        if position > 0 and position <= (self.count + 1):
            if position == 1:
                new_student = NodeDe(data)
                new_student.next = self.head
                self.head = new_student
                self.count += 1
            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        new_node = NodeDe(data)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count +=1
                        break
                    temp = temp.next
                    count +=1

        else:
            raise Exception("La posición no es válida")

#Adicionar en posicion
    def add_to_position_de(self, position, data: Student):
        date=Student(data)
        if position > 0 and position <= (self.count + 1):
            if position == 1:
                self.add_de(date)
        else:
            if self.validate_exist_de(date.identification):
                raise Exception("Ya existe un estudiante con esa identificacion")
            node = NodeDe(date)
            temp = self.head
            previous= None
            count = 1

            while count< position:
                previous = temp
                temp = temp.next
                count += 1
            node.next = temp
            temp.previous = node
            previous.next = node
            node.previous= previous
        self.count = +1

#Mujeres primero
    def get_womans_to_start_de(self):
        temp=self.head
        list_copy = ListDe()
        while temp != None:
            if temp.data.gender == 2:
                list_copy.add_to_start_de(temp.data)

            if temp.data.gender == 1:
                list_copy.add_de(temp.data)
            temp=temp.next
        self.head = list_copy.head

# Lista intercalada por genero
    def get_list_for_genders_de(self):
        if self.count > 1:
            list_man= ListDe()
            list_woman= ListDe()
            temp=self.head
            while temp != None:
                if temp.data.gender==2:
                    list_woman.add_de(temp.data)
                if temp.data.gender==1:
                    list_man.add_de(temp.data)
                temp=temp.next

            if list_man.count ==0 or list_woman.count ==0:
                raise Exception("No es posible intercalar, la lista solo contiene estudiantes del mismo género")

            else:
                pos = 2
                temp = list_woman.head
                while temp != None:
                    if pos > list_man.count:
                        list_man.add_de(temp.data)
                    else:
                        list_man.add_to_position_de(pos,temp.data)
                    temp = temp.next
                    pos = pos +2
                self.head = list_man.head

        else:
            raise Exception({"message":"No hay datos para intercalar"})

#Lista organizada por edad
    def order_students_age_less_de(self, data):
        if self.head==None:
            self.add_to_start_de(data)
        else:
            if data.age<self.head.data.age:
                self.add_to_start_de(data)
            else:
                temp=self.head
                while temp.next !=None:
                    if temp.data.age < temp.next.data.age:
                        break
                    temp=temp.next
                new_node=NodeDe(data)
                new_node.next=temp.next
                temp.next=new_node
        self.count+=1


    def order_students_age_higher_de(self, data):
        if self.head==None:
            self.add_to_start_de(data)
        else:
            if data.age>self.head.data.age:
                self.add_to_start_de(data)
            else:
                temp=self.head
                while temp.next !=None:
                    if temp.data.age > temp.next.data.age:
                        break
                    temp=temp.next
                new_node=NodeDe(data)
                new_node.next=temp.next
                temp.next=new_node
        self.count+=1


    def order_for_ages_genders_de(self):
        if self.head !=None:
            temp=self.head
            list_woman=ListDe()
            list_man=ListDe()

            while temp !=None:
                if temp.data.gender ==1:
                    list_man.order_students_age_higher_de(temp.data)

                if temp.data.gender == 2:
                    list_woman.order_students_age_less_de(temp.data)
                temp=temp.next

            temp=list_woman.head
            while temp.next !=None:
                temp=temp.next

            temp.next=list_man
            return list_woman

#Eliminar por posicion parado donde
    def Kamikaze(self, position: int):
        if position > 0 and position <= self.count :
            temp = self.head
            if position==1:
                self.head=temp.next
                self.head.previous=None


            else:
                count=1
                while temp.next != None:
                    if count == position:
                        break
                    temp=temp.next
                    count += 1
                temp.previous.next=temp.next
                if temp.previous!=None:
                    temp.next.previous=temp.previous
                else:
                    temp.next.previous=None
        else:
            raise Exception("La posición no es válida")





