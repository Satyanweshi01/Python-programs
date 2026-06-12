import matplotlib.pyplot as plt
import random

outcome = ["H","T"]
required_outcome = ["H","T"]
frequency = 0
TRIALS= 10000


x = [] # for number of trials
y = [] # for relative frequency


for trial in range(1, TRIALS + 1):
    trial_result = random.choice(outcome)

    for i in required_outcome:
        if trial_result == i:
            frequency +=1

    relative_frequency = (frequency/trial)
    x.append(trial)
    y.append(relative_frequency)

# plotting
plt.plot(x,y)
plt.title("Frequency definition of probability")
plt.xlabel("No. of trials")
plt.ylabel("Relative frequency")
plt.show()