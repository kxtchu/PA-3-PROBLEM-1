PA#3
Author: Nathan Josh Cacho
This project demonstrates basic pandas operations for data selection and indexing.

Cars Dataset Problem – loading a dataset of cars from a CSV file, and then subsetting rows to display only the first five and the last four entries.

The goal is to practice working with pandas DataFrames, specifically reading CSV files, applying logical conditions with .loc, and printing results in a clean format.

Below is how I approached the problem given and integrated it into code:

PROBLEM 1
For this task, I first loaded the dataset using pandas with the command:
cars = pd.read_csv('cars.csv')

The challenge was to extract only the first five rows and the last four rows of the dataset. Since the dataset had 32 entries, I used the DataFrame index and applied a condition with .loc

Here, (cars.index < 5) selects rows with indices 0 to 4 (the first five rows), while (cars.index > 26) selects rows with indices 27 to 31 (the last four rows). The OR (|) combines these two conditions.

Finally, I displayed the results with:
print("These are the first and last cars:")
cars1stlast


