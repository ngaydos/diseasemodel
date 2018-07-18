import random
import matplotlib.pyplot as plt
import math

class Grid:

    def __init__(self, xsize, ysize, people):
        self.xarea = [0, xsize]
        self.yarea = [0, ysize]
        self.people = people
        #this is for storing where each person wants to move when moves are in relation to other people



    def split_people(self):
        '''splits people into two lists of infected and uninfected people objects
        '''
        uninfected_people = []
        infected_people = []
        for person in self.people:
            if person.infected == True:
                infected_people.append(person)
            else:
                uninfected_people.append(person)
        return uninfected_people, infected_people

    def random_move(self):
        for person in self.people:
            xmove = random.randint(-1, 1)
            ymove = random.randint(-1, 1)
            if person.xloc + xmove <= self.xarea[1] and person.xloc + xmove >= self.xarea[0]:
                person.xloc += xmove
            if person.yloc + ymove <= self.yarea[1] and person.yloc + ymove >= self.yarea[0]:
                person.yloc += ymove

    def zombie_move(self):
        #zombies are not currently running, not sure why not
        for person in self.people:
            #should have the infected people move towards the closest uninfected, and should have the
            #uninfected move away from the closest infected.
            uninfected_people, infected_people = self.split_people()
                #sets a dummy variable to be replaced
            distance_check = self.xarea[1] + self.yarea[1]
            if person.infected == True:
                for uninfected_person in uninfected_people:
                    working_distance = person.distance_from(uninfected_person)
                    if working_distance < distance_check:
                        distance_check = working_distance
                        if person.xloc > uninfected_person.xloc:
                            person.desired_xmove = -1
                        elif person.xloc < uninfected_person.xloc:
                            person.desired_xmove = 1
                        else:
                            person.desired_xmove = 0
                        if person.yloc > uninfected_person.yloc:
                            person.desired_ymove = -1
                        elif person.yloc < uninfected_person.yloc:
                            person.desired_ymove = 1
                        else:
                            person.desired_ymove = 0
                #need similar code here to make uninfected people run from zombies
        for person in self.people:
            #coding this way will result in people getting trapped in corners because they refused to move towards zombies
            xmove = person.desired_xmove
            ymove = person.desired_ymove
            if person.xloc + xmove <= self.xarea[1] and person.xloc + xmove >= self.xarea[0]:
                person.xloc += xmove
            if person.yloc + ymove <= self.yarea[1] and person.yloc + ymove >= self.yarea[0]:
                person.yloc += ymove


    def simulate_random(self, infection_range, generation_count, infection_rate = 100 ,movement_distance = 1):
        random.choice(self.people).infected = True
        for i in range(generation_count):
            infected_people = []
            non_infected_people = []
            for person in self.people:
                if person.infected == True:
                    infected_people.append(person)
                else:
                    non_infected_people.append(person)
            for _ in range(movement_distance):
                self.random_move()
            for infected_person in infected_people:
                for non_infected_person in non_infected_people:
                    if infected_person.distance_from(non_infected_person) <= infection_range and non_infected_person.exposed == False:
                        if random.randint(1, 100) <= infection_rate:
                            non_infected_person.infected = True
                            non_infected_person.exposed = True
                        else:
                            non_infected_person.exposed = True
        return(sum(person.infected for person in self.people))

    def plot_all(self):
        infected_x = []
        infected_y = []
        non_infected_x = []
        non_infected_y = []
        for person in self.people:
            if person.infected == True:
                infected_x.append(person.xloc)
                infected_y.append(person.yloc)
            else:
                non_infected_x.append(person.xloc)
                non_infected_y.append(person.yloc)
        plt.plot(infected_x, infected_y, 'ro')
        plt.plot(non_infected_x, non_infected_y, 'bo')
        plt.show()


class Person:

    def __init__(self, xloc, yloc, infected = False, exposed = False):
        self.xloc = xloc
        self.yloc = yloc
        self.infected = infected
        self.exposed = exposed
        self.desired_xmove = 0
        self.desired_ymove = 0


    def distance_from(self, other):
        return math.sqrt(((self.xloc - other.xloc) ** 2 ) + ((self.yloc - other.yloc) **2))

class Hospital:

    def __init__(self, xloc, yloc):
        self.xloc = xloc
        self.yloc = yloc

if __name__ == '__main__':
    people = []
    for i in range(50):
        people.append(Person(random.randint(0, 20), random.randint(0, 20)))
    grid = Grid(20, 20, people)
    print(grid.simulate_random(1, 10))
    grid.plot_all()