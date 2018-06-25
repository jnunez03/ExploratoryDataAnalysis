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



# reading in the data set using pandas
df = pd.read_csv("/Users/justinnunez/Downloads/insights.csv")


# Get a general sense of what the data looks like and how its stored.
df.head()
df.dtypes


# Check for unique session ID's. We don't want to double count customers.
df['Session Id'].value_counts()

# This code below tests if duplicated session ID's have identical data for other variables.
dfsession1 = df[df['Session Id'] == "03ee5add-410d-4be2-8458-0a277ab741bd"]
dfsession2 = df[df['Session Id'] == '00cad8c8-094d-4dbb-894c-88984c76e2d3']
dfsession3 = df[df['Session Id'] == '01c400f2-1aec-41d7-a62d-10a87fb7658b']


# Drop duplicate session Id's

df.drop_duplicates(['Session Id'], keep='last') # keep last just means keep the row of data that is the last one for each duplicate.

df['Session Id'].value_counts()
len(df) # 20189 rows.

df['Device Type'].value_counts() # check the number of times a device is in our data set.
df['Cart Order'].value_counts() # Check how many cart orders there were.


#  ****    time AM/PM and dates  

#  Extract AM/PM from session start time
#  and put it into a new column

# Convert it to string, take out whitespace
df["Session Start Time"] = df["Session Start Time"].astype('str')
df["Session Start Time"] = df["Session Start Time"].str.strip()
df["Session Start Time"] = df["Session Start Time"].str.lstrip()


df["Session Start Time"].str[12:17] #extract the AM/PM part from Session Start Time

# However numbers are found in the above string subset from character length 12 to 17 not including 17.

# Create new column
df["DayOrNight"] = np.nan

# Extracted AM-PM into a new column: called DayOrNight
df["DayOrNight"] = df["Session Start Time"].str[12:17].str.replace('\d+', '') # We replace the number found with whitespace
# To only have AM/PM registered in new column

# Now take out the left whitespace in the string:
# EX: " AM" is different from "AM" 
df["DayOrNight"] = df["DayOrNight"].str.lstrip()

# check if it works
df.head()



# Take a subset of the data where people made a phone order.
df2 = df[df['Phone Order'] == 1]

# Convert dates in phone orders to datetime format using pandas
df2['Date Visited'] = df2['Session Start Time'].str[0:7]
df2['Date Visited']= pd.to_datetime(df2['Date Visited'])
df2['Date Visited'] = df2['Date Visited'].dt.date # Just get the Date and leave out time (which is just 00:00:00 in this case).
df2['Date Visited'].value_counts()


# Plot the times they went on the site and made phone purchase
sb.countplot(x="DayOrNight", data=df2)
sb.countplot(y="Date Visited", hue="DayOrNight", data=df2)



df2['Device Type'].value_counts() # See how much people in this subset came from each device
df2['State'].value_counts() # Where they came from. 
len(df2) # how big is this subset


# First Plot
g = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df2, kind='count', size=7, aspect=.7)
sb.plt.title('Conversion on Mobile: Where did they come from? \n')
sb.despine()
g.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)

# Second Plot
df2['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Phone Orders \n", weight='bold', fontsize= 28, alpha=.85)

# Third plot
a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df2, kind='count', size=7, aspect=.7)
sb.plt.title('Phone Orders: How many pages were clicked? \n')


 
#     ***   CART ORDERS SUBSET  *** 
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

# First plot
b = sb.factorplot(x='Device Type', hue='traffic Source', col='Phone Order',
              data=df1, kind='count', size=7, aspect=.7)

sb.plt.title('Conversion on Cart Orders: Where did they come from? \n')
sb.despine()
b.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)

