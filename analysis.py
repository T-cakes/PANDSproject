import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

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

grouped = data.groupby('Name')
colors = {'Iris-setosa':'red', 'Iris-versicolor':'orange', 'Iris-virginica':'purple'}

def plothist(dim):
    fig, ax = plt.subplots()
    for key, group in grouped:
        #https://www.dataindependent.com/pandas/pandas-histogram/
        group[dim].plot(ax=ax, kind='hist', alpha = 0.4, title = dim, bins = 10, grid=True,  color = colors[key])
    plt.legend(['Iris-setosa', 'iris-versicolor', 'iris-virginica'])
    plt.xlabel( dim + ' in cm')
    plt.ylabel('Amount')
    plt.savefig('histogram/'+ dim + '.png')
    plt.show()
    plt.close()

def scatplot(mes):
    #https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
    fig, ax = plt.subplots()
    for key, group in grouped:
        group.plot(ax=ax,kind='scatter', x = mes + ' Length', y = mes + ' Width', grid = True, label=key, color = colors[key])
    plt.savefig('ScatterPlots/'+ mes +' Scatter.png')
    plt.show()
    plt.close()

plothist('Sepal Length')
plothist('Sepal Width')
plothist('Petal Length')
plothist('Petal Width')
scatplot('Sepal')
scatplot('Petal')