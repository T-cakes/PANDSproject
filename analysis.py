import pandas as pd
import numpy as np

#Removes Limit of lines in Dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)

#reads in iris.data and details it for easier use
data = pd.read_csv('iris.data', delimiter= None, sep=',',header = None)
data.columns =["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"]

#Writes to output.txt, a summary of each variables split into each flower category.
f = open('output.txt', 'w')
f.write(str(data.groupby(['Name']).describe()))
f.close()

