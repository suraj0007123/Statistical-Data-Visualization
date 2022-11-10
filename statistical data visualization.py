import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data1=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\statistical data visualization\Statistical Datasets\Statistical Datasets\Q1_a.csv")

data1.info() # to info about the data


#### Exploratory data analysis 
# Measures of Central Tendency / First Moment of Business 
data1.speed.mean()
data1.speed.median()
data1.speed.mode()

# pip install numpy
from scipy import stats
stats.mode(data1.speed)

# Measures of Dispersion / Second moment business decision
data1.speed.var() # variance
data1.speed.std() # standard deviation

# Third moment business decision
data1.speed.skew()

# Fourth moment business decision
data1.speed.kurt()

plt.hist(data1.speed) #histogram


#### Exploratory data analysis 
# Measures of Central Tendency / First Moment of Business 
data1.dist.mean()
data1.dist.median()
data1.dist.mode()

# pip install numpy
from scipy import stats
stats.mode(data1.dist)

# Measures of Dispersion / Second moment business decision
data1.dist.var() # variance
data1.dist.std() # standard deviation

# Third moment business decision
data1.dist.skew()

# Fourth moment business decision
data1.dist.kurt()


plt.hist(data1.dist) #histogram


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data2=pd.read_csv(r"E:\DESKTOPFILES\suraj\assigments\statistical data visualization\Statistical Datasets\Statistical Datasets\Q2_b.csv")

data2.info() # To know info about the data

#### Exploratory data analysis 
# Measures of Central Tendency / First Moment of Business 
data2.SP.mean()
data2.SP.median()
data2.SP.mode()

# pip install numpy
from scipy import stats
stats.mode(data2.SP)

# Measures of Dispersion / Second moment business decision
data2.SP.var() # variance
data2.SP.std() # standard deviation

# Third moment business decision
data2.SP.skew()

# Fourth moment business decision
data2.SP.kurt()

plt.boxplot(data2.SP) # boxplot
plt.hist(data2.SP) #histogram


#### Exploratory data analysis 
# Measures of Central Tendency / First Moment of Business 
data2.WT.mean()
data2.WT.median()
data2.WT.mode()

# pip install numpy
from scipy import stats
stats.mode(data2.WT)

# Measures of Dispersion / Second moment business decision
data2.WT.var() # variance
data2.WT.std() # standard deviation

# Third moment business decision
data2.WT.skew()

# Fourth moment business decision
data2.WT.kurt()

plt.boxplot(data2.WT) # boxplot
plt.hist(data2.WT) #histogram

X=pd.Series([34,36,36,38,38,39,40,40,41,41,41,41,42,42,45,49,56])
X.mean()
X.median()
X.var()
X.std()

plt.boxplot(X)
