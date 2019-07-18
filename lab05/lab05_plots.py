from datascience import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")

hybrid = Table.read_table("data/hybrid.csv")
by_class = hybrid.group("class", np.mean)
sorted_by_acceleration = hybrid.sort("acceleration")

def part_3_plot_1():
    plt.figure(figsize=[20,15])
    plt.suptitle("Do acceleration and mpg increase together?", size=20)
    plt.subplots_adjust(top=.9)

    plt.subplot(221)
    plt.bar(np.arange(by_class.num_rows), by_class.column("acceleration mean"), width=.3)
    plt.bar(np.arange(by_class.num_rows) + 0.5, by_class.column("mpg mean"), width=.3)
    plt.xticks(np.arange(by_class.num_rows) + 0.25, by_class.column("class"))
    plt.xlabel("Class")
    plt.ylabel("Mean Value")
    plt.legend(["Acceleration", "MPG"])
    plt.title("Plot A")

    plt.subplot(222)
    plt.hist(hybrid.column("acceleration"), alpha=0.5)
    plt.hist(hybrid.column("mpg"), alpha=0.5)
    plt.xlabel("Variable Distribution")
    plt.legend(["Acceleration", "MPG"])
    plt.title("Plot B")

    plt.subplot(223)
    plt.plot(sorted_by_acceleration.column("acceleration"), sorted_by_acceleration.column("mpg"))
    plt.xlabel("Acceleration")
    plt.ylabel("MPG")
    plt.title("Plot C")

    plt.subplot(224)
    plt.barh(np.arange(by_class.num_rows), by_class.column("acceleration mean"), height=.3)
    plt.barh(np.arange(by_class.num_rows) + 0.5, by_class.column("mpg mean"), height=.3)
    plt.yticks(np.arange(by_class.num_rows) + 0.25, by_class.column("class"))
    plt.ylabel("Class")
    plt.xlabel("Mean Value")
    plt.legend(["Acceleration", "MPG"])
    plt.title("Plot D");
    
def part_3_plot_2():
    plt.figure(figsize=[20,15])
    plt.suptitle("What is the distribution of the acceleration values?", size=20)
    plt.subplots_adjust(top=.9)

    plt.subplot(221)
    plt.bar(np.arange(by_class.num_rows), by_class.column("msrp mean"))
    plt.xticks(np.arange(by_class.num_rows), by_class.column("class"))
    plt.xlabel("Class")
    plt.ylabel("MSRP Mean")
    plt.title("Plot A")

    plt.subplot(222)
    plt.scatter(hybrid.column("msrp"), hybrid.column("acceleration"))
    plt.xlabel("MSRP")
    plt.ylabel("Acceleration")
    plt.title("Plot B")

    plt.subplot(223)
    plt.scatter(hybrid.column("acceleration"), hybrid.column("msrp"))
    plt.xlabel("Acceleration")
    plt.ylabel("MSRP")
    plt.title("Plot C")

    plt.subplot(224)
    plt.hist(hybrid.column("acceleration"))
    plt.xlabel("Acceleration")
    plt.title("Plot D");
    
def part_3_plot_3():
    plt.figure(figsize=[20,15])
    plt.suptitle("How does the class affect the acceleration?", size=20)
    plt.subplots_adjust(top=.9)

    plt.subplot(221)
    plt.barh(np.arange(by_class.num_rows), by_class.column("acceleration mean"))
    plt.yticks(np.arange(by_class.num_rows), by_class.column("class"))
    plt.xlabel("Acceleration Mean")
    plt.ylabel("Class")
    plt.title("Plot A")

    plt.subplot(222)
    plt.hist(hybrid.column("acceleration"), bins=5)
    plt.xlabel("Acceleration")
    plt.title("Plot B")

    plt.subplot(223)
    plt.hist(hybrid.column("acceleration"), bins=40)
    plt.xlabel("Acceleration")
    plt.title("Plot C")

    plt.subplot(224)
    plt.plot(sorted_by_acceleration.column("msrp"), sorted_by_acceleration.column("acceleration"))
    plt.xlabel("MSRP")
    plt.ylabel("Acceleration")
    plt.title("Plot D");
    
def part_3_plot_4():
    plt.figure(figsize=[20,15])
    plt.suptitle("What is the distribution of the MPG values?", size=20)
    plt.subplots_adjust(top=.9)

    plt.subplot(221)
    plt.hist(hybrid.column("mpg"), bins=5)
    plt.title("Plot A")

    plt.subplot(222)
    plt.hist(hybrid.column("mpg"), bins=10)
    plt.title("Plot B")

    plt.subplot(223)
    plt.hist(hybrid.column("mpg"), bins=15)
    plt.title("Plot C")

    plt.subplot(224)
    plt.hist(hybrid.column("mpg"), bins=20)
    plt.title("Plot D");