import random
import matplotlib.pyplot as plt
import math

class Grid:

    def __init__(self, xsize, ysize, people):
        self.xarea = [0, xsize]
        self.yarea = [0, ysize]
        self.people = people


    def all_move(self):
        for person in self.people:
            xmove = random.randint(-1, 1)
            ymove = random.randint(-1, 1)
            if person.xloc + xmove <= self.xarea[1] and person.xloc + xmove >= self.xarea[0]:
                person.xloc += xmove
            if person.yloc + ymove <= self.yarea[1] and person.yloc + ymove >= self.yarea[0]:
                person.yloc += ymove

    def simulate(self, infection_range, generation_count, movement_distance = 1):
        random.choice(person).infected = True
        for i in range(generation_count):
            infected_people = [person if person.infected == True for person in self.people]
            non_infected_people = [person if person.infected == False for person in self.people]
            for _ in range(movement_distance):
                self.all_move()
            for infected_person in infected_people:
                for non_infected_person in non_infected_people:
                    if infected_person.distance_from(non_infected_person) <= infection_range:
                        non_infected_person.infected == True
        return sum([person.infected for person in self.people])


class Person:

    def __init__(self, xloc, yloc, infected = False):
        self.xloc = xloc
        self.yloc = yloc
        self.infected = infected


    def distance_from(self, other):
        return math.sqrt(((self.xloc - other.xloc) ** 2 ) + ((self.yloc - other.yloc) **2))

if __name__ == '__main__':
    people = [Person(random.randint(0, 20), random.randint(0, 20)) ]
    grid = Grid(20, 20, people)
    xplaces = [people[0].xloc]
    yplaces = [people[0].yloc]
    for i in range(5):
        grid.all_move()
        xplaces.append(people[0].xloc)
        yplaces.append(people[0].yloc)
    plt.scatter(xplaces, yplaces)
    plt.show()