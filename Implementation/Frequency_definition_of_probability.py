import matplotlib.pyplot as plt
import random
import tkinter

def getting_data():
    try:
        TRIALS = int(input_box.get())
        plot_graph(TRIALS)
    except ValueError:
        print("Enter a valid integer")
def clear_graph():
    plt.close('all')
def plot_graph(trials):

    outcome = ["H","T"]
    required_outcome = "H"
    frequency = 0

    x = [] # for number of trials
    y = [] # for relative frequency


    for trial in range(1, trials + 1):
        trial_result = random.choice(outcome)

        if trial_result == required_outcome:
            frequency +=1

        relative_frequency = (frequency/trial)
        x.append(trial)
        y.append(relative_frequency)

    # plotting

    plt.plot(x,y)
    plt.title("Frequency definition of probability")
    plt.xlabel("No. of trials")
    plt.ylabel("Relative frequency")
    plt.grid(True)
    plt.show()



window = tkinter.Tk()

window.title("Probability Simulation")
window.minsize(width=300,height=80)
window.config(padx=20,pady=20)

my_label = tkinter.Label(text="No. of Trials", font= ("Arial",12,"bold"))
my_label.grid(column=0,row=0,columnspan=2,pady=10)

input_box = tkinter.Entry(width=10)
input_box.grid(column=0,row=1,padx=5,pady=5)

button =tkinter.Button(text="Run Simulation",command=getting_data)
button.grid(column=1,row=1,padx=5,pady=5)

button =tkinter.Button(text="Close",command=clear_graph)
button.grid(column=2,row=1,padx=5,pady=5)

window.mainloop()
