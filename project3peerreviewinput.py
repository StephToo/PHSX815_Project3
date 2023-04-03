# here is a rough first attempt at what we need to do 
# I still need to include some of my code from the last two projects here
# but this is what is needed to add to those I suppose


import numpy as np
from scipy.optimize import minimize_scalar

def graphene_test(p, n):

    # Characterization of graphene type (monolayer vs bilayer) using machine better for one type (bias)
    # p (float): probability of finding monolayer
    # n (int): amount of samples tested

    return np.random.binomial(n, p)
    # gives an array of outcomes of tests (0 or 1)
    

def likelihood(p, X):
    # likelihood of parameter given data
 
    return np.power(p, np.sum(X)) * np.power(1 - p, len(X) - np.sum(X))
    # gives a float likelihood function evaluated at p


def estimate_p(X):
    # estimate probability of finding monolayer via the "Max Likelihood Estimation"
    # p here is teh X(np.array) for all the outcomes of tests
    # p is max value 
    # gives a float "max likelihood estimation" of probability of finding monolayer graphene

    objective = lambda p: -likelihood(p, X)
    # https://python.quantecon.org/mle.html

    result = minimize_scalar(objective, bounds=(0, 1), method='bounded')
    # minimize scalar from scipy.optimize, found online in a forum but need to find the link for it 
    return result.x

# Example of what output could be formatted like
p_true = 0.7 # probability of finding monolayer
n = 1000 # tests
X = graphene_test(p_true, n)
p_estimate = estimate_p(X)
print(f'True probability: {p_true:.2f}')
print(f'Estimated probability: {p_estimate:.2f}')
