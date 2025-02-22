import numpy as np
from random import *
from random import random
from random import randint
from progressbar import printProgressBar #Import progress bar function.


def mutation(input_city, mut_prob, types): #Mutates chromosomically each individual depending on a given probability.
    for genes in range(0, input_city.shape[0]):
        #TODO: is this != 0 necessary? -> can be removed
        if random() < mut_prob:
            #place_variable = randint(1,9)
            input_city[genes] = randint(1,types)
    return input_city

def mutate_individuals(input_city, mutationprob, population, citysize,types): #Complete function for looping through every individual's mutations in an entire population.
    mutateded_population = np.zeros((population, citysize*citysize))
    printProgressBar(0, population, prefix = 'Population Mutation Progress:', suffix = 'Complete', length = 50)
    for indiv in range (0, population):
        mutated_individual = mutation(input_city[indiv, :], mutationprob, types)
        mutateded_population[indiv, :] = mutated_individual
        printProgressBar(indiv + 1, population, prefix = 'Population Mutation Progress:', suffix = 'Complete', length = 50)
    return mutateded_population
