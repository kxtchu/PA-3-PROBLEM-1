# %% [markdown]
# ## PROBLEM #2

# %%
import pandas as pd

# %%
# (a)
cars = pd.read_csv("cars.csv")
first_odd = cars.loc[[0, 1, 2, 3, 4], ['Model', 'cyl', 'hp', 'wt', 'vs', 'gear']]
print("a. First 5 rows with odd-numbered columns:")
first_odd

# %%
#(b)
mazda_rx4 = cars.loc[cars['Model'] == 'Mazda RX4']
print("\nb. Row that contains the Model of Mazda Rx4: ")
mazda_rx4

# %%
#(c)
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
print("\nc. Cylinders of Camaro Z28: ") 
camaro_cyl

# %%
#(d)
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
subset_models = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
print("\nd. Cylinders and gear of Mazda RX4 Wag, Ford Pantera L, Honda Civic: ")
subset_models

# %%



