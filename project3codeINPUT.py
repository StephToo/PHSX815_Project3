import random
import numpy as np

# Define the probability distribution with a configurable parameter
# https://www.geeksforgeeks.org/random-normalvariate-function-in-python/
def probability_distribution(parameter):
    return random.normalvariate(0, parameter)

# https://stackoverflow.com/questions/11615664/multivariate-normal-density-in-python
# Define the likelihood function
def likelihood(data, parameter):
    sigma = np.std(data)
    return np.exp(-0.5*np.sum((data/parameter)**2))/((2*np.pi*parameter**2)**(len(data)/2))

# Set the true parameter value and the number of measurements to take
true_parameter_value = 2.0
num_measurements = 100

# Simulate the experiment and save the results to a text file
#https://www.projectpro.io/recipes/write-text-file-output-of-for-loop
with open('simulated_data.txt', 'w') as file:
    for i in range(num_measurements):
        result = probability_distribution(true_parameter_value)
        file.write(str(result) + '\n')







