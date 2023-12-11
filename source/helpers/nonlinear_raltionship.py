

"""
This program is designed to determine the function representing the nonlinear relationship between voltage and another variable, such as temperature. To use the program, follow these steps:

1. Gather Data: Use a multimeter to measure different voltages and record the corresponding values of the variable you are measuring (e.g., temperature).

2. Input Data: Replace the values in the arrays below. The "Voltage" array should contain the voltage measurements, and the "temperature" array should contain the corresponding values of the measured variable.

3. Run the Program: Execute the program in a Python environment. Ensure you have the required libraries (NumPy, Matplotlib, and SciPy) installed.

The program employs an exponential decay model to fit the data and determine the relationship between voltage and the measured variable. The fitted function will be displayed, allowing you to predict the variable's values based on voltage.

Note: Make sure to have the necessary Python libraries installed by running `pip install numpy matplotlib scipy` in your terminal or command prompt.

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Given data
voltage = np.array([10.05, 8.85, 7.92, 7.30, 6.65])
temperature = np.array([100, 125, 150, 165, 180])

# Define the exponential decay model function
def exponential_decay(v, a, b):
    return a * np.exp(b * v)

# Fit the model to the data
params, covariance = curve_fit(exponential_decay, voltage, temperature)

# Extract the parameters
a_fit, b_fit = params

# Display the fitted exponential decay model
print(f"Fitted Exponential Decay Model: T(v) ≈ {a_fit:.2f} * e^({b_fit:.2f} * v)")

