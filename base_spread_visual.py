import random
from base_spread import Person, all_infected, infect
import matplotlib.pyplot as plt

def simulate(people, num_infect):
    '''simulates an infection in a group of people. Each person is exposed 1 time to num_infect other people
    and each person exposed infects other people. This tracks the number of people infected at each generation looped through.
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


def multitest_same_num(num_infect, test_count):
    infection_rates = []
    for i in range(test_count):
        people = []
        for i in range(100):
            people.append(Person())
        infection_rates.append(simulate(people, num_infect))
    for group in infection_rates:
        plt.plot(group)

