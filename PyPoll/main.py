import os 
import csv 

#read CSV file election_data.csv
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline="") as pypollfile:
    pypollfile = csv.reader(pypollfile, delimiter=",")
    header = next(pypollfile)

#* The total number of votes cast: length of a list of values in voter id column 
    votes=[]
    candidate =[]
    Pcts=[]

    for row in pypollfile: 
        (votes.append(row[0]))
        (candidate.append(row[2]))

    votescast= len(votes)
    
 # A complete list of candidates who received votes 
    unique_candidates =set(candidate)
    unique_candidate_list= list(unique_candidates)
    
    
    #total #of votes per candidate  
    Correyvotes= candidate.count('Correy')
    Khanvotes= candidate.count('Khan')
    Livotes= candidate.count('Li')
    OTvotes= candidate.count("O'Tooley")
    #* The percentage of votes each candidate won
    # number of candidate votes / total votes * 100
    def pctwon(x):
        ratio = x/votescast
        percent = ratio * 100 
        return round(percent,2)
    
    Correypct= (pctwon(Correyvotes))
    Khanpct= (pctwon(Khanvotes))
    Lipct= (pctwon(Livotes))
    OTpct= (pctwon(OTvotes))

    candidatePCT=[Correypct, Khanpct, Lipct, OTpct]
  #* The winner of the election based on popular vote.
    if(max(candidatePCT) == Khanpct):
        winner = "Khan wins!"
    elif(max(candidatePCT) == Correypct):
        winner = "Correy wins!"
    elif(max(candidatePCT) == Lipct):
        winner = "Li wins!"
    else:
        winner = "O'Tooley wins!"

    #terminaloutput 
    

    print("Election Results")
    print("-------- ---------- -------- ---------- ")
    print("Total Votes: "+ str(votescast))
    print("-------- ---------- -------- ---------- ")
    print("Khan: " + str(Khanpct)+ "%" + " : " + str(Khanvotes) + " votes")
    print("Correy: " + str(Correypct)+ "%" + " : " + str(Correyvotes) + " votes")
    print("Li: " + str(Lipct)+ "%" + " : " + str(Livotes) + " votes")
    print("O'Tooley: " + str(OTpct)+ "%" + " : " + str(OTvotes) + " votes")
    print("-------- ---------- -------- ---------- ")
    print("Who wins???: " + str(winner))
    print("-------- ---------- -------- ---------- ")
    
    #txtfileoutput
    f = open("pypoll2.txt", "w+")
    print("Election Results", file=f)
    print("-------- ---------- -------- ---------- ", file=f)
    print("Total Votes: "+ str(votescast), file=f)
    print("-------- ---------- -------- ---------- ", file=f)
    print("Khan: " + str(Khanpct)+ "%" + " : " + str(Khanvotes) + " votes", file=f)
    print("Correy: " + str(Correypct)+ "%" + " : " + str(Correyvotes) + " votes", file=f)
    print("Li: " + str(Lipct)+ "%" + " : " + str(Livotes) + " votes", file=f)
    print("O'Tooley: " + str(OTpct)+ "%" + " : " + str(OTvotes) + " votes", file=f)
    print("-------- ---------- -------- ---------- ", file=f)
    print("Who wins???: " + str(winner), file=f)
    print("-------- ---------- -------- ---------- ", file=f)
    
  