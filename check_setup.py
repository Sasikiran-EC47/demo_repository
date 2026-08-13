import sys
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("Python Version:", sys.version.split()[0])
print("NumPy Version:", np.__version__)
print("Pandas:", pd.__version__)
print("Matplotlib:", matplotlib.__version__)
print("Roll Number: 25EC01047")

# A one-line smoke test of the plotting back-end
plt.plot([0, 1, 2, 3], [0, 1, 4, 9], marker="o")
plt.title("If you can see this window, the setup works")
plt.xlabel("horizontal axis")
plt.ylabel("x squared")
plt.grid(True)
plt.show()
print("date of birth 23:10:2007")