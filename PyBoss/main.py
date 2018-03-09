#Import the employee_data1.csv and employee_data2.csv files, organized as follows:
#Emp ID,Name,DOB,SSN,State

#Convert and export the data to use the following format instead:
    #The Name column should be split into separate First Name and Last Name columns.
    #The DOB data should be re-written into DD/MM/YYYY format.
    #The SSN data should be re-written such that the first five numbers are hidden from view.
    #The State data should be re-written as simple two-letter abbreviations.

import os
import csv

os.chdir("/Users/christinapark/gitrepo/python-challenge/PyBoss")

#path for csv to read in
emp_in_csv = os.path.join('..','PyBoss','employee_data1.csv')

#arrays to write out
emp_id = []
f_name = []
l_name = []
DOB_clean = []
SSN_clean = []
state = []

#state dictionary
stateDict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#counter to skip line 1
counter = 1

#open employee data csv file
with open(emp_in_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Loop through the data
    for row in csvreader:
        if counter>1 :
            emp_id.append(row[0])
            name = row[1].split()
            f_name.append(name[0])
            l_name.append(name[1])
            DOB_dirty = row[2].split('-')
            DOB_clean.append(str(DOB_dirty[1]) + "/" + str(DOB_dirty[2]) + "/" + str(DOB_dirty[0]))
            SSN_dirty = row[3].split('-')
            SSN_clean.append("***-**-" + str(SSN_dirty[2]))
            state.append(stateDict[row[4]])
        else :
            counter = counter + 1
cleaned_csv = zip(emp_id, f_name, l_name, DOB_clean, SSN_clean, state)

#csv to write out
emp_out_csv = "employee_data_v2.csv"

with open(emp_out_csv, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)