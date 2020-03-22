#Import module for reading csv files
import csv
import os 

#load files
csvpath = os.path.join("./","election_data.csv")


 #Open the csv file election_data using handle csvreader
with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Read and omit the header row
    csv_header = next(csvreader)
    
    # Intitilizes the variables used in the loop
    total_number_of_votes= 0
    candidate = [] 
    candidate_votes = []
    


    for row in csvreader:
        total_number_of_votes = total_number_of_votes + 1

        if row[2] not in candidate :
            candidate.append(row[2])
            candidate_votes.append(1)
        else:
            candidate_votes[candidate.index(row[2])] = candidate_votes[candidate.index(row[2])] + 1


    

    print("Election Results")
    print("-------------------------")
    print("Total votes:",total_number_of_votes)
    print("-------------------------")
    
    for i  in range(len(candidate)):
        print(candidate[i] +": " + "{:.3f}% ".format(candidate_votes[i]/total_number_of_votes*100) + "({:d})".format(candidate_votes[i]))


    winner_person = candidate[candidate_votes.index(max(candidate_votes))]
    print("Winner: ", winner_person)

    #Exporing to .txt file
    outputfile = os.path.join("./","ElectionResults.txt")
    file = open(outputfile, "w")
    file.write("Election Results" + "\n")
    file.write("-------------------------"+ "\n")
    file.write("Total votes: " + str(total_number_of_votes)  + "\n")
    file.write("-------------------------" + "\n")
    
    for i  in range(len(candidate)):
        file.write(candidate[i] +": " + "{:.3f}% ".format(candidate_votes[i]/total_number_of_votes*100) + "({:d})".format(candidate_votes[i]) +  "\n")


    winner_person = candidate[candidate_votes.index(max(candidate_votes))]
    file.write("Winner: " + winner_person)