import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from pandas import Series, DataFrame
from pylab import *
import statsmodels.api as sm
from pandas_datareader import data, wb
from toolz import partitionby
from matplotlib.ticker import MaxNLocator
from scipy import stats
from __future__ import division

plt.rcParams['figure.figsize']= (11,7)
plt.style.use('fivethirtyeight')


df = pd.read_csv("/Users/justinnunez/Downloads/insights.csv")


df.head()
df.dtypes

len(df)

df['Cart Order'].value_counts()

# sb.pairplot(df, hue='Cart Order')

#sb.boxplot(x='Cart Order', y='Device Type', data = df)

#df.groupby(["catcher"])["pitch_type"].value_counts().plot(kind='bar')

df.groupby(['Device Type'])['Cart Order'].value_counts().plot(kind='bar')

df.groupby(['State'])[(df['Cart Order'] == 1)].plot(kind='bar')

df1 = df[df['Cart Order'] == 1]

len(df1) # 305 conversions
df1.groupby(['Device Type'])['Cart Order'].plot(kind='bar')



df1['Device Type'].value_counts()

df1['State'].value_counts()

df1['Country'].value_counts()

df1['traffic Source'].value_counts()

df1['City'].value_counts()


df1['Manufacturer'].value_counts()

df1['Zip Code'].value_counts()
df1['Landing Page Raw'].value_counts()

df1['Isp Name'].value_counts()
df1['Start Time'] = df1['Session Start Time'].str[0:7]
df1['Start Time'].value_counts()



# ****  VISUALS FOR PHONE ORDERS  ****

df2.head()
df2 = df[df['Phone Order'] == 1]
df2.head()

df2['Date Visited'] = df2['Session Start Time'].str[0:7]
df2['Device Type'].value_counts()
df2['State'].value_counts()
len(df2)

g = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df2, kind='count', size=7, aspect=.7)
sb.plt.title('Conversion on Mobile: Where did they come from? \n')
sb.despine()
g.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)

df2['Device Type'].value_counts()
## 
df2['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Phone Orders \n", weight='bold', fontsize= 28, alpha=.85)


a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df2, kind='count', size=7, aspect=.7)
sb.plt.title('Phone Orders: How many pages were clicked? \n')



# ***** VISUALS FOR  CART ORDERS
b = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df1, kind='count', size=7, aspect=.7)
sb.plt.title('Conversion on Cart Orders: Where did they come from? \n')
sb.despine()
b.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)


df1['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Cart Orders \n", weight='bold', fontsize= 28, alpha=.85)


a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df1, kind='count', size=7, aspect=.7)
sb.plt.title('Cart Orders: How many pages were clicked? \n')

df1['Device Type'].value_counts()
(len(df1)/len(df)) * 100
(len(df2)/len(df)) * 100






df['Device Type'].value_counts()



#   **** VISUALS FOR NO CONVERSION ** 


df5 = df[(df['Phone Order'] == 0) & (df['Cart Order'] == 0)]

df5['Device Type'].value_counts()

n = sb.factorplot(x='Device Type', hue='traffic Source',
              data=df5, kind='count', size=7, aspect=.7)
sb.plt.title('Non Conversion: Where did they come from? \n')
sb.despine()
n.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)



df5['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: No Conversion \n", weight='bold', fontsize= 28, alpha=.85)


c = sb.factorplot(x='Distinct Page Views', hue='Device Type',
              data=df5, kind='count', size=7, aspect=.7)
sb.plt.title('No Conversion: How many pages were clicked? \n')


### df5 is no conversion subset. Wanted to see where they were from, connection speed, etc,
#   to see if this was a cause for not converting.
df5['State'].value_counts()
df5['City'].value_counts()
df5['Connection Speed'].value_counts()
df5['Browser Name'].value_counts()
df5['Isp Name'].value_counts()
df5['traffic Source'].value_counts()

# .. same but checking data for conversion
df2['State'].value_counts()
df2['City'].value_counts()
df2['Connection Speed'].value_counts()
df2['Browser Name'].value_counts()

# .. same but checking data for conversion
df1['State'].value_counts()
df1['City'].value_counts()
df1['Connection Speed'].value_counts()
df1['Browser Name'].value_counts()


