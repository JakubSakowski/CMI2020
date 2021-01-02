import sys
import pandas as pd 

# reading the data
df = pd.read_csv(sys.stdin, skiprows = 1, names = ['x', 'y'], sep = " ")

# printing the data
# print(df)

# finding min and max values
xmin = df['x'].min()
xmax = df['x'].max()
ymin = df['y'].min()
ymax = df['y'].max()
# print (xmin, xmax, ymin, ymax)

# calculating the perimeter of the fence\
a = xmax - xmin + 4 
b = ymax - ymin + 4
fencePerimeter = (2 * a + 2 * b)

# printing the perimeter of the fence
print(fencePerimeter)