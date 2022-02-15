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


population_size = 100#1000 # Number of solutions in the population.
num_parents_mating = 4#100 # Number of solutions to be selected as parents in the mating pool. Must be < population_size
num_generations = 100#400 # Number of generations.
prob_mutation = .3 # Must be between 0 and 1
#TODO: review as prop_crossover and crossover_value should tell the same thing
#prop_crossover = .9 # The point which will define the amount of each parent constituting the offspring
crossover_value = .9 # The point at which crossover takes place between two parents. Usually, it is at the center.
building_types = 3 # [1 = Office, 2 = Park, 3 = Residential]
block_size = 10 # Size of the area to optimise (square dimension)
city_size = 1 #Amount of adjancent blocks to optimise in parallel (square dimension)
building_types = 3 # [1 = Office, 2 = Park, 3 = Residential]
cmap = ListedColormap(["blue","green","orange"])
visualizations = False

