import matplotlib.pyplot as plt

# line 1 points
import pandas
from numpy.matlib import randn
from pandas import Series, date_range

x1 = [1, 2, 3]
y1 = [2, 4, 1]
# plotting the line 1 points
plt.plot(x1, y1, label="line 1")

# line 2 points
x2 = [1, 2, 3]
y2 = [4, 1, 3]
# plotting the line 2 points
plt.plot(x2, y2, label="line 2")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Two lines on same graph!')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()

# ts = Series(randn(1000), index=date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# df = pandas.DataFrame(randn(1000, 4), index=ts.index, columns=list('ABCD'))
# df = df.cumsum()
# plt.figure(); df.plot(); plt.legend(loc='best')

pass
