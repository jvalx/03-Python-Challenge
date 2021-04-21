import os
import csv

election_data_csv = os.path.join('PyPoll/Resources', 'election_data.csv')
countList = []
nameList = []



with open(election_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')
    next(csvreader, None)
    for row in csvreader:
        countList.append(row[0])
        nameList.append(row[2])

sum = 0.0
KhanCount = 0.0
CorreyCount = 0.0
LiCount = 0.0
OtooleyCount = 0.0
for i in range(len(countList)):
    sum += 1
    if nameList[i] == 'Khan':   
        KhanCount += 1
    elif nameList[i] == 'Correy':
        CorreyCount += 1
    elif nameList[i] == 'Li':
        LiCount += 1
    else: 
        OtooleyCount += 1

print("Election Results" + '\n' + ('-' * 20) + '\n' + "Total Votes: " + str(sum)
        + '\n' + ('-' * 20) + '\n' + "Khan: " + str(round((KhanCount/sum) * 100,2)) + "%  (" + str(KhanCount)
        +  ")" + '\n' + "Correy: " + str(round((CorreyCount/sum) * 100,2)) + "%  (" + str(CorreyCount)
        +  ")" + '\n' + "Li: " + str(round((LiCount/sum) * 100,2)) + "%  (" + str(LiCount)
        +  ")" + '\n' + "O'Tooley: " + str(round((OtooleyCount/sum) * 100,2)) + "%  (" + str(OtooleyCount)
        +  ")" + '\n' + ('-' * 20) + '\n' + "Winner: Khan" + '\n' + ('-' * 20))


#w tells python we are opening the file to write into it
outfile = open('PollResults.txt', 'w')

outfile.write("Election Results" + '\n' + ('-' * 20) + '\n' + "Total Votes: " + str(sum)
        + '\n' + ('-' * 20) + '\n' + "Khan: " + str(round((KhanCount/sum) * 100,2)) + "%  (" + str(KhanCount)
        +  ")" + '\n' + "Correy: " + str(round((CorreyCount/sum) * 100,2)) + "%  (" + str(CorreyCount)
        +  ")" + '\n' + "Li: " + str(round((LiCount/sum) * 100,2)) + "%  (" + str(LiCount)
        +  ")" + '\n' + "O'Tooley: " + str(round((OtooleyCount/sum) * 100,2)) + "%  (" + str(OtooleyCount)
        +  ")" + '\n' + ('-' * 20) + '\n' + "Winner: Khan" + '\n' + ('-' * 20))

outfile.close()
