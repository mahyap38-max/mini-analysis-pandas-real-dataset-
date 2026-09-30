import pandas as pd

df=pd.read_csv('winequality-white.csv',sep=';')

import matplotlib.pyplot as plt
import seaborn as sns 

#general information
print(df.info())

#repeated values
#print(df.duplicated().sum())
#937 values are repeated

#missing values()
#print(df.isnull().sum())
# No missing values


#distribution of Quality
#sns.histplot(data=df, x='quality')
#plt.show()
#Most of thw wines got 6 in quality rate
#print(df['quality'].describe()) mean:roudnly 5.9
#print(df['quality'].mode()) 6
#General observation: most wines are at 6 rate for the quality check test.


#distribution of alcohol
#ns.histplot(data=df, x='alcohol')
#plt.show()
#print(df['alcohol'].mean()) #roundly 10.5
#print(df['alcohol'].std())  roundly 1.2
#print(df['alcohol'].median())  #10.4
#as the mean and median has a tiny different I can conclude that the data does not have 
#a speacial outlier and the distribution may be reasonably symmetric.
#Because mean>median so it might be a right skewed.
#print(df['alcohol'].mode())  #9.4
#print(df['alcohol'].var()) 1.5
#The number 9.4 is more repeated for the alcohol level
#Most of the wines got 9.5 to 10.5 level in alcohol
#print(df['alcohol'].describe())
#print(df['alcohol'].quantile(0.50)) 10.4
#print(df['alcohol'].quantile(0.9)) 19.4
#print((df['alcohol']>10.5).mean())  roundly 0.44
#general observation of the alcohol level: most ot the wines are at 9.4 rate in alcohol range
#which seems to be dramarically less than the center and the mean so the data may have some wines
#with high level of alcohol more than 10.5+1.2 which cuases the differences of the mode and the 
#median.due to the fact that mean>median and judghing by the histogram plot, the dataset has a right 
#skewed distribution


#relationship between alcohol and quality
#sns.lineplot(data=df, x='quality',y='alcohol')
#plt.show()
#print((df['alcohol']>10.5) & (df['quality']<6))
#General observation:The alcohol level can probably have a positive relationship with quality.#print(((df['alcohol']>9 )& (df['quality']>6)).mean()) 0.2


#ph distribution
#sns.histplot(data=df, x='pH')
#plt.show()
#print(df['pH'].mean())  3.188
#print(df['pH'].median()) 3.18
#print(df['pH'].std()) 0.151
#General observation: As Median and mean are close to eachother so PH of the wines may have a symmestric shape
#Due to mean and std and histogram plot , most wines may have a PH at 3.1 level 


#relationship between  alcohol and PH level 
#sns.lineplot(data=df, x=df['pH'], y=df['alcohol'])
#plt.show()
#print((( df['alcohol']>9.4) & (df['pH']>3.1)).mean ())  #0.561

#print(df['volatile acidity'].mean()) #0.28
#print(df['volatile acidity'].median()) #0.26


#print(df['fixed acidity'].mean()) #6.85
#print(df['fixed acidity'].median()) #6.8
sns.lineplot(data=df, x='volatile acidity ' , y='fixed acidity')
plt.show()


#Overal Analysis:
#The dataset contains 11 columns called as [fixed acidity , volatile acidity , citric acid , residual sugar , chlorides , free sulfur dioxide , total sulfur dioxide ,
#density , ph , sulphates , alcohol , quality ]
#Excpectation of a random white wine from this data set :
#Alcohol level around 9.3 to 9.5 , ph 3 to 3.5 , 