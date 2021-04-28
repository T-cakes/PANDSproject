# PANDSproject

 by

# Stephen Caulfield
---------------------------------------------------------
# Table of Contents

1. [History of Fishers Iris Data Set](#history-of-fishers-iris-data-set)

2. [Detailing the Data Set](#detailing-the-data-set)

3. [Analysis of Fishers Iris Data Set Using Python](#analysis-of-fishers-iris-data-set-using-python)

4. [Histogram Analysis](#histogram-analysis)

5. [References](#references)
---------------------------------------------------------

# History of Fishers Iris Data Set

<i>The Fisher's Iris Data set</i> was first founded by the British Statitician, geneticist and academic: <i>Ronald Aylmer Fisher</i>.[[1]](#references)

In 1936 he wrote an article titled <i>The Use of Multiple Measurements in Taxonomic Problems</i> in a journal called <i>Annals of Eugenics</i>.[[2]](#references)

In this article, he developed a linear function to differentiate various Iris species based on their Petal and Sepal lengths and widths. Those Iris species involve: Iris-Setosa, Iris-Versicolor and Iris-Virginica.

![alt text](https://camo.githubusercontent.com/74e378bb24b34efb63e8db09c4f073370d36f23aaa2c7580a805e93c881b78c2/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6173736574732e6461746163616d702e636f6d2f626c6f675f6173736574732f4d616368696e652b4c6561726e696e672b522f697269732d6d616368696e656c6561726e696e672e706e67)

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

![alt text](https://github.com/T-cakes/PANDSproject/blob/main/output.png)

The <i>mean</i> of each data set can tell us the comparisons between each class.

For example, when looking of the <i>mean sepal length</i> for each class we can determine on average that <b>Iris-Virginica's</b> have the longest sepals with an average of 6.588cm.

The <b>Iris-Setosa's</b> have the shortest sepals of all the iris's.


The <i>standard deviation(std)/i> shows us how widely the data varies. 

This information is useful as it gives us a better idea of the consistency of the data.

For example, when we look at the <i>std</i> for <i>petal length's</i> we see that the <b>Iris-Setosa</b> has very consistent <i> petal length's</i> as it has a low <i>std</i> of <b>0.173511.</b> This tells us that the statistics are reliable with less outlier's.

Compare this with the <i>std</i> of <b>Iris-Virginica's</b> <i>petal length</i> which is 0.551895. This shows that the data has a wider margin of lengths and may have more outliers on either the higher end or lower end.


The <i>range</i> is denoted by min, 25%, 50%, 75% and max. These values give more information on the <i>Standard Deviation</i> by showing the exact number and how much they differ from the above and a below intervals.

Following up with the <i>petal length's</i> again, with the <b>Iris-Setosa</b> we see that each interval are pretty similar in distance from eachother varying from 0.1 to 0.4 in distance from each other.

But also considering that the 50% and 75% intervals are the most closely equivalent to eachother shows that general number range is the most representative of this particular data set.

Comparing this with the <b>Iris-Virginica</b> <i>petal lengths</b> we see the distances for the first 4 intervals range from 0.325 to 0.6 which is somewhat unnotable, but with the 75% to max interval, there is a difference of 1.025 which tells us that there is either some extreme outliers on the higher end or that the <b>Iris-Virginica's</b> <i>petal length's</i> have an exponential growth past a certain point.
---------------------------------------------------------

# Histogram Analysis


# REFERENCES

[1] The Iris Dataset — A Little Bit of History and Biology - https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

[2] Annals of Human Genetics - https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x

[3] UCI Machine Learning Respository - https://archive.ics.uci.edu/ml/datasets/iris