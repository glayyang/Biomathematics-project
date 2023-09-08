import matplotlib.pyplot as plt


# Function to calculate the population of pythons at each time step
def calculate_python_population(r1, r2, ϱ1, ϱ2, P0, A0, m, t):
    popP = [P0]  # List to store python population sizes
    popA = [A0]  # List to store alligator population sizes

    for i in range(1, t + 1):
        tempP = (1 + r1) * popP[i - 1] - ϱ1 * popP[i - 1] * popA[i - 1] + m
        popP.append(tempP)

        tempA = (1 + r2) * popA[i - 1] - ϱ2 * popP[i - 1] * popA[i - 1]
        popA.append(tempA)

    return popP, popA


# Parameter values
r1 = 0.05
r2 = 0.05
ϱ1 = 0.0005
ϱ2 = 0.0005
P0 = 100
A0 = 100
m = 1
t = 50

# Calculate population dynamics
python_pop, alligator_pop = calculate_python_population(r1, r2, ϱ1, ϱ2, P0, A0, m, t)

# Plotting
time_steps = range(t + 1)

plt.plot(time_steps, python_pop, label="Pythons")
plt.plot(time_steps, alligator_pop, label="Alligators")
plt.xlabel("Time")
plt.ylabel("Population Size")
plt.legend()
plt.show()
