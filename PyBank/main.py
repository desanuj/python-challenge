import os
import csv

os.chdir(os.path.dirname(__file__))

filepath = os.path.join("./Resources", "budget_data.csv")


with open(filepath, newline ="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader, None)

    monthtotal = 0
    nettotal = 0
    avgchange = 0
    maxprofit = 0
    maxloss = 0
    maxmonth = ''
    minmonth = ''

    change = 0
    totalchange = 0
    lastmonth = 0
    value = 0
    
    for row in csv_reader:
        lastmonth = value
        monthtotal +=1
        nettotal += int(row[1])
        value = int(row[1])

        if lastmonth != 0:
            change = value - lastmonth
            totalchange += change
        if change > maxprofit:
            maxprofit = change
            maxmonth = row[0]
        
        elif change < maxloss:
            maxloss = change
            minmonth = row[0]
        
        

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {monthtotal}")
    print(f"Total: ${nettotal}")
    print(f"Average Change: ${round(totalchange/(monthtotal-1),2)}")
    print(f"Greatest Increase in Profits: {maxmonth} ({maxprofit})")
    print(f"Greatest Decrease in Profits: {minmonth} ({maxloss})")

    file = open('FinancialAnalysis.txt','w+')

    file.write("Financial Analysis")
    file.write("----------------------------")
    file.write(f"Total Months: {monthtotal}")
    file.write(f"Total: ${nettotal}")
    file.write(f"Average Change: ${round(totalchange/(monthtotal-1),2)}")
    file.write(f"Greatest Increase in Profits: {maxmonth} ({maxprofit})")
    file.write(f"Greatest Decrease in Profits: {minmonth} ({maxloss})")

    file.close()
 
        



