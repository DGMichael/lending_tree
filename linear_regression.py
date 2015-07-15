
# coding: utf-8

# In[2]:

import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')


# In[4]:

loansData["Interest.Rate"][0:5]


# In[7]:

loansData["Loan.Length"][0:5]


# In[8]:

loansData["FICO.Range"][0:5]


# In[22]:

loansData["FICO.Range"][0:5]


# In[30]:

#Generate new column with lower range of the FICO score: Evaluate the function
loansData["FICO.Range"].values[0:5][0].split("-")[0]


# In[81]:

minFICO = loansData["FICO.Range"].map(lambda x: float(x.split("-")[0]))


# In[82]:

loansData["FICO.Score"] =minFICO


# In[83]:

loansData["FICO.Score"][0:5]


# In[86]:

loansData["Interest.Rate"][0:5]


# In[87]:

cleanRate = loansData["Interest.Rate"].map(lambda x: float(x.strip("%")) /100)


# In[88]:

loansData["Interest.Rate"] = loansData["Interest.Rate"].map(lambda x: float(x.strip("%")) /100)


# In[89]:

loansData["Interest.Rate"][0:5]


# In[90]:

#Strip the months:
loansData["Loan.Length"][0:5]


# In[91]:

loansData["Loan.Length"].values[0].rstrip(" months")


# In[92]:

cleanLength = loansData["Loan.Length"].map(lambda x: x.rstrip(" months"))


# In[93]:

loansData["Loan.Length"] = cleanLength


# In[74]:

loansData["Loan.Length"]


# In[103]:

import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[101]:

#Generate scatter plot:
loansData["FICO.Score"].hist()


# In[108]:

#Generate scatter matrix:
pd.scatter_matrix(loansData, alpha = 0.05, figsize = (20,20), diagonal = "hist")


# In[118]:

#Generate linear model of FICOScore and Loan Amount -> interest rate
import numpy as np
import statsmodels.api as sm


# In[121]:

#Pull out data for model training:
intrate = loansData["Interest.Rate"]
loanamt = loansData["Amount.Requested"]
fico = loansData["FICO.Score"]


# In[136]:

#Reshape series into columns:
y = np.matrix(intrate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()


# In[137]:

#Put the two independent variable columns together:
x = np.column_stack([x1,x2])


# In[138]:

x1


# In[139]:

x2


# In[140]:

x


# In[141]:

#Generate the linear model:
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()


# In[142]:

#Output results:
f.summary()


# In[143]:




# In[ ]:



