class add():

    def __init__(self,*args):
        print(args)
        self.l=list(args)
        print(self.l)

"""
class mul(add):

    def __init__(self,no):
        super().__init__()
        super().__init__(34)
        print(no)
"""


o1 = add(5,34)
