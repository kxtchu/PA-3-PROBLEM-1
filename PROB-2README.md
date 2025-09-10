PA #2

Author: Nathan Josh Cacho

The goal is to practice pandas DataFrame operations such as .loc, conditional selection, and filtering by lists.

Below is how I approached the problems given and integrated them into code:

PROBLEM 2

(a). For this part, I had to display the first five rows with odd-numbered columns (1, 3, 5, ...). Using .loc, 
I explicitly selected the first five rows by their indices [0, 1, 2, 3, 4] and specified the corresponding odd-numbered columns by name: 
['Model', 'cyl', 'hp', 'wt', 'vs', 'gear']. This produced a compact DataFrame showing only the relevant data.

(b). The task here was to find the row that contains the car model "Mazda RX4". I applied a conditional filter using: cars.loc[cars['Model'] == 'Mazda RX4'] 
This returns the entire row where the "Model" column matches "Mazda RX4".

(c). For "Camaro Z28", I needed to determine the number of cylinders. I again used .loc but this time selected only the 'Model' and 'cyl' 
columns: cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']] This outputs the model name along with the cylinder count.

(d). Finally, I extracted both cylinders and gear type for three specific models: "Mazda RX4 Wag", "Ford Pantera L", and "Honda Civic". To do this efficiently, 
I used the .isin() method so that it will scan for the items in 'models': cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']] 
This returned a filtered DataFrame showing only those three models with their cylinder and gear info.
