import matplotlib.pyplot as plt

# Loads data from the text file
# https://www.pythontutorial.net/python-basics/python-write-text-file/
with open('simulated_data.txt', 'r') as file:
    data = [line.strip().split(',') for line in file]

# Split  data into two sets based on the scenario number
# https://sparkbyexamples.com/python/python-convert-string-to-float/
# https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement
scenario1_data = [float(d[0]) for d in data if d[1] == '1']
scenario2_data = [float(d[0]) for d in data if d[1] == '2']

# Creates separate histograms for each scenario
# https://www.geeksforgeeks.org/how-to-plot-two-histograms-together-in-matplotlib/
plt.hist(scenario1_data, bins=35, alpha=0.5, label='Scenario 1')
plt.hist(scenario2_data, bins=35, alpha=0.5, label='Scenario 2')

# Add labels and title to the plot, legend, show, histograms on top of eachother
# https://www.geeksforgeeks.org/how-to-plot-data-from-a-text-file-using-matplotlib/
plt.xlabel('Deviation from 175 cm')
plt.ylabel('Amount of Adult Males')
plt.title('Adult Male Height Comparison')

plt.legend()

plt.show()

