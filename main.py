import pandas as pd
import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("Data Collection - Summary.csv")
    trial_names = ["Pos1_3sens_floor", "Pos1_3sens_chair",
                   "Pos2_3sens_floor", "Pos2_3sens_chair",
                   "Pos1_6sens_floor", "Pos1_6sens_chair",
                   "Pos2_6sens_floor", "Pos2_6sens_chair"
                   ]

    fig = plt.plot()
    for i in range(len(trial_names)):
        trial_name = trial_names[i]
        x = list(df.loc[i, ["Average X1", "Average X2", "Average X3"]])
        y = list(df.loc[i, ["Average Y1", "Average Y2", "Average Y3"]])
        plt.scatter(x, y)

    footprint = pd.read_csv("Default-Dataset.csv", header=None)
    plt.plot(footprint[0], footprint[1], '-', color="black")
    plt.axis('equal')
    plt.title("Centre of Pressure for Different Trials")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.xlim([-3, 3])
    plt.ylim([-4, 21])
    plt.legend(trial_names)
    plt.savefig("cop.png")
    plt.show()

