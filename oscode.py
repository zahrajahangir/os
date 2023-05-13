# Importing the essential libraries
import psutil
import GPUtil

# Testing the psutil library for both CPU and RAM performance details
print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)

# Testing the GPUtil library for both GPU performance details
GPUtil.showUtilization()

# Importing the numpy and visualization library
import numpy as np
import matplotlib.pyplot as plt

# Plotting the axis
plt.axis([0, 10, 0, 1])

# Creating a random scatter plot
for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)
plt.show()

# Importing the required libraries
import psutil
import GPUtil
import numpy as np
import matplotlib.pyplot as plt

# Creating an almost infinite for loop to monitor the details continuously
for i in range(100000000):

    # Obtaining all the essential details
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    print(cpu_usage)
    print(mem_usage)

    # Creating the scatter plot
    plt.scatter(i, cpu_usage, color = "red")
    plt.scatter(i, mem_usage, color = "blue")
    plt.legend(["CPU", "Memory"], loc ="lower right")
    plt.pause(0.05)

    # Obtaining the GPU details
    GPUtil.showUtilization()

# Plotting the information
plt.show()
