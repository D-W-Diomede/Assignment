class members:

    def __init__(self,fname="",sname="",distance=0.0):
        self.fname = fname
        self.sname = sname
        self.distance = distance
        self.marathons = self.distance // 26.22
            

def getMemberData():
    memberData=[]
    import csv
    with open('members.txt','r') as data:
        memberinfo=csv.reader(data,delimiter=',')
        for row in memberinfo:
            memberData.append(members(row[0],row[1],float(row[2])))
        return memberData

def maxDistanceWalked(memberData):
    maxDistance=memberData[0].distance
    for x in range(len(memberData)):
            if memberData[x].distance>maxDistance:
                maxDistance = memberData[x].distance
    return maxDistance

def showMaxDistance(maxDistance):
    print("\nThe maximum distance walked is {}".format(maxDistance))

def createResults(memberData,maxDistance):
    with open('results.txt','w') as resultsfile:
        resultsfile.write("Walking club results file\n\n")
        
        resultsfile.write("[PRIZE WINNERS]\n")
        resultsfile.write("\nFirst Name     Second Name")
        resultsfile.write("\n---------------------------\n")
        for x in range(len(memberData)):
            if memberData[x].distance > 0.7*maxDistance:
                resultsfile.write("{}{}".format(memberData[x].fname,memberData[x].sname.rjust(15)))
                resultsfile.write("\n")

        resultsfile.write("\n\nClub Member Statistics | Marathons ran by each member")
        resultsfile.write("\n\nFirst Name     Second Name     Marathons Ran")
        resultsfile.write("\n---------------------------------------------------------\n")
        for x in range(len(memberData)):
            resultsfile.write("{}{}\t\t\t{}".format(memberData[x].fname,memberData[x].sname.rjust(15),int(memberData[x].marathons)))
            resultsfile.write("\n")
        resultsfile.close()

memberdata=getMemberData()
maxDistance=maxDistanceWalked(memberdata)
showMaxDistance(maxDistance)
createResults(memberdata,maxDistance)
