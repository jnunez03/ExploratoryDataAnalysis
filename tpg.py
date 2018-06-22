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

df['Session Id'].value_counts()


dfsession1 = df[df['Session Id'] == "03ee5add-410d-4be2-8458-0a277ab741bd"]
dfsession2 = df[df['Session Id'] == '00cad8c8-094d-4dbb-894c-88984c76e2d3']
dfsession3 = df[df['Session Id'] == '01c400f2-1aec-41d7-a62d-10a87fb7658b']


# Drop duplicate session Id's

df.drop_duplicates(['Session Id'], keep='last')

df['Session Id'].value_counts()
len(df) # 20189

df['Device Type'].value_counts()


len(df)

df['Cart Order'].value_counts()

# sb.pairplot(df, hue='Cart Order')

#sb.boxplot(x='Cart Order', y='Device Type', data = df)

#df.groupby(["catcher"])["pitch_type"].value_counts().plot(kind='bar')

df.groupby(['Device Type'])['Cart Order'].value_counts().plot(kind='bar')

df.groupby(['State'])[(df['Cart Order'] == 1)].plot(kind='bar')



df2 = df[df['Phone Order'] == 1]


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

## 
df2['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Phone Orders \n", weight='bold', fontsize= 28, alpha=.85)


a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df2, kind='count', size=7, aspect=.7)
sb.plt.title('Phone Orders: How many pages were clicked? \n')



# CART ORDERS
df1 = df[df['Cart Order'] == 1]


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

# subset conversion calculation!
(len(df1)/len(df)) * 100
(len(df2)/len(df)) * 100



df5 = df[(df['Phone Order'] == 0) & (df['Cart Order'] == 0)]

df5['Device Type'].value_counts()
df5['Session Id'].value_counts()

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


### Differences
df5['State'].value_counts()
df5['City'].value_counts()
df5['Connection Speed'].value_counts()
df5['Browser Name'].value_counts()
df5['Isp Name'].value_counts()
df5['traffic Source'].value_counts()
df5['Device Type'].value_counts()


df2['State'].value_counts()
df2['City'].value_counts()
df2['Connection Speed'].value_counts()
df2['Browser Name'].value_counts()
df2['Isp Name'].value_counts()
df2['traffic Source'].value_counts()
len(df2)

df1['State'].value_counts()
df1['City'].value_counts()
df1['Connection Speed'].value_counts()
df1['Browser Name'].value_counts()
df1['Isp Name'].value_counts()
df1['traffic Source'].value_counts()

dfnon = df[df['Isp Name'] == "time warner cable internet llc"]
len(dfnon)

df7 = df[(df['Phone Order'] == 1) & (df['Isp Name'] == "time warner cable internet llc")]
df8 = df[(df['Cart Order'] == 1) & (df['Isp Name'] == "time warner cable internet llc")]
df9 = df[(df['Isp Name'] == "time warner cable internet llc") & (df['Phone Order'] == 0) & (df['Cart Order'] == 0)]

len(df7) + len(df8)
len(df8)

len(df9)

#       ***   PLOTS FOR TIME WARNER CUSTOMERS    *** 

# PLOT 1 
b = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df7, kind='count', size=7, aspect=.7)

sb.plt.title('Conversion on Phone Orders: Time Warner Customers \n')
sb.despine()
b.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)
#  PLOT  2

df7['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Phone Orders \n", weight='bold', fontsize= 28, alpha=.85)

# PLOT 3 
a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df7, kind='count', size=7, aspect=.7)
sb.plt.title('Phone Orders: How many pages were clicked? \n')


df7['State'].value_counts()
df7['Connection Speed'].value_counts()
df7['Browser Name'].value_counts()
df7['Isp Name'].value_counts()
df7['traffic Source'].value_counts()
df7['Device Type'].value_counts()
df7['Landing Page Raw'].value_counts()

# NOW df8

j = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df8, kind='count', size=7, aspect=.7)

sb.plt.title('Conversion on Cart Orders: Time Warner Customers \n')
sb.despine()
j.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)
#  PLOT  2

