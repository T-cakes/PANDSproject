import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Removes Limit of lines in Dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)
dataList = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"]
#reads in iris.data and details it for easier use
data = pd.read_csv('iris.data', delimiter= None, sep=',',header = None)
data.columns = dataList

#Writes to output.txt, a summary of each variables split into each flower category.
f = open('output.txt', 'w')
f.write(str(data.groupby(['Name']).describe()))
f.close()


plt.figure(1)
data['Sepal Length'].hist(bins = [0,1,2,3,4,5,6,7], color = 'red')
plt.title('Sepal Length')
plt.xlabel('sepal length in cm')
plt.ylabel('Amount')
plt.savefig('histogram/SepalLength.png')

plt.figure(2)
data['Sepal Width'].hist(bins = [0,1,2,3,4,5,6,7], color = 'orange')
plt.title('Sepal Width')
plt.xlabel('sepal width in cm')
plt.ylabel('Amount')
plt.savefig('histogram/SepalWidth.png')

plt.figure(3)
data['Petal Length'].hist(bins = [0,1,2,3,4,5,6,7])
plt.title('Petal Length')
plt.legend(['petal', 'sepal'])
plt.xlabel('petal length in cm')
plt.ylabel('Amount')
plt.savefig('histogram/PetalLength.png')

plt.figure(4)
data['Petal Width'].hist(bins = [0,1,2,3,4,5,6,7], color = 'indigo')
plt.title('Petal Width')
plt.xlabel('petal width in cm')
plt.ylabel('Amount')
plt.savefig('histogram/PetalWidth.png')

colors = {'Iris-setosa':'red', 'Iris-versicolor':'blue', 'Iris-virginica':'green'}


#https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
plt.figure(5)
fig, ax = plt.subplots()
grouped = data.groupby('Name')
for key, group in grouped:
    group.plot(ax=ax,kind='scatter', x = 'Sepal Length', y = 'Sepal Width',label=key, color = colors[key])
plt.savefig('ScatterPlots/SepalScatter.png')

plt.figure(6)
for key, group in grouped:
    group.plot(ax=ax,kind='scatter', x = 'Petal Length', y = 'Petal Width', color = colors[key])
plt.savefig('ScatterPlots/PetalScatter.png')
plt.show()