from .node import Node
from .student import Student

class ListSE:
    def __init__(self):
        self.head= None
        self.count=0

#ADICIONAR ESTUDIANTE

    def add(self, data:Student):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con la identificacion")

            temp=self.head
            while temp.next != None:
                temp=temp.next
            #posicionandonos en el ultimo
            temp.next=Node(data)
        self.count += 1

    def add_to_start(self, data: Student):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.validate_exist(data.identification):
                raise Exception("Ya existe un estudiante con la identificacion")
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        self.count+=1


    def validate_exist(self,id):
            temp=self.head
            while temp != None:
                if temp.data.identification == id:
                    return True
                temp = temp.next
            return False

    def reversed_list(self):
        if self.head != None:
            list_copy = ListSE()
            temp = self.head
            while temp != None:
                list_copy.add_to_start(temp.data)
                temp = temp.next
            self.head = list_copy.head

#Ejercicios

#Intercambiar extremos
    def exchange_start_finally(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        date_temporal = self.head.data
        self.head.data = temp.data
        temp.data = date_temporal

#Eliminar por dato

    def remove_data_id(self, id: str):
        temp=self.head
        if self.head.data.identification==id:
            self.head=temp.next
            return True

        else:
            while temp.next != None:
                if temp.next.data.identification==id:
                    temp.next=temp.next.next
                    return True
                temp=temp.next
            temp.next=None
            return False

#Eliminar por posicion

    def remove_by_position(self, position: int):
        if position > 0 and position <= self.count :
            temp = self.head
            if position==1:
                self.head=temp.next

            else:
                count=1
                while temp.next != None:
                    if count==position-1:
                        temp.next=temp.next.next
                        break
                    count+=1
                    temp=temp.next

        else:
            raise Exception("La posición no es válida")


#Adicionar por posicion
    def add_to_position(self, position: int, data:Student):
        if position > 0 and position <= (self.count + 1):
            if position == 1:
                new_student = Node(data)
                new_student.next = self.head
                self.head = new_student
                self.count += 1
            else:
                temp = self.head
                count = 1
                while temp != None:
                    if count == position - 1:
                        new_node = Node(data)
                        new_node.next = temp.next
                        temp.next = new_node
                        self.count +=1
                        break
                    temp = temp.next
                    count +=1


        else:
            raise Exception("La posición no es válida")

#Mujeres primero

    def get_womans_to_start(self):
        temp=self.head
        list_copy = ListSE()
        while temp != None:
            if temp.data.gender == 2:
                list_copy.add_to_start(temp.data)

            if temp.data.gender == 1:
                list_copy.add(temp.data)
            temp=temp.next
        self.head = list_copy.head

# Lista intercalada por genero
    def get_list_for_genders(self):
        if self.count > 1:
            list_man= ListSE()
            list_woman= ListSE()
            temp=self.head
            while temp != None:
                if temp.data.gender==2:
                    list_woman.add(temp.data)
                if temp.data.gender==1:
                    list_man.add(temp.data)
                temp=temp.next

            if list_man.count ==0 or list_woman.count ==0:
                raise Exception("No es posible intercalar, la lista solo contiene estudiantes del mismo género")

            else:
                pos = 2
                temp = list_woman.head
                while temp != None:
                    if pos > list_man.count:
                        list_man.add(temp.data)
                    else:
                        list_man.add_to_position(pos,temp.data)
                    temp = temp.next
                    pos = pos +2
                self.head = list_man.head

        else:
            raise Exception({"message":"No hay datos para intercalar"})

    def order_students_age_less(self, data):
        if self.head==None:
            self.add_to_start(data)
        else:
            if data.age<self.head.data.age:
                self.add_to_start(data)
            else:
                temp=self.head
                while temp.next !=None:
                    if temp.data.age < temp.next.data.age:
                        break
                    temp=temp.next
                new_node=Node(data)
                new_node.next=temp.next
                temp.next=new_node
        self.count+=1


    def order_students_age_higher(self, data):
        if self.head==None:
            self.add_to_start(data)
        else:
            if data.age>self.head.data.age:
                self.add_to_start(data)
            else:
                temp=self.head
                while temp.next !=None:
                    if temp.data.age > temp.next.data.age:
                        break
                    temp=temp.next
                new_node=Node(data)
                new_node.next=temp.next
                temp.next=new_node
        self.count+=1


    def order_for_ages_genders(self):
        if self.head !=None:
            temp=self.head
            list_woman=ListSE()
            list_man=ListSE()

            while temp !=None:
                if temp.data.gender ==1:
                    list_man.order_students_age_higher(temp.data)

                if temp.data.gender == 2:
                    list_woman.order_students_age_less(temp.data)
                temp=temp.next

            temp=list_woman.head
            while temp.next !=None:
                temp=temp.next

            temp.next=list_man
            return list_woman