# Python Data Analysis and Visualization Project

This project demonstrates basic data analysis and visualization tasks using Python with the following libraries:

*   **pandas:** For data manipulation and analysis.
*   **numpy:** For numerical operations.
*   **matplotlib:** For data visualization.
*   **requests:** For making web requests and fetching data from APIs.

## Installation

Before running the code, ensure you have the necessary libraries installed. You can install them using pip:

```bash
pip install pandas numpy matplotlib requests
Project Structure
The project consists of a single Python script:

main.py
: Contains the main code that performs the data analysis and visualization tasks.
Usage
To run the project, simply execute the
main.py
script:

python main.py
Functionality
The
main.py
script performs the following tasks:

NumPy Array and Mean Calculation:

Creates a NumPy array containing numbers from 1 to 10.
Calculates the mean of the array using
numpy.mean()
.
Prints the calculated mean to the console.
Pandas DataFrame and Summary Statistics:

Loads a small, predefined dataset (in a dictionary format) into a pandas DataFrame. This dataset is defined directly within the script.
Displays summary statistics of the DataFrame using
pandas.DataFrame.describe()
.
Prints the summary statistics to the console.
API Data Fetching with Requests:

Fetches data from a public API (specifically, the JSON Placeholder API -
https://jsonplaceholder.typicode.com/todos/1
).
Parses the JSON response.
Prints the value associated with the "title" key from the JSON response to the console.
Handles potential errors during the API request (e.g., connection errors).
Matplotlib Line Graph:

Creates a simple list of numbers (e.g.,
[1, 3, 2, 4, 5]
).
Plots the list of numbers as a line graph using
matplotlib.pyplot.plot()
.
Adds a title to the graph.
Displays the graph using
matplotlib.pyplot.show()
. The graph will appear in a separate window.
Code Example (Snippet from main.py - Illustrative)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

# NumPy array and mean calculation
numpy_array = np.arange(1, 11)
mean_value = np.mean(numpy_array)
print(f"Mean of NumPy array: {mean_value}")

# Pandas DataFrame and summary statistics
data = {'col1': [1, 2, 3, 4, 5], 'col2': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)
print("\nDataFrame Summary Statistics:")
print(df.describe())

# API Data Fetching with Requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    json_data = response.json()
    print(f"\nAPI Title: {json_data['title']}")
except requests.exceptions.RequestException as e:
    print(f"Error fetching data from API: {e}")

# Matplotlib Line Graph
numbers = [1, 3, 2, 4, 5]
plt.plot(numbers)
plt.title("Simple Line Graph")
plt.show()