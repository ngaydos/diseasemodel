from geo_spread import Person
import random
import matplotlib.pyplot as plt
import random


class Grid:

    def __init__(self, xsize, ysize, people):
        self.xarea = [0, xsize]
        self.yarea = [0, ysize]
        self.people = people

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


    def zombie_move(self):
        #zombies are not currently running, not sure why not
        uninfected_people, infected_people = self.split_people()

        for person in self.people:
            random.shuffle(uninfected_people)
            random.shuffle(infected_people)
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
            else:
                for infected_person in infected_people:
                    working_distance = person.distance_from(infected_person)
                    if working_distance < working_distance:
                        distance_check = working_distance
                        if person.xloc < infected_person.xloc:
                            person.desired_xmove = -1
                        elif person.xloc > infected_person.xloc:
                            person.desired_xmove = 1
                        else:
                            person.desired_xmove = 0
                        if person.yloc < infected_person.yloc:
                            person.desired_ymove = -1
                        elif person.yloc > infected_person.yloc:
                            person.desired_ymove = 1
                        else:
                            person.desired_ymove = 0

        for person in self.people:
            #coding this way will result in people getting trapped in corners because they refused to move towards zombies
            xmove = person.desired_xmove
            ymove = person.desired_ymove
            if person.xloc + xmove <= self.xarea[1] and person.xloc + xmove >= self.xarea[0]:
                person.xloc += xmove
            if person.yloc + ymove <= self.yarea[1] and person.yloc + ymove >= self.yarea[0]:
                person.yloc += ymove

    def simulate_zombie(self, infection_range, generation_count, infection_rate = 100 ,movement_distance = 1):
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
                self.zombie_move()
            for infected_person in infected_people:
                for non_infected_person in non_infected_people:
                    if infected_person.distance_from(non_infected_person) <= infection_range and non_infected_person.exposed == False:
                        if random.randint(1, 100) <= infection_rate:
                            non_infected_person.infected = True
                            non_infected_person.exposed = True
                        else:
                            non_infected_person.exposed = True
        return(sum(person.infected for person in self.people))


    def weighted_distance(self, person):
        holding_dict = {}
        distances = []
        for other_person in people:
            if person.infected != other_person.infected:
                distance = person.distance_from(other_person)
                distances.append(1.0/distance)
                holding_dict[other_person] = (1.0/distance)
        total_distance = sum(distances)
        #this does the opposite of what I want it to.
        #Probably want to do something to reverse the values
        target_num = random.uniform(0, total_distance)
        acc = 0
        for val in distances:
            acc += val
            if acc <= target_num:
                for key, value in holding_dict.items():
                    if value == val:
                        return key

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