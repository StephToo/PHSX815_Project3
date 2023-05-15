import numpy as np
import matplotlib.pyplot as plt
# https://analyticsindiamag.com/maximum-likelihood-estimation-python-guide/#:~:text=The%20term%20likelihood%20can%20be,employed%
# 20with%20most%2Dlikely%20parameters
# https://python.quantecon.org/mle.html
def likelihood(data, parameter):
    sigma = np.std(data)
    return np.exp(-0.5*np.sum((data/parameter)**2))/((2*np.pi*parameter**2)**(len(data)/2))

# Read in the data from the text file
with open('simulated_data.txt', 'r') as file:
    data = [float(line) for line in file]

# Define a range of parameter values to test
# https://www.geeksforgeeks.org/numpy-linspace-python/
parameter_values = np.linspace(0.1, 10, 20)

# Calculate the likelihood for each parameter value and find the maximum likelihood value
# https://barnesanalytics.com/maximum-likelihood/
likelihoods = [likelihood(data, p) for p in parameter_values]
max_likelihood_index = np.argmax(likelihoods)
max_likelihood_parameter = parameter_values[max_likelihood_index]

# Plot the likelihood as a function of the parameter value
plt.plot(parameter_values, likelihoods)
plt.axvline(x=max_likelihood_parameter, color='r', linestyle='--')
plt.xlabel('Difference in Peak Height')
plt.ylabel('Likelihood of Monolayer Graphene')
plt.title('Likelihood of Monolayer Graphene Based on Peak Ratio')
plt.show()

# Print the estimated parameter value and a confidence interval
# https://www.geeksforgeeks.org/numpy-searchsorted-in-python/
#https://www.statology.org/confidence-intervals-python/
confidence_level = 0.68
lower_index = np.searchsorted(likelihoods[:max_likelihood_index], np.max(likelihoods)*confidence_level)
upper_index = np.searchsorted(likelihoods[max_likelihood_index:], np.max(likelihoods)*confidence_level) + max_likelihood_index
lower_bound = parameter_values[lower_index]
upper_bound = parameter_values[upper_index]
print(f"Estimated parameter value: {max_likelihood_parameter:.3f}")
print(f"Confidence interval: [{lower_bound:.3f}, {upper_bound:.3f}]")

# parameter is the best difference of peaks to find monolayer graphene is raman spec

