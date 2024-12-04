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
import statsmodels.formula.api as smf
from scipy import stats 

dt = pd.read_csv('analyze_visits_ms_data.csv')

#1) 
walking_speed_model = smf.mixedlm("walking_speed ~ education_level + age", dt, groups=data["patient_id"])