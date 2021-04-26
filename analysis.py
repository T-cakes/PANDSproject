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

#Allows each flower on graphs to be colour coded
grouped = data.groupby('Name')
colors = {'Iris-setosa':'red', 'Iris-versicolor':'orange', 'Iris-virginica':'purple'}

#Function for plotting all histograms
def plothist(dim):
    #allows Plotting of each Flower type seperately in same graph
    fig, ax = plt.subplots()
    for key, group in grouped:
        #Plotting Histograms: https://www.dataindependent.com/pandas/pandas-histogram/
        group[dim].plot(ax=ax, kind='hist', alpha = 0.4, title = dim, bins = 10, grid=True,  color = colors[key])
    plt.legend(['Iris-setosa', 'iris-versicolor', 'iris-virginica'])
    plt.xlabel( dim + ' in cm')
    plt.ylabel('Amount')
    plt.savefig('histogram/'+ dim + '.png')
    plt.show()

#Function for plotting all scatter plots
def scatplot(mes1, mes2):
    #Plotting Scatter Plots: https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
    fig, ax = plt.subplots()
    for key, group in grouped:
        group.plot(ax=ax,kind='scatter', x = mes1, y = mes2, grid = True, label=key, color = colors[key])
    plt.savefig('ScatterPlots/'+ mes1 + "-" + mes2 + ' Scatter.png')
    plt.show()


plothist('Sepal Length')
plothist('Sepal Width')
plothist('Petal Length')
plothist('Petal Width')
scatplot('Sepal Length','Sepal Width')
scatplot('Sepal Length','Petal Length')
scatplot('Sepal Length','Petal Width')
scatplot('Petal Length','Sepal Width')
scatplot('Petal Length','Petal Width')
scatplot('Sepal Width','Petal Width')

#Produces a pair plot of Histograms and scatterplot using seaborn
pp = sb.pairplot(data, hue = 'Name', diag_kind="hist")
pp.savefig("pairplot.png")