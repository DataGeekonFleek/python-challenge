#PYBANK PREP
# The total number of months included in the dataset
    # Read the csv file, 
import os 
import csv

    #Set path for file budget_data copy.csv
csvpath = os.path.join("budget_data copy.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # create a python list from the date column, assign it variable
    date =[]
    pnl =[]

    # for each row in 88 loops print the first column of data into a list date and 2nd column in list pnl
    for row in csvreader:
        (date.append(row[0]))
        (pnl.append(row[1]))
        
    # calculate the length of the list. 
    (TotalMonths)=(len(date))
    int(TotalMonths)
    
    #make values in pnl all ints using list comprehension
    pnl = [int (pnl2) for (pnl2) in pnl]
    # create a sum function or the list 
    sumpnl = int(sum(pnl))

    # NET TOTAL PNL 
    print(sumpnl)

    #The average of the changes in "Profit/Losses" over the entire period
    #calculate the average by using the length variable as denominatore & sum as numerator
    #print 
    average = sumpnl / TotalMonths
    #print(average)


#The greatest decrease in profits 
    #use min to determine the lowest value in P&L list 
    maxprof=max(pnl)
    #print ("Highest value in P&L List " + str(maxprof))

    #return the index of that number and set it to variable x 
    x= pnl.index(maxprof)
    #print(x)

    #return x index of the Date column to get the Date 
    highestdate=date[x]
    # print Date and Profit 
   
    minprof=min(pnl)
    #print ("Lowest value in P&L List " + str(minprof))
    #return the index of that number and set it to variable x 
    y= pnl.index(minprof)
    #print(y)
    #return x index of the Date column to get the Date 
    lowestdate=date[y]
    # print Date and Profit 
    
  
# output in terminal 
print("Financial Analysis")
print("------------------------------")
print("Total Months: "+ str(TotalMonths))
print("Average Change: " + "$" + str(average))
print("Highest date = " + str(highestdate)+ " and highest profit = " + str(maxprof))
print("Lowest date = " + str(lowestdate)+ " and lowest profit = " + str(minprof))

#output to text file 
f = open("pybank1.txt", "w+")
print("Financial Analysis", file=f)
print("------------------------------", file=f)
print("Total Months: "+ str(TotalMonths), file=f)
print("Average Change: " + "$" + str(average), file=f)
print("Highest date = " + str(highestdate)+ " and highest profit = " + str(maxprof), file=f)
print("Lowest date = " + str(lowestdate)+ " and lowest profit = " + str(minprof), file=f)
    
       
    