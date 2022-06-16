import random


class Cards:


    def __init__(self):

        self.value = random.randint(1, 13)

    def getValue(self):

        return self.value
