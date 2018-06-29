import random

class Person:

    def __init__(self, infected = False, checked = False):
        self.infected = infected
        self.checked = checked

def simulate(people, num_infect):
    '''simulates an infection. Infects one random individual and then has them infect num_infect additional people.
    Then each of those people attempts to infect num_individual random individuals. If those individuals are uninfected
    then they are each infected and will attempt to infect in the future. If each infected individual has infected others then the simulation ends
    '''


def all_infected(people):
    for person in people:
        if person.infected == True:
            if person.checked == True:
                continue
            else:
                return False
    return True