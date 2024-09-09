# Home Price Prediction
#Linear Regression Single Variable
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("homeprices.csv")
df
# %matplotlib inline   (apparently this is for jupiter notebook) 
plt.xlabel('area(Sqr Ft)')
plt.ylabel('Price($USD)')
plt.scatter(df.area,df.price, color='black', marker='*')
reg=linear_model.LinearRegression()
reg.fit(df[['area']].values,df.price)
reg.predict([[3300]])
plt.xlabel('area',fontsize=12,color='green')
plt.ylabel('price',fontsize=12,color='green')
plt.scatter(df.area,df.price,color='red',marker='*')
plt.plot(df.area,reg.predict(df[['area']].values),color='blue')


d=pd.read_csv('areas.csv')
d.head(3)
p=reg.predict(d)
d['prices']=p
d.to_csv("prediction.csv",index=False)


#End of single varibale

