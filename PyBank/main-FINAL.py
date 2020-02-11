#Python Homework - PyBank

#Import dependencies
import os
import csv 

bank_data = os.path.join("..","PyBank","budget_data.csv")

#Open and read csv
with open(bank_data, newline = "") as csvfile:
    
    #Read through each row of data after the header
    next(csvfile)
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Set counters/tracks for our objective data 
    TotalMonths = 0
    NetProfitLoss = 0
    Max = 0
    Min = 0
    AvgProfitLoss = 0
    Previous = 0
    CummulativeDiff = 0

    #Loop through each row
    for row in csvreader:


        #TotalMonths tracks how many rows we have reviewed
        TotalMonths += 1

        #Each row we process, we add the profit/loss by row index
        NetProfitLoss = NetProfitLoss + int(row[1])

        #AverageProfit Loss is the net divided by rows we have process (i.e. months)
        Current = int(row[1])
        
        Diff = Current - Previous

        CummulativeDiff = CummulativeDiff + Diff

        AvgProfitLoss = (CummulativeDiff)/TotalMonths

        Previous = int(row[1])
        
        #Identify row with max value
        if int(Diff) > Max:
            Max = int(Diff)
            DateMax = row[0]
        else:
            Max = Max
        
        #Identify row with min value
        if int(Diff) < Min:
            Min = int(Diff)
            DateMin = row[0]
        else:
            Min = Min
    
FinancialResults = os.path.join("..","PyBank","FinancialResults.txt")

with open(FinancialResults, "w", newline="") as text_file:
    print(f"Financial Analysis", file=text_file)
    print(f"--------------------------" , file=text_file)
    print(f"Total Months: {str(TotalMonths)}" , file=text_file)
    print(f"Total Net Profit/Loss: ${str(NetProfitLoss)}" , file=text_file)
    print(f"Average Change: ${str(AvgProfitLoss)}", file=text_file)
    print(f"Greatest Increase in Profits: {str(DateMax)} (${str(Max)})", file=text_file)
    print(f"Greatest Decrease in Profits: {str(DateMin)} (${str(Min)})", file=text_file)
