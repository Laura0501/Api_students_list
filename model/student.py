class Student:
    """def __init__(self, identification,gender,salary,job,name,age,zone,city):
        self.identification=identification
        self.gender=gender
        self.salary=salary
        self.job=job
        self.name=name
        self.age=age
        self.zone=zone
        self.city=city"""

    def __init__(self, my_dict):
            for key in my_dict:
                setattr(self,key, my_dict[key])


