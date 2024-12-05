
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
with open('insurance.lst' , 'r') as file: #opening insurance.lst file in read mode  
    insurance  = file.readlines()[1:] #assinging the lines from the insurance.lst file to a variable called insurance, minus the header 
insurance = [line.strip() for line in insurance] # makes sure that 'insurance' is a list with each element in the list being a different insurance type by removing any trailing space 

np.random.seed(100) #setting random seed to ensure same results when running the script 
unique_pid = dt['patient_id'].unique() #extracting unique patient IDs 
insurance_assignment = np.random.choice(insurance, size=len(unique_pid)) #randomly assigning insurances based on number of unique patient IDs 
dt['insurance_type'] = dt['patient_id'].map(dict(zip(unique_pid, insurance_assignment))) #adding a new variable for insurance type by mapping the insurance assignment from line above to unique patient IDs

insurance_cost = {'Basic' : 100, 'Premium' : 200, 'Platinum' : 300} #defining base costs of three insurance tiers 
dt['visit_cost'] = dt['insurance_type'].map(insurance_cost) + np.random.normal(0, 5, size=len(dt)) #mapping the base costs of each insurance type and adding random normal variation with SD of 5 and a mean centered around 0. 

dt.to_csv('/Users/MuskaanSandhu/09-second-exam-muskaansandhu/analyze_visits_ms_data.csv', index=False) #saving the CSV file with the visit costs and insurance types 

#3) 
dt = pd.read_csv("/Users/MuskaanSandhu/09-second-exam-muskaansandhu/csv/analyze_visits_ms_data.csv")
mean_walking_speed = dt.groupby('education_level')['walking_speed'].mean() #calculating mean walking speed by education level
mean_costs = dt.groupby('insurance_type')['visit_cost'].mean() #calculating mean visit cost by insurance type 
age_walking_speed = dt['age'].corr(dt['walking_speed']) #calculating correlation of walking speed by age 
missing = dt.isnull().sum() #checking for missing values in the dataset 

#Printing all the results to terminal: 
print(f"Missing Data: {missing}")
print(f"Mean walking speed by education level: {mean_walking_speed}")
print(f"Mean cost by insurance type: {mean_costs}")
print(f"Correlation between age and walking speed: {age_walking_speed}")
