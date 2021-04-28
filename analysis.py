# analysis.py

# Author: Stephen Caulfield

# This Program reads in the Fishers Iris Data Set(Iris.data) and 
# outputs various analyses on on the data set along with Histograms
# and Scatter Plots detailing the data.


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
f.write('Statistical Analysis of Fishers Iris Data Set \n')
f.write('=============================================== \n')
f.write(str(data.groupby(['Name']).describe()))
f.close()

#Allows each flower on graphs to be colour coded
grouped = data.groupby('Name')
colors = {'Iris-setosa':'red', 'Iris-versicolor':'orange', 'Iris-virginica':'purple'}

#Function for plotting all histograms
def plothist(column):
    #allows Plotting of each Flower type seperately in same graph
    fig, axes = plt.subplots()
    for key, group in grouped:
        #Plotting Histograms: https://www.dataindependent.com/pandas/pandas-histogram/
        group[column].plot(ax=axes, kind='hist', alpha = 0.4, title = column, bins = 10, grid=True,  color = colors[key])
    plt.legend(['Iris-setosa', 'iris-versicolor', 'iris-virginica'])
    plt.xlabel( column + ' in cm')
    plt.ylabel('Amount')
    plt.savefig('Histogram/'+ column + '.png')
    plt.show()

#Function for plotting all scatter plots
def plotscatter(measure1, measure2):
    #Plotting Scatter Plots: https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
    fig, axes = plt.subplots()
    for key, group in grouped:
        group.plot(ax=axes,kind='scatter', x = measure1, y = measure2, grid = True, label=key, color = colors[key])
    plt.savefig('ScatterPlots/'+ measure1 + "-" + measure2 + ' Scatter.png')
    plt.show()

#Each function call passes in column names for each graph
plothist('Sepal Length')
plothist('Sepal Width')
plothist('Petal Length')
plothist('Petal Width')
plotscatter('Sepal Length','Sepal Width')
plotscatter('Sepal Length','Petal Length')
plotscatter('Sepal Length','Petal Width')
plotscatter('Petal Length','Sepal Width')
plotscatter('Petal Length','Petal Width')
plotscatter('Sepal Width','Petal Width')

#Produces a pair plot of Histograms and scatterplot using seaborn
pp = sb.pairplot(data, hue = 'Name', diag_kind="hist")
pp.savefig("pairplot.png")