# Second Plot
df1['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: Cart Orders \n", weight='bold', fontsize= 28, alpha=.85)

# Third plot
a = sb.factorplot(x='Distinct Page Views', hue='Device Type', col='Phone Order',
              data=df1, kind='count', size=7, aspect=.7)
sb.plt.title('Cart Orders: How many pages were clicked? \n')

# subset conversion calculation!
(len(df1)/len(df)) * 100
(len(df2)/len(df)) * 100


# Next subset: Where there was no conversion
df5 = df[(df['Phone Order'] == 0) & (df['Cart Order'] == 0)]

df5['Device Type'].value_counts()
df5['Session Id'].value_counts()

# First plot
n = sb.factorplot(x='Device Type', hue='traffic Source',
              data=df5, kind='count', size=7, aspect=.7)
sb.plt.title('Non Conversion: Where did they come from? \n')
sb.despine()
n.set_xticklabels(rotation=0)
plt.xlabel(" ") 
plt.ylabel("Count          ",rotation=0)


# Second Plot
df5['Distinct Page Views'].value_counts().plot(kind='bar')
plt.xticks(rotation='horizontal')
plt.title("Distinct Page Views: No Conversion \n", weight='bold', fontsize= 28, alpha=.85)

# Third plot
c = sb.factorplot(x='Distinct Page Views', hue='Device Type',
              data=df5, kind='count', size=7, aspect=.7)
sb.plt.title('No Conversion: How many pages were clicked? \n')


###  This section was just an ad-hoc analysis to spot differences between the 3 subsets of data.
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


#  ****** New subset: Time Warner Customers ******
dfnon = df[df['Isp Name'] == "time warner cable internet llc"]
len(dfnon) # How big is it?


# Take 3 subsets of Time Warner Customers: 
# Those who made phone orders, those who made cart orders, and those who did not order.

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


# Ad-hoc analysis of Time Warner Phone Orders
df7['State'].value_counts()
df7['Connection Speed'].value_counts()
df7['Browser Name'].value_counts()
df7['Isp Name'].value_counts()
df7['traffic Source'].value_counts()
df7['Device Type'].value_counts()
df7['Landing Page Raw'].value_counts()



#  *** Now Plots of Time Warner customers who made a CART ORDER.

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

# Ad-hoc analysis of Time Warner Cart Orders
df8['State'].value_counts()
df8['Connection Speed'].value_counts()
df8['Browser Name'].value_counts()
df8['Isp Name'].value_counts()
df8['traffic Source'].value_counts()
df8['Device Type'].value_counts()
df8['Landing Page Raw'].value_counts()



## Non-Conversion  for Time Warner Customers

# Plot 1
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

# Ad-hoc analysis of Time Warner Non-conversion people
df9['State'].value_counts()
df9['Connection Speed'].value_counts()
df9['Browser Name'].value_counts()
df9['Isp Name'].value_counts()
df9['traffic Source'].value_counts()
df9['Device Type'].value_counts()
df9['Landing Page Raw'].value_counts()


# Machine learning: Decision Tree (Classification Model)

#    ****     Model:   Random Forest

# Taking a subset of the data 

# This subset only focuses on peoeple with most notable ISPs (based on the dataset)
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

# Most notable states (based on the data set
dfsub2 = dfsub1[dfsub1["State"].isin(["ca","fl","tx","ct","in","pa","wa","il","ny","az","oh"])]

# People using the most notable web browsers
dfsub3 = dfsub2[dfsub2["Browser Name"].isin(["Chrome","Safari","Chrome Mobile","Internet Explorer", "Edge", "Firefox"])]

# To check distribution of count for each brower used
dfsub3['Browser Name'].value_counts()

# Deleting data that is not needed for model
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

# Ad-hoc analysis of how many phone/cart orders were made
dfsub3['Phone Order'].value_counts()
dfsub3['Cart Order'].value_counts()

# This line of code converts our categorical data to actual numbers [1 or 0] to be used for analysis.
dfsub4 = pd.get_dummies(dfsub3)
dfsub4.dtypes
dfsub4.head()

# We want to predict Phone Orders! So we separate it into a new variable called labels
labels = np.array(dfsub4['Phone Order'])

# Drop our target variable from our data!
dfsub5 = dfsub4.drop('Phone Order', axis = 1)
# Drop cart order. We wont use it to predict phone orders.
dfsub5 = dfsub5.drop('Cart Order', axis = 1)

# Save variable names to a new list
df_list = list(dfsub5.columns)

# Convert data to numpy array
dfsub5 = np.array(dfsub5)

# Importing necessary library to split our data into testing/training data sets.
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(dfsub5, labels, test_size = 0.25, random_state = 42)


# Check the shape
train_features.shape
train_labels.shape

# We split our data and we can see difference in amount of data
test_features.shape
test_labels.shape


# Importing library for random forest classifier from sklearn
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 1000, random_state = 42)

# Train the model on training data
rf.fit(train_features, train_labels)

# Make our predictions based on trained model (the model learned from a portion of our data and now time to make 
# predictions on other subset of data
predictions = rf.predict(test_features)


print('Train score: ', rf.score(train_features, train_labels))
print('Test Score: ', rf.score(test_features, test_labels))

# see which variables were most important in predicting phone order
importances = list(rf.feature_importances_)

feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(df_list, importances)]


feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)

print(feature_importances)


#  ** Plot to see feature importance in bar graph.
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
