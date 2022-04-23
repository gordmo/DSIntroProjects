import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#generate a sequence of numbers from -10 to 10
x = np.linspace(-10, 10, 100)
#create a second array using sine
y = np.sin(x)
#The plot function makes a line chart of one array against another
plt.plot(x, y, marker="x")

#create a simple dataset of names, locations and ages
data = {'Name': ['Tom', 'Jack', 'Steve', 'Ricky'],
        "Location": ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen'],
        "age": [28, 34, 29, 42]}

data_pandas = pd.DataFrame(data)
#IPython.display allows "pretty printing" of dataframes
# in the Jupyter notebook but im in vscode rn so i cant use it
display(data_pandas)
#select all rows with an age column greater than 30
display(data_pandas[data_pandas.age > 30])
 