#1.	Load Dataset from Boston Housing Agency into a DataFrame. 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols

#1.	Load Dataset from Boston Housing Agency into a DataFrame. 
df=pd.read_csv(r"C:\Users\Ilavarasi\OneDrive\Desktop\DA03\Assessment4\RR-DVIS-UA2 - boston_housing.csv")
print(df.head())

#2.	For the "Median value of owner-occupied homes" provide a boxplot. 
import matplotlib.pyplot as plt
df['MEDV'].plot(kind='box', title='Median value of owner-occupied homes')
plt.show()

#3.	Provide a histogram for the “Charles river variable”. 
df['CHAS'].plot(kind='hist', title='Charles river variable')
plt.show()

#4.	Provide a boxplot for the MEDV variable vs the AGE variable. (Discretize the age variable into three groups of 35% or less, between 35 and 70% and 70% and over) 
df.loc[(df['AGE'] <= 35), 'Age_group'] = '35 or less'
df.loc[(df['AGE'] > 35) & (df['AGE']<70), 'Age_group'] = 'Between 35 and 70'
df.loc[(df['AGE'] >= 70), 'Age_group'] = 'above 70'
ax4 = sns.boxplot(x='MEDV', y='Age_group', data=df)
ax4.set_title('Median value of owner-occupied homes per Age Group')
plt.show()

#5.	Provide a scatter plot to show the relationship between Nitric oxide concentrations (NOX) and the proportion of non-retail business acres per town (INDUS). What can you say about the relationship? 
ax5 = sns.scatterplot(x= 'NOX', y = 'INDUS', data = df)
ax5.set_title('Relationship between NOX and INDUS')
plt.show()

#6.	Create a histogram for the pupil to teacher ratio variable (PTRATIO) 
ax6 = sns.countplot(x = 'PTRATIO', data = df)
ax6.set_title('pupil to teacher ratio variable')
plt.show()

#7.	Is there a significant difference in median value of houses bounded by the Charles river or not? (CHAS)
df.loc[(df['CHAS'] == 0), 'CHAS_T'] = 'Yes'
df.loc[(df['CHAS'] == 1), 'CHAS_T'] = 'No'
print(df.head(5))

#8.	Is there a difference in Median values of houses (MEDV) for each proportion of owner occupied units built prior to 1940 (AGE)? 
dif = ols('MEDV ~ AGE', data = df).fit()
medval = sm.stats.anova_lm(dif)
print(medval)
