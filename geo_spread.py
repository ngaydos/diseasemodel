import random

class Grid:

    def __init__(self, xsize, ysize, people):
        self.xarea = [0, xsize]
        self.yarea = [0, ysize]
        self.people = people


    def all_move(self):
        for person in self.people:
            xmove = random.randint(-1, 1)
            ymove = random.randint(-1, 1)
            if person.xloc + xmove <= xarea[1] and person.xloc + xmove >= xarea[0]:
                person.xloc += xmove
            if person.yloc + ymove <= yarea[1] and person.yloc + ymove >= xarea[0]:
                person.yloc += ymove