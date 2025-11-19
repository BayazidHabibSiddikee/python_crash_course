from random import randint
class Die:
    def __init__(self,num=6):
        self.num= num
    def roll(self):
        return randint(1,self.num)
