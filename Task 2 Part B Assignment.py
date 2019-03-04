# Ross Andrew
# Task 2B Assignment
# Kilwinning Academy

class Members():
    def __init__(self,forename="",surname="",distance=0.0):
        self.forename=forename
        self.surname=surname
        self.distance=distance

def getData():
    membersData=[]
    import csv
    with open ('members.txt','r') as membersfile:
        membersdetails=csv.reader(membersfile, delimiter=',')
        for x in membersdetails:
            membersData.append(Members(x[0],x[1],float(x[2])))
    membersfile.close()
    return membersData

def findFurthest(membersData):
    furthest=membersData[0].distance
    for index in range(len(membersData)):
        if membersData[index].distance>furthest:
            furthest=membersData[index].distance
    return furthest

def displayFurthest(furthest):
    print("The furthest distance walked was",furthest)

def prizeWinners(membersData,furthest):
    import csv
    winnersfile=open("prize_winners_file.txt","w")
    winnersfile.write("The prize winning members are:\n")
    for x in membersData:
        if x.distance>0.7*furthest:
            winnersfile.write(x.forename+" "+x.surname+"\n")
    winnersfile.write("\nThe number of whole marathons walked by each member is:\n")
    for y in range(len(membersData)):
        marathons=membersData[y].distance/26.22
        whole_marathons=int(marathons)
        winnersfile.write(membersData[y].forename+","+membersData[y].surname+","+str(whole_marathons)+"\n")
        

membersData=getData()
furthest=findFurthest(membersData)
displayFurthest(furthest)
prizeWinners(membersData,furthest)
