import os
import csv
from typing import TYPE_CHECKING
# from csv import DictReader
count=0
winning_votes=0
candidate_Name=[]
#set up the voter_dictionary
Voter_count={}

#set path for the file
Pypoll_csv=os.path.join("..","PyPoll","Resources","PyPoll_Resources_election_data.csv")

with open (Pypoll_csv) as Pypoll_csv:
    csvreader=csv.reader(Pypoll_csv,delimiter=',')
 #skip header
    csvheader=next(Pypoll_csv)
    
    #Loop through to add candidates and counts into voter_name dictionary
    for row in csvreader:
       #add the counter
        count=count+1
        candidate_Name=0
        candidate_Name=row[2]
   #          
               
        if candidate_Name in Voter_count:
           Voter_count[candidate_Name]+=1
        else:
           Voter_count[candidate_Name]=1 
    #  to print voting results
    print("Election Results")
    print("-------------------------------")
    print("Total Votes:"+str(count))
    print("-------------------------------")

   # to list all candidates votes count and the winner 
    for candidate_Name in Voter_count:
       votes= Voter_count.get(candidate_Name)
       #print (votes)
       #set vote percentage calculation 
       vote_percentage=float(votes)/float(count)*100
       #set to print voting_result and set the format
       voting_result = (f'{candidate_Name}": {vote_percentage:.4f}% ({votes}) \n' )

       print(voting_result,end="")
       
       if votes>winning_votes:
            winning_votes=votes
            winner=candidate_Name
    #  to print winner
    print("-------------------------------")
    print("Winner:"+str(winner))
    print("-------------------------------")
    
      

#Name and path of the result txt file    
PyPoll_AnalysisName=os.path.join("..","PyPoll","analysis","PyPoll_Analysis.txt")
#print the results in txt file
PyPoll_Analysis=open(PyPoll_AnalysisName, "w")
PyPoll_Analysis.write("Election Results\n")
PyPoll_Analysis.write("-------------------------------\n")
PyPoll_Analysis.write("Total Votes:"+str(count))+"\n")
PyPoll_Analysis.write("Total Profits and Loss:"+"$"+str(Total_PNL)+"\n")
PyPoll_Analysis.write("Average PNL Change:"+"$"+str(Average_Change_PNL))
PyPoll_Analysis.write("Greatest increase PNL:"+str(Related_increase_month)+" "+str(Greatest_increase_PNL)+"\n")
PyPoll_Analysis.write("Greatest decrease PNL:"+str(Related_decrease_month)+" "+str(Greatest_decrease_PNL)+"\n")

PyPoll_Analysis.close()