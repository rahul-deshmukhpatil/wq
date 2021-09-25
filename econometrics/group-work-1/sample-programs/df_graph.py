# Import pandas library
import matplotlib.pyplot as plt
import pandas as pd


# initialize list of lists
data = [[1, 10, 3.3], [2, 15, 1.2], [3, 14, 3.4]]
data1 = [[1, 15, 4.5], [2, 5, 5.4], [3, 10, 3.5]]

# Create the pandas DataFrame
df1 = pd.DataFrame(data, columns=['Name', 'Age' , 'Price'])

# print dataframe.
plt.figure()
df1.plot(x='Name')
plt.legend(loc='best')
plt.show()

