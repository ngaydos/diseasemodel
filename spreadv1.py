import random

class Person:

    def __init__(self, infected = False, exposed = False, checked = False):
        self.infected = infected
        self.exposed = exposed
        self.checked = checked

def all_infected(people):
    '''checks to see if all people who are infected have been checked and infected for use in simulate
    Inputs = list
    Outputs = Bool
    '''
    for person in people:
        if person.infected == True:
            if person.checked == True:
                continue
            else:
                return False
    return True

def simulate(people, num_infect, infection_rate):
    random.choice(people).infected = True
    while all_infected(people) == False:
        for person in people:
            if person.infected and person.checked == False:
                infect(person, people, num_infect, infection_rate)
    count_infected = sum([person.infected for person in people])
    return count_infected/len(people)

def infect(person, people, num_infect, infection_rate):
    '''
    takes a person (assumes they are infected) and infects a num_infect number of people from a list of people
    inputs: person: A Person object, people: A list of Person objects, num_infect: Int to infect, infection_rate: int between 0 and 100
    outputs: None
    '''
    to_infect = random.sample(people, num_infect)
    for i in to_infect:
        if random.randint(1, 100) <= infection_rate:
            i.infected = True
    person.checked = True
    #right now this doesn't remove the infected individual from the possible samples