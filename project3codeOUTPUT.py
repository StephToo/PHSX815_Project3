import numpy as np
import matplotlib.pyplot as plt

def likelihood(data, parameter):
    sigma = np.std(data)
    return np.exp(-0.5*np.sum((data/parameter)**2))/((2*np.pi*parameter**2)**(len(data)/2))

# Read in the data from the text file
with open('simulated_data.txt', 'r') as file:
    data = [float(line) for line in file]

# Define a range of parameter values to test
parameter_values = np.linspace(0.1, 10, 1000)

# Calculate the likelihood for each parameter value and find the maximum likelihood value
likelihoods = [likelihood(data, p) for p in parameter_values]
max_likelihood_index = np.argmax(likelihoods)
max_likelihood_parameter = parameter_values[max_likelihood_index]

# Plot the likelihood as a function of the parameter value
plt.plot(parameter_values, likelihoods)
plt.axvline(x=max_likelihood_parameter, color='r', linestyle='--')
plt.xlabel('Parameter value')
plt.ylabel('Likelihood')
plt.title('Likelihood function for simulated data')
plt.show()

# Print the estimated parameter value and a confidence interval
confidence_level = 0.68
lower_index = np.searchsorted(likelihoods[:max_likelihood_index], np.max(likelihoods)*confidence_level)
upper_index = np.searchsorted(likelihoods[max_likelihood_index:], np.max(likelihoods)*confidence_level) + max_likelihood_index
lower_bound = parameter_values[lower_index]
upper_bound = parameter_values[upper_index]
print(f"Estimated parameter value: {max_likelihood_parameter:.3f}")
print(f"Confidence interval: [{lower_bound:.3f}, {upper_bound:.3f}]")

