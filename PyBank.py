# Your task is to create a Python script that analyzes the records to calculate each of the following:
import os
import csv

budget_data_csv = os.path.join('PyBank/Resources', 'budget_data.csv')
month_count = 0
sum = 0
change = 0
maxNum = 0
indexMax = 0
minNum = 0
indexMin = 0
prices = []
dates = []

with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    for row in csvreader:
        if row[1].strip('-').isdigit():
            month_count += 1
            sum += int(row[1])
            prices.append(row[1])
            dates.append(row[0])
            
          
for i in range(0, len(prices) - 1):
    change += int(prices[i+1]) - int(prices[i])
    if maxNum < change:
        maxNum = change
        indexMax = i+1
    elif minNum > change:
        minNum = change 
        indexMin = i+1



print("Financial Analysis" + '\n' + ('-' * 20) + '\n' + "Total Months: " + str(month_count) + 
        '\n' + "Total: $" + str(sum) + '\n' + "Average Change: $" + str(round((change/month_count),2)) + '\n'
        + "Greatest Increase in Profits: " + str(dates[indexMax]) + "($" + 
        str( int(prices[indexMax]) - int(prices[indexMax-1]) ) + ")" + '\n' + "Greatest Decrease in Profits: " 
        + str(dates[indexMin]) + "($" + str( int(prices[indexMin]) - int(prices[indexMin-1]) ) + ")"
        )



outfile = open('results.txt', 'w')

outfile.write("Financial Analysis" + '\n' + ('-' * 20) + '\n' + "Total Months: " + str(month_count) + 
        '\n' + "Total: $" + str(sum) + '\n' + "Average Change: $" + str(round((change/month_count),2)) + '\n'
        + "Greatest Increase in Profits: " + str(dates[indexMax]) + "($" + 
        str( int(prices[indexMax]) - int(prices[indexMax-1]) ) + ")" + '\n' + "Greatest Decrease in Profits: " 
        + str(dates[indexMin]) + "($" + str( int(prices[indexMin]) - int(prices[indexMin-1]) ) + ")"
        )

outfile.close() #Close the file when we’re done!
