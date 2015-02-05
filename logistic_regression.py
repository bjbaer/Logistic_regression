import pandas as pd
import numpy as np
import statsmodels.api as sm
import math
loansData = pd.read_csv('loansData_clean.csv')

loansData['Interest.Rate.Low'] = (loansData['Interest.Rate'] < .12) # create a new column Interest.Rate.High True if greater than 12%
loansData['Intercept'] = 1 #create a new column Intercept that is always 1

ind_vars = [] #create a list of the titles of the columns
ind_vars.append('Intercept')
ind_vars.append('Amount.Requested')
ind_vars.append('FICO.Range')


logit = sm.Logit(loansData['Interest.Rate.Low'], loansData[ind_vars]) #Logistic Regression
result = logit.fit() #fit the model
coeff = result.params #save the parameters
print coeff # print the coefficients

def logistic_function(Amount_Requested, FICO_Score): #create a function that takes in two numbers, the amount of loan requested and the persons FICO
	return 1 / (1 + math.exp(coeff[0] + coeff[1]*Amount_Requested + coeff[2]*FICO_Score))

print logistic_function(10000, 720)
#this returns a value of .325 which is lower then 0.7. This tells us that we would not expect this person to get a loan with an interest rate lower than
#12%
def pred(Amount_Requested, FICO_Score):
	if logistic_function(Amount_Requested, FICO_Score) >= .7:
		print "I think you'll get the loan for less than 12 percent interest"
	else:
		print "Don't count on getting that loan for less than 12 percent!"
pred(10000, 720)

#loansData.to_csv('loansData_work.csv', header=True, index=False) #save the data as a new csv file to save it.
