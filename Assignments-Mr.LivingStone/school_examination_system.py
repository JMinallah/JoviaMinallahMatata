# parent learner class with name and registration number
class Learner:
    def __init__(self, name, reg_no):
        self.name = name
        self.reg_no = reg_no

    def get_name(self):
        return self.name

    def get_reg_no(self):
        return self.reg_no
