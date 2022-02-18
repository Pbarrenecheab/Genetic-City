# -*- coding: utf-8 -*-

"""
 ██████╗ ███████╗███╗   ██╗███████╗████████╗██╗ ██████╗     ██████╗██╗████████╗██╗   ██╗
██╔════╝ ██╔════╝████╗  ██║██╔════╝╚══██╔══╝██║██╔════╝    ██╔════╝██║╚══██╔══╝╚██╗ ██╔╝
██║  ███╗█████╗  ██╔██╗ ██║█████╗     ██║   ██║██║         ██║     ██║   ██║    ╚████╔╝
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝     ██║   ██║██║         ██║     ██║   ██║     ╚██╔╝
╚██████╔╝███████╗██║ ╚████║███████╗   ██║   ██║╚██████╗    ╚██████╗██║   ██║      ██║
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝ ╚═════╝     ╚═════╝╚═╝   ╚═╝      ╚═╝

Parameters and some functions to compute new parameters.

By: Juan Mugica - jmugicag@mit.edu
MIT Media Lab - City Science Group
                                                                                      """






from matplotlib.colors import ListedColormap
import numpy as np


population_size = 200#1000 # Number of solutions in the population.
num_parents_mating = 10#100 # Number of solutions to be selected as parents in the mating pool. Must be < population_size
num_generations = 400#400 # Number of generations.
prob_mutation = .1 # Must be between 0 and 1
#TODO: review as prop_crossover and crossover_value should tell the same thing
#prop_crossover = .9 # The point which will define the amount of each parent constituting the offspring
crossover_value = .9 # The point at which crossover takes place between two parents. Usually, it is at the center.
block_size = 15 # Size of the area to optimise (square dimension)
city_size = 1 #Amount of adjancent blocks to optimise in parallel (square dimension)
building_types = 3 # [1 = Park, 2 = Office, 3 = Residential, 4 = Road]
cmap = ListedColormap(["green","blue","orange","grey"])
#cmap = ListedColormap(["green","blue","orange"])
visualizations = True


'''PARAMETERS FOR RULES'''

'''RULE1: green_space_balance_amount'''
percentage_of_parks = 0.9
weights = np.array([0, 0, 1, 0, 0, 0, 0, 0, 0]) #Weights used by function to evaluate. Places more interest in high numbers.



'''PARAMETERS FOR PLOTS'''
num_generations_saved = 8
time_per_image = 500 #Time in ms for each image in the GIF

#Create dictionary for images saving
dict = {i:chr(i+96) for i in range(1,27)}
