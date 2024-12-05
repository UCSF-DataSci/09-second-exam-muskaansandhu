#Instructions: 

#1) Analyze walking speed:
   # - Multiple regression with education and age
   # - Account for repeated measures
   # - Test for significant trends

# 2. Analyze costs:
   # - Simple analysis of insurance type effect
   # - Box plots and basic statistics
   # - Calculate effect sizes

# 3. Advanced analysis:
   # - Education age interaction effects on walking speed
   # - Control for relevant confounders
   # - Report key statistics and p-values


#Importing necessary libraries 

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import statsmodels as sm
import statsmodels.formula.api as smf
from scipy.stats import f_oneway 

dt = pd.read_csv('analyze_visits_ms_data.csv') #reading in dataset from previous exercise 

#1) 
walking_speed_model = smf.mixedlm("walking_speed ~ C(education_level) + age", dt, groups=dt["patient_id"]).fit() #fitting mixed linear model of walking speed accounting for education level and age plus logitudinal nature of data 
print(walking_speed_model.summary()) #priting out model summary for coefficients and p-values 

#2) 

insurance_cat = dt.groupby('insurance_type')['visit_cost'].apply(list).tolist() #produces a list of 3 different arrays that groups the visit costs by insurance types 
f_stat, p_val = f_oneway(*insurance_cat) #obtains the F-statistic and associated p-value from the ANOVA; '*insurance_cat' unpacks the three arrays as seperate arguements for the ANOVA function to register as three different groups
print("F-statistic for ANOVA:", f_stat) #printing F-statistic
print("P-value for ANOVA:", p_val) #printing p-value 

insurance_model = smf.ols("visit_cost ~ C(insurance_type)", data=dt).fit() #fitting linear regression of visit cost based on insurance type
print(insurance_model.summary()) #printing model summary to obtain coefficients and p-values

plt.figure(figsize=(10, 7))
sns.boxplot(x='insurance_type', y='visit_cost', data=dt, showfliers=True, palette='pastel') #plotting box plot of visit cost by insurance type 
plt.title("Visit Costs by Insurance Types") #adding plot title
plt.ylabel("Total Visit Cost") #adding Y-axis label
plt.xlabel("Insurance Types") #adding X-axis label 
plt.show() #displaying plot 

print(dt.groupby('insurance_type')['visit_cost'].describe()) #printing out basic summary statistics of visit cost by insurance type 


#3) 

adv_walking_speed_model = smf.mixedlm("walking_speed ~ C(education_level) * age + C(insurance_type)", dt, groups=dt["patient_id"]).fit() #fitting advanced mixed linear model of walking speed accounting for interaction between education level and age, along with insurance type and the logitduinal nature of data 
print(adv_walking_speed_model.summary()) #printing model summary and coefficients 


