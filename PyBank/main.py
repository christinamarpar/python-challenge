#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The total number of months included in the dataset
#The total amount of revenue gained over the entire period
#The average change in revenue between months over the entire period
#The greatest increase in revenue (date and amount) over the entire period
#The greatest decrease in revenue (date and amount) over the entire period
import os
import csv
import math

os.chdir("/Users/christinapark/gitrepo/python-challenge/PyBank")

# Path to budget csv
budgetCSV = "budget_data_1.csv"
# Read in the CSV file
with open(budgetCSV, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Count the number of lines
    line_num = 0
    rev_tot = float(0)
    rev_lastmonth=float(0)
    rev_thismonth=float(0)
    delta = []
    temp_delta=float(0)
    max_delta=float(0)
    max_date=""
    min_delta=float(0)
    min_date=""
    for row in csvreader:
        if line_num==1:
            rev_lastmonth = float(row[1])
            rev_tot = rev_tot + rev_lastmonth
        if line_num>1:
            rev_thismonth = float(row[1])
            rev_tot = rev_tot + rev_thismonth
            temp_delta = rev_thismonth-rev_lastmonth
            delta.append(temp_delta)
            if temp_delta>max_delta:
                max_delta=temp_delta
                max_date=row[0]
            if temp_delta<min_delta:
                min_delta=temp_delta
                min_date=row[0]
            rev_lastmonth = rev_thismonth
        line_num=line_num+1

months = line_num-1

sum_delta = float(0)
num_delta = line_num-2
for i in range(0,num_delta):
    sum_delta=sum_delta+delta[i]
avg_delta = sum_delta/num_delta

print("----------------------------")
print("FINANCIAL ANALYSIS")
print("----------------------------")
print("Months: " + str(months))
print("Total Revenue: $" + str(math.floor(rev_tot)))
print("Average Revenue Change: $" + str(math.floor(avg_delta)))
print("Greatest Increase in Revenue: " + max_date + " ($" + str(math.floor(max_delta)) + ")")
print("Greatest Decrease in Revenue: " + min_date + " ($" + str(math.floor(min_delta)) + ")")