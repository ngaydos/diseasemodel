import random
from base_spread import Person, all_infected, infect

def simulate(people, num_infect):
    '''simulates an infection in a group of people. Each person is exposed 1 time to num_infect other people
    and each person exposed has one chance of catching the disease at a infection_rate chance of exposure.
    '''
    infected = []
    random.choice(people).infected = True
    while all_infected(people) == False:
        for person in people:
            if person.infected and person.checked == False:
                infect(person, people, num_infect)
        count_infected = sum([person.infected for person in people])
        infected.append(count_infected)
    return infected
