#mean the average value
import numpy as np
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)
print(x)

#Median the mid value
y=np.median(speed)
print(y)

#Mode the value that occurs most numeber of time
from scipy import stats as st
z = st.mode(speed)
print(z)



#Standard Deviation
"""
Standard deviation is a number that describes how spread out the values are.

A low standard deviation means that most of the numbers are close to the mean (average) value.

A high standard deviation means that the values are spread out over a wider range.
"""

a = np.std(speed)
print(a)

#Variance
# Variance is another number that indicates how spread out the values are.

b= np.var(speed)
print(b)

#Percentiles are used in statistics to give you a number that describes the value that a given percent of the values are lower than.
ages=[60,77,81,101,83,97,73]
c = np.percentile(ages, 75)
print(c)


newages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]
d = np.percentile(newages, 90)
print(d)


#Data Distribution

e = np.random.uniform(0.0, 5.0, 20)
print(e)