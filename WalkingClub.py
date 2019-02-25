class members:

    def __init__(self,fname="",sname="",distance=0.0):
        self.fname = fname
        self.sname = sname
        self.distance = distance
    

def getMemberData():
    memberData=[]
    import csv
    with open('members.txt') as data:
        memberinfo=csv.reader(data)
        for row in memberinfo:
            memberData.append(members(row[0],row[1],row[2]))
        return memberData

def maxDistanceWalked(memberData):
    maxDistance=memberData[0].distance
    for x in memberData:
            if memberData[x.distance>maxDistance]:
                maxDistance = memberData[x].distance
                print(maxDistance)
    return maxDistance

def showMaxDistance(maxDistance):
    print("The maximum distance walked is {}".format(maxDistance))

def createResults(memberData,maxDistance):
    with open('results.txt','w') as resultfile:
        resultsfile.write("Walking club results file")
        resultsfile.write("First Name\tSecond Name")
        resultsfile.write("-------------------------------------")
        for x in memberData:
            if x.distance > 0.7*maxDistance:
                resultsfile.write("{}\t{}".format(memberData[x.fname],memberData[x.sname]))
        resultsfile.close()

memberdata=getMemberData()
maxDistance=maxDistanceWalked(memberdata)
showMaxDistance(MaxDistance)
createResults(memberdata,maxDistance)
