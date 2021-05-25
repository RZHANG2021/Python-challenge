import os
import csv
from typing import TYPE_CHECKING
count=0 
InitialPNL=0
Total_PNL=0
Total_Change_PNL=0
month=[]
PNL=[]
Change_PNLS=[]

#set path for the file
Pybank_csv=os.path.join("..","Pybank","Resources","PyBank_Resources_budget_data.csv")

with open (Pybank_csv) as Pybank_csv:
    csvreader=csv.reader(Pybank_csv,delimiter=',')
 #skip header
    csvheader=next(Pybank_csv)
    
    
    
    #PNL short for Profit and loss
    for row in csvreader:
        #add the counter
        count=count+1
        #to count how many months
        month.append(row[0])
        PNL.append(row[1])
        Total_PNL=Total_PNL+int(row[1]) 
        NextPNL=int(row[1])
        Change_PNL=NextPNL-InitialPNL
        Change_PNLS.append (Change_PNL)

        Total_Change_PNL=Total_Change_PNL+Change_PNL
        InitialPNL=NextPNL
        Average_Change_PNL=(Total_Change_PNL/count)

        Greatest_increase_PNL=max(Change_PNLS) 
        Greatest_decrease_PNL=min(Change_PNLS)
        Related_increase_month=month[Change_PNLS.index(Greatest_increase_PNL)]
        Related_decrease_month=month[Change_PNLS.index(Greatest_decrease_PNL)]

    #print the result line by line
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Month:"+str(count))
    print("Total Profits and Loss:"+"$"+str(Total_PNL))
    print("Average PNL Change:"+"$"+str(Average_Change_PNL))
    print("Greatest increase PNL:"+str(Related_increase_month)+" "+str(Greatest_increase_PNL))
    print("Greatest decrease PNL:"+str(Related_decrease_month)+" "+str(Greatest_decrease_PNL))


#Name and path of the result txt file    
PyBank_AnalysisName=os.path.join("..","PyBank","analysis","PyBank_Analysis.txt")
#print the results in txt file
PyBank_Analysis=open(PyBank_AnalysisName, "w")
PyBank_Analysis.write("Financial Analysis\n")
PyBank_Analysis.write("-------------------------------\n")
PyBank_Analysis.write("Total Month:"+str(count)+"\n")
PyBank_Analysis.write("Total Profits and Loss:"+"$"+str(Total_PNL)+"\n")
PyBank_Analysis.write("Average PNL Change:"+"$"+str(Average_Change_PNL))
PyBank_Analysis.write("Greatest increase PNL:"+str(Related_increase_month)+" "+str(Greatest_increase_PNL)+"\n")
PyBank_Analysis.write("Greatest decrease PNL:"+str(Related_decrease_month)+" "+str(Greatest_decrease_PNL)+"\n")

PyBank_Analysis.close()
