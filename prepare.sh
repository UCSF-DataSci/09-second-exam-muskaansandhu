#!/bin/bash

#Instructions: 
    #1) Run the script generate_dirty_data.py to create ms_data_dirty.csv which you will clean in the next steps (you may need to install the numpy library).
    #2) Clean the raw data file:
        # - Remove comment lines
        # - Remove empty lines
        # - Remove extra commas
        # - Extract essential columns: patient_id, visit_date, age, education_level, walking_speed
        # - Save the file as ms_data.csv
    #3) Create a file, insurance.lst listing unique labels for a new variable, insurance_type, one per line (your choice of labels). Depending on how you want to import this file later with Python, you may or may not want to add a header row nameing the column as insurance_type.
    #4) Generate a summary of the processed data:
        # - Count the total number of visits (rows, not including the header)
        # - Display the first few records

#1)
python3 generate_dirty_data.py #running the python script 

#2)
grep -v '^#' ms_data_dirty.csv | sed '/^$/d' | sed 's/,,*/,/g' | cut -d, -f1,2,4,5,6  > cleaned_data.csv
head -n 1 cleaned_data.csv > ms_data.csv
awk -F, '$5 >= 2.0 && $5 <= 8.0' cleaned_data.csv >> ms_data.csv
#removes lines with comments, empty lines, and extra commas from the dirty csv. extracts the five columns we need, filters the walked speed from 2.0-8.0, and saves it to a csv called ms_data.csv.


#3)
echo -e "insurance_type\nBasic\nPremium\nPlatinum" > insurance.lst #creating a new list with the three insurance types 

#4) 
echo "Total number of visits:" 
tail -n +2 ms_data.csv | wc -l #counts the total number of rows in the dataset starting from the second row, which removes the headers 

echo "First 10 records:"  
head -n 10 ms_data.csv #printing first 10 records 
 
rm cleaned_data.csv 
echo "Removed cleaned_data.csv"


