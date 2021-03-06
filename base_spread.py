import random

class Person:

    def __init__(self, infected = False, checked = False):
        self.infected = infected
        self.checked = checked

def simulate(people, num_infect):
    '''simulates an infection. Infects one random individual and then has them infect num_infect additional people.
    Then each of those people attempts to infect num_individual random individuals. If those individuals are uninfected
    then they are each infected and will attempt to infect in the future. 
    If each infected individual has infected others then the simulation ends
    inputs = List of people objects, int
    outputs = Float of ratio of people infected
    '''
    random.choice(people).infected = True
    while all_infected(people) == False:
        for person in people:
            if person.infected and person.checked == False:
                infect(person, people, num_infect)
    count_infected = sum([person.infected for person in people])
    return count_infected/len(people)

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

def infect(person, people, num_infect):
    '''
    takes a person (assumes they are infected) and infects a num_infect number of people from a list of people
    inputs: person: A Person object, people: A list of Person objects, num_infect: Int to infect
    outputs: None
    '''
    to_infect = random.sample(people, num_infect)
    for i in to_infect:
        i.infected = True
    person.checked = True
    #right now this doesn't remove the infected individual from the possible samples