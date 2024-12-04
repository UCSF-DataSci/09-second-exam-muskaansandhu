
#Instructions: 
#1. Load and structure the data:
   # - Read the processed CSV file
   # - Convert visit_date to datetime
   # - Sort by patient_id and visit_date

# 2. Add insurance information:
   # - Read insurance types from `insurance.lst`
   # - Randomly assign (but keep consistent per patient_id)
   # - Generate visit costs based on insurance type:
     # - Different plans have different effects on cost
     # - Add random variation

# 3. Calculate summary statistics:
   # - Mean walking speed by education level
   # - Mean costs by insurance type
   # - Age effects on walking speed


#Importing needed libraries 
import pandas as pd 
import numpy as np 

#1) 
dt = pd.read_csv("ms_data.csv") #loading in dataset 
dt['visit_date'] = pd.to_datetime(dt['visit_date'], format='%Y-%m-%d') #converting visit_date to datetime object 
dt_sorted = dt.sort_values(by=['patient_id', 'visit_date']) #sorting by patient_id and visit_date 

#2)  
with open('insurance.lst' , 'r') as file:
    insurance  = file.readlines()[1:]
insurance = [line.strip() for line in insurance]

np.random.seed(100)
unique_pid = dt['patient_id'].unique()
insurance_assignment = np.random.choice(insurance, size=len(unique_pid))
dt['insurance_type'] = dt['patient_id'].map(dict(zip(unique_pid, insurance_assignment)))

insurance_cost = {'Basic' : 100, 'Premium' : 200, 'Platinum' : 300}
dt['visit_cost'] = dt['insurance_type'].map(insurance_cost) + np.random.normal(0, 50, size=len(dt))

dt.to_csv('/Users/MuskaanSandhu/09-second-exam-muskaansandhu/analyze_visits_ms_data.csv', index=False)

#3) 

mean_walking_speed = dt.groupby('education_level')['walking_speed'].mean()
mean_costs = dt.groupby('insurance_type')['visit_cost'].mean()
age_walking_speed = dt['age'].corr(dt['walking_speed'])
missing = dt.isnull().sum()

#Printing all the results to terminal: 
print(f"Missing Data: {missing}")
print(f"Mean walking speed by education level: {mean_walking_speed}")
print(f"Mean cost by insurance type: {mean_costs}")
print(f"Correlation between age and walking speed: {age_walking_speed}")
