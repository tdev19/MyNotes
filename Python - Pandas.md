````
```
#Write your code here

#Create pandas series 
import pandas as pd
import numpy as np

#Task 1
data1 = {"s1":176.2,"s2":158.4,"s3":167.6,"s4":156.2,"s5":161.4}
heights_A = pd.Series(data= data1,index= None)
print(heights_A.shape)

#Task 2 
data2 = {"s1":85.1,"s2":90.2,"s3":76.8,"s4":80.4,"s5":78.9}
weights_A = pd.Series(data= data2,index= None)
print(weights_A.dtypes)

#Task 3
data3 = {"Student_height":data1,"Student_weight":data2}
df_A = pd.DataFrame(data = data3, index=None)

print(df_A.shape)
#Task 4
np.random.seed(100)

# Generate 1D numpy array from normal distribution
B = np.random.normal(loc=170, scale=25, size=5)  # Generating 100 samples

# Convert numpy array to pandas Series
heights_B = pd.Series(B,index=['s1','s2','s3','s4','s5'])

np.random.seed(100)

wB = np.random.normal(loc=75,scale = 12, size =5)

weights_B = pd.Series(wB,index=['s1','s2','s3','s4','s5'])

print(heights_B.mean())

#Task 5
d_2 = {'Student_height':heights_B,'Student_weight':weights_B}
df_B = pd.DataFrame(data=d_2,index=None)
print(df_B.columns)







