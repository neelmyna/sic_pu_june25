import numpy as np
# Replacing values less than 50 with 0 in an array

# Explanation: Using np.where() to replace values meeting the condition

expenses = np.array([20, 60, 5, 80, 45, 90])
modified_expenses = np.where(expenses < 50, 0, expenses)
print(modified_expenses)  # Output: [ 0 60  0 80  0 90]