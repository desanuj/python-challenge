import os
import csv

os.chdir(os.path.dirname(__file__))

filepath = os.path.join("./Resources", "election_data.csv")


with open(filepath, newline ="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    next(csv_reader, None)

    totalc = 0
    khanc = 0
    correyc = 0
    lic = 0
    otooleyc = 0
    khanc = 0
    correyc = 0
    lic = 0
    otooleyc = 0
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    votes = [khanc, correyc, lic, otooleyc]
    winner = ""
    for row in csv_reader:
        totalc += 1
        if row[2] == "Khan":
            khanc += 1
        elif row[2] == "Correy":
            correyc += 1
        elif row[2] == "Li":
            lic += 1
        elif row[2] == "O'Tooley":
            otooleyc += 1
    
    winner = candidates[votes.index(max(votes))]

    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalc}")
    print("-------------------------")
    print(f"Khan: {round(khanc*100/totalc, 4)}% ({khanc})")
    print(f"Correy: {round(correyc*100/totalc, 4)}% ({correyc})")
    print(f"Li: {round(lic*100/totalc, 4)}% ({lic})")
    print(f"O'Tooley: {round(otooleyc*100/totalc, 4)}% ({otooleyc})")
    print("-------------------------")
    print(f"Winner: {winner}")

    file = open('PyPollResults.txt','w+')
 
    file.write("Election Results")
    file.write(f"Total Votes: {totalc}")
    file.write("-------------------------")
    file.write(f"Khan: {round(khanc*100/totalc, 4)}% ({khanc})")
    file.write(f"Correy: {round(correyc*100/totalc, 4)}% ({correyc})")
    file.write(f"Li: {round(lic*100/totalc, 4)}% ({lic})")
    file.write(f"O'Tooley: {round(otooleyc*100/totalc, 4)}% ({otooleyc})")
    file.write("-------------------------")
    file.write(f"Winner: {winner}")
 
    file.close() 
        



