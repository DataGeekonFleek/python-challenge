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
    delta=[]

    # for each row in 88 loops print the first column of data into a list date and 2nd column in list pnl
    for row in csvreader:
        (date.append(row[0]))
        (pnl.append(row[1]))
        
    #TOTAL MONTHS:  calculate the length of the list. 
    (TotalMonths)=(len(date))
    int(TotalMonths)
    

    #NET TOTAL: make values in pnl all ints using list comprehension
    pnl = [int (pnl2) for (pnl2) in pnl]
    sumpnl = int(sum(pnl))


    #AVERAGE CHANGE IN PNL 
    # create a loop that subtracts index2 from index 1, and adds each difference to a delta list
    delta = [(pnl[x]) - (pnl[x+1]) for x in range(len(pnl)-1)]

    #make values in delta all ints using list comprehension
    delta2= [int(delta2) for delta2 in delta]
    avgdelta = round(int(sum(delta2)) / (TotalMonths-1), 2)
   

    #GREATEST INCREASE 
    #use max to determine the highest increase in delta 
    maxprof= max(delta)
    
    #return the index of that number and set it to variable y 
    y= delta.index(maxprof)

    #return y index of the Date column to get the Date 
    highestdate =date[y]


   #GREATEST LOSS
    #use min to determine the largest decrease in delta 
    minprof=min(delta)

    #return the index of that number and set it to variable y 
    z= delta.index(minprof)

    #return y index of the Date column to get the Date 
    lowestdate =date[z]
    
   
    
  
# output in terminal 
print("Financial Analysis")
print("------------------------------")
print("Total Months: "+ str(TotalMonths))
print("Net Total: "+ "$"+ str(sumpnl))
print("Average Change: " + "$" + str(avgdelta))
print("In " + str(highestdate)+ " we earned the highest profit: " + "$"+ str(maxprof))
print("In " + str(lowestdate)+ " we suffered the highest loss: " + "$"+ str(minprof))
print("------------------------------")

#output to text file 
f = open("pybank1.txt", "w+")
print("Financial Analysis",file=f)
print("------------------------------", file=f)
print("Total Months: "+ str(TotalMonths), file=f)
print("Net Total: "+ "$"+ str(sumpnl), file=f)
print("Average Change: " + "$" + str(avgdelta))
print("In " + str(highestdate)+ " we earned the highest profit: " + "$"+ str(maxprof), file=f)
print("In " + str(lowestdate)+ " we suffered the highest loss: " + "$"+ str(minprof), file=f)
print("------------------------------", file=f)
    
       
    