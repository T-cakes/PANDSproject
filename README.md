# PANDSproject

 by

# Stephen Caulfield
# Table of Contents

1. [History of Fishers Iris Data Set](#history-of-fishers-iris-data-set)

2. [Code Explanation](#code-explanation)
    - [Imported Libraries](#imported-libraries)
    - [Reading the data File](#reading-the-data-file)
    - [Writing Analysis to txt File](#writing-analysis-to-txt-file)
    - [Histogram Code](#histogram-code)
    - [Scatter Plot Code](#scatter-plot-code)
    - [Pair Plot Code](#pair-plot-code)
3. [Detailing the Data Set](#detailing-the-data-set)

4. [Analysis of Fishers Iris Data Set Using Python](#analysis-of-fishers-iris-data-set-using-python)
    - [Table Overview](#table-overview)
    - [Mean](#mean)
    - [Standard Deviation](#standard-deviation)
    - [Range](#range)

5. [Plots](#plots)
    - [Histogram Analysis](#histogram-analysis)
    - [Scatter Plots](#scatter-plots)
    - [Pair Plot](#pair-plot)

6. [Technologies Used](#technologies-used)

7. [References](#references)


# History of Fishers Iris Data Set

<i>The Fisher's Iris Data set</i> was first founded by the British Statitician, geneticist and academic: <i>Ronald Aylmer Fisher</i>.[[1]](#references)

In 1936 he wrote an article titled <i>The Use of Multiple Measurements in Taxonomic Problems</i> in a journal called <i>Annals of Eugenics</i>.[[2]](#references)

In this article, he developed a linear function to differentiate various Iris species based on their Petal and Sepal lengths and widths. Those Iris species involve: Iris-Setosa, Iris-Versicolor and Iris-Virginica.

![alt text](https://camo.githubusercontent.com/74e378bb24b34efb63e8db09c4f073370d36f23aaa2c7580a805e93c881b78c2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6173736574732e6461746163616d702e636f6d2f626c6f675f6173736574732f4d616368696e652b4c6561726e696e672b522f697269732d6d616368696e656c6561726e696e672e706e67)



# Code Explanation

 ## Imported Libraries

 ```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
 ```

 ## Reading the data File

```python
#Removes Limit of lines in Dataframe
pd.set_option("display.max_rows", None, "display.max_columns", None)
dataList = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Name"]

#reads in iris.data and details it for easier use
data = pd.read_csv('iris.data', delimiter= None, sep=',',header = None)
data.columns = dataList
```

 ## Writing Analysis to txt File

```python
#Writes to output.txt, a summary of each variables split into each flower category.
f = open('output.txt', 'w')
f.write('Statistical Analysis of Fishers Iris Data Set \n')
f.write('=============================================== \n')
f.write(str(data.groupby(['Name']).describe()))
f.write('\n\nAll measurements are in centimetres(cm)')
f.close()
```

 ## Histogram Code

The function I wrote that creates the histogram passes in a string that one of the measurement columns. This then applies that string to all areas that specific data is required of referenced.\

I used matplotlib to create and detail the histograms and it proved to have all the tools need for a satisfactory histogram\

I originally had several different blocks of code to create each histogram, but I realised this was a lot of repetition and that it could be condensed into a singular function with a string argument passed in.

```python
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
```

 ## Scatter Plot Code

The function I wrote for creating scatter plots is similar in nature to my histogram plotting function, with the only difference being I passed in two strings for a pair of data sets to create the scatter plot.

6 scatter plots are created through this, 1 for each pairing of data sets.

```python
#Function for plotting all scatter plots
def plotscatter(measure1, measure2):
    #Plotting Scatter Plots: https://kanoki.org/2020/08/30/matplotlib-scatter-plot-color-by-category-in-python/
    fig, axes = plt.subplots()
    for key, group in grouped:
        group.plot(ax=axes,kind='scatter', x = measure1, y = measure2, grid = True, label=key, color = colors[key])
    plt.savefig('ScatterPlots/'+ measure1 + "-" + measure2 + ' Scatter.png')
    plt.show()
```

## Pair Plot Code

This plot was created using seaborn, and I mostly wanted to make it to be a more compact set of graphs in one image that allowed overview all possible data set pairings with ease.

The one issue with these pair plots is that they have repeating graph's that are just inverted in some fashion.

```python
pp = sb.pairplot(data, hue = 'Name', diag_kind="hist")
pp.savefig("pairplot.png")
```

# Detailing the Data Set

The data set that I used comes from the <i>University of California Irvine(UCI) Machine Learning Respository</i>[[3]](#references)

The data file itself did not detail the column names so I named them according to the websites[[3]](#references) detail as follows:

    1. Sepal Length
    2. Sepal Width
    3. Petal Length
    4. Petal Width
    5. Name

The data set contains 3 classes detailed by name with 50 instances each with those classes being[[3]](#references):

    1. Iris-Setosa
    2. Iris-Versicolor
    3. Iris-Virginica

Every numeric value on the table is a centimetre(cm) unit value.

# Analysis of Fishers Iris Data Set Using Python

## Table Overview

The data analysis I have performed through python provides various statistical observations which are split up by the first four columns and then further split up by the classes.

The analysis provides the count of each data set

the mean of those specific values (e.g. Mean of Sepal Length of all Iris-Setosa etc.).

The <i>Standard</i> Deviation of data.

And the range of the data in 25% intervals.

```
        Statistical Analysis of Fishers Iris Data Set 

    ===============================================
    
                    Sepal Length                                              \
                        count   mean       std  min    25%  50%  75%  max   
    Name                                                                       
    Iris-setosa             50.0  5.006  0.352490  4.3  4.800  5.0  5.2  5.8   
    Iris-versicolor         50.0  5.936  0.516171  4.9  5.600  5.9  6.3  7.0   
    Iris-virginica          50.0  6.588  0.635880  4.9  6.225  6.5  6.9  7.9   

                    Sepal Width                                                \
                        count   mean       std  min    25%  50%    75%  max   
    Name                                                                        
    Iris-setosa            50.0  3.418  0.381024  2.3  3.125  3.4  3.675  4.4   
    Iris-versicolor        50.0  2.770  0.313798  2.0  2.525  2.8  3.000  3.4   
    Iris-virginica         50.0  2.974  0.322497  2.2  2.800  3.0  3.175  3.8   

                    Petal Length                                               \
                        count   mean       std  min  25%   50%    75%  max   
    Name                                                                        
    Iris-setosa             50.0  1.464  0.173511  1.0  1.4  1.50  1.575  1.9   
    Iris-versicolor         50.0  4.260  0.469911  3.0  4.0  4.35  4.600  5.1   
    Iris-virginica          50.0  5.552  0.551895  4.5  5.1  5.55  5.875  6.9   

                    Petal Width                                            
                        count   mean       std  min  25%  50%  75%  max  
    Name                                                                   
    Iris-setosa            50.0  0.244  0.107210  0.1  0.2  0.2  0.3  0.6  
    Iris-versicolor        50.0  1.326  0.197753  1.0  1.2  1.3  1.5  1.8  
    Iris-virginica         50.0  2.026  0.274650  1.4  1.8  2.0  2.3  2.5  
```

This Table was created using this code:
```python
f = open('output.txt', 'w')
f.write('Statistical Analysis of Fishers Iris Data Set \n')
f.write('=============================================== \n')
f.write(str(data.groupby(['Name']).describe()))
f.close()
```

## Mean

The <i>mean</i> of each data set can tell us the comparisons between each class.

For example, when looking of the <i>mean sepal length</i> for each class we can determine on average that <b>Iris-Virginica's</b> have the longest sepals with an average of 6.588cm.

The <b>Iris-Setosa's</b> have the shortest <i>sepal length's</i> of all the Iris's.

## Standard Deviation

The <i>standard deviation(std)</i> shows us how widely the data varies. 

This information is useful as it gives us a better idea of the consistency of the data.

For example, when we look at the <i>std</i> for <i>petal length's</i> we see that the <b>Iris-Setosa</b> has very consistent <i> petal length's</i> as it has a low <i>std</i> of <b>0.173511.</b> This tells us that the statistics are reliable with less outlier's.

Compare this with the <i>std</i> of <b>Iris-Virginica's</b> <i>petal length</i> which is 0.551895. This shows that the data has a wider margin of lengths and may have more outliers on either the higher end or lower end.

## Range

The <i>range</i> is denoted by min, 25%, 50%, 75% and max. These values give more information on the <i>Standard Deviation</i> by showing the exact number and how much they differ from the above and a below intervals.

Following up with the <i>petal length's</i> again, with the <b>Iris-Setosa</b> we see that each interval are pretty similar in distance from eachother varying from 0.1 to 0.4 in distance from each other.

But also considering that the 50% and 75% intervals are the most closely equivalent to eachother shows that general number range is the most representative of this particular data set.

Comparing this with the <b>Iris-Virginica</b> <i>petal lengths</b> we see the distances for the first 4 intervals range from 0.325 to 0.6 which is somewhat unnotable, but with the 75% to max interval, there is a difference of 1.025 which tells us that there is either some extreme outliers on the higher end or that the <b>Iris-Virginica's</b> <i>petal length's</i> have an exponential growth past a certain point.


# Plots

## Histogram Analysis


![alt text](https://github.com/T-cakes/PANDSproject/blob/main/histogram/Sepal%20Length.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/histogram/Sepal%20Width.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/histogram/Petal%20Length.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/histogram/Petal%20Width.png)


## Scatter Plots Analysis

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/ScatterPlots/Petal%20Length-Petal%20Width%20Scatter.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/ScatterPlots/Petal%20Length-Sepal%20Width%20Scatter.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/ScatterPlots/Sepal%20Length-Petal%20Length%20Scatter.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/ScatterPlots/Sepal%20Length-Petal%20Width%20Scatter.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/ScatterPlots/Sepal%20Length-Sepal%20Width%20Scatter.png)

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/ScatterPlots/Sepal%20Width-Petal%20Width%20Scatter.png)


## Pair Plot

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/pairplot.png)


# REFERENCES

[1] The Iris Dataset — A Little Bit of History and Biology - https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

[2] Annals of Human Genetics - https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x

[3] UCI Machine Learning Respository - https://archive.ics.uci.edu/ml/datasets/iris

# Technologies Used

- Visual Studio Code - version 1.55.2
- Anaconda3
- Python - version 3.8.5 64 bit
- Google Chrome