df8['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Cart Orders on Time Warner Customers \n", weight='bold', fontsize= 28, alpha=.85)

# PLOT 3 
a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df8, kind='count', size=7, aspect=.7)
sb.plt.title('Cart Orders: How many pages were clicked? \n')


df8['State'].value_counts()
df8['Connection Speed'].value_counts()
df8['Browser Name'].value_counts()
df8['Isp Name'].value_counts()
df8['traffic Source'].value_counts()
df8['Device Type'].value_counts()
df8['Landing Page Raw'].value_counts()



## NON-Conversion NOW for Time Warner

q = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df9, kind='count', size=7, aspect=.7)

sb.plt.title('Time Warner Customers Who Did Not Convert \n')
sb.despine()
q.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)
#  PLOT  2

df9['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Non-Conversion Time Warner Customers \n", weight='bold', fontsize= 28, alpha=.85)

# PLOT 3 
h = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df9, kind='count', size=7, aspect=.7)
sb.plt.title('Time Warner (Non-Conversion): How many pages were clicked? \n')


df9['State'].value_counts()
df9['Connection Speed'].value_counts()
df9['Browser Name'].value_counts()
df9['Isp Name'].value_counts()
df9['traffic Source'].value_counts()
df9['Device Type'].value_counts()
df9['Landing Page Raw'].value_counts()


#   ****     Model:   Random Forest

dfsub1 = df[df['Isp Name'].isin(["frontier communications of america inc.",
                                 "time warner cable internet llc",
                                 "comcast cable communications inc.",
                                 "verizon wireless",
                                 "mci communications services inc. dba verizon business",
                                 "att internet services",
                                 "qwest communications company llc",
                                 "att mobility llc",
                                 "southern new england telephone company and snet america inc.",
                                 "t-mobile usa inc.",
                                 "charter communications"])]

dfsub2 = dfsub1[dfsub1["State"].isin(["ca","fl","tx","ct","in","pa","wa","il","ny","az","oh"])]

dfsub3 = dfsub2[dfsub2["Browser Name"].isin(["Chrome","Safari","Chrome Mobile","Internet Explorer", "Edge", "Firefox"])]

dfsub3['Browser Name'].value_counts()

del dfsub3['Landing Page Raw']
del dfsub3['Order ID']
del dfsub3['Zip Code']
del dfsub3['Os Name']
del dfsub3['Metro Name']
del dfsub3['Manufacturer']
del dfsub3['Country']
del dfsub3['Connection Speed']
del dfsub3['Session Start Time']
del dfsub3['Session Id']
del dfsub3['City']


dfsub3['Phone Order'].value_counts()
dfsub3['Cart Order'].value_counts()

dfsub4 = pd.get_dummies(dfsub3)
dfsub4.dtypes
dfsub4.head()

# We want to predict Phone Orders!
labels = np.array(dfsub4['Phone Order'])

# Drop our target variable from our data!
dfsub5 = dfsub4.drop('Phone Order', axis = 1)
# Drop cart order. We wont use it to predict phone orders.
dfsub5 = dfsub5.drop('Cart Order', axis = 1)

# Save variable name to list
df_list = list(dfsub5.columns)

# Convert to numpy array
dfsub5 = np.array(dfsub5)

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(dfsub5, labels, test_size = 0.25, random_state = 42)


# Check the shape
train_features.shape
train_labels.shape
# We split our data and we can see difference in amount of data
test_features.shape
test_labels.shape


# Algorithm
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(train_features, train_labels)


predictions = rf.predict(test_features)


print('Train score: ', rf.score(train_features, train_labels))
print('Test Score: ', rf.score(test_features, test_labels))

importances = list(rf.feature_importances_)

feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(df_list, importances)]


feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

print(feature_importances)






# Set the style
plt.style.use('fivethirtyeight')
# list of x locations for plotting
x_values = list(range(len(importances)))
# Make a bar chart
plt.bar(x_values, importances, orientation = 'vertical')
# Tick labels for x axis
plt.xticks(x_values, df_list, rotation='vertical')
# Axis labels and title
plt.ylabel('Importance'); plt.xlabel('Variable'); plt.title('Variable Importances');
