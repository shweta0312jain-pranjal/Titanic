import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

plt.figure(figsize = (6, 4))
sns.countplot(x = 'Gender', hue = 'Survived', data = data)
plt.title("Survival Count on the basis of Gender")
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (6, 4))
sns.countplot(x = 'Pclass', hue = 'Survived', data = data)
plt.title("Survival Count based on Passenger Class")
plt.xlabel('Pclass')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (6, 4))
sns.histplot(data = data, x = 'Age', kde = False, bins = 40)
plt.title("Age Distribution of Passengers")
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize = (6, 4))
sns.countplot(x ='Gender', data = data)
plt.title("Total Count of male vs female")
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

plt.figure(figsize = (6, 4))
sns.countplot(x = 'Survived', data = data)
plt.title("Overall Survival Count")
plt.xlabel('Survived (0 = no, 1 = yes)')
plt.ylabel('Count')
plt.show()
