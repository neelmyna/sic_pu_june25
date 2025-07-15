import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D plotting module

fruits = ['Mango', 'Apple', 'Banana', 'Grapes']
sales = [10, 20, 15, 25]

plt.bar(fruits, sales, color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Fruits")
plt.ylabel("Sales (lakh rupees)")
plt.legend()
plt.title("Bar Chart")
plt.show()