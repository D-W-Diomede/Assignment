class members:

    def __init__(self,fname="",sname="",distance=0.0):
        self.fname = fname
        self.sname = sname
        self.distance = distance
    

def getMemberData():
    memberData=[]
    import csv
    with open('members.txt','r') as data:
        memberinfo=csv.reader(data,delimiter=',')
        for row in memberinfo:
            memberData.append(members(row[0],row[1],float(row[2])))
            print(row[0],row[1],row[2])
            print(memberData)
        return memberData

def maxDistanceWalked(memberData):
    maxDistance=memberData[0].distance
    for x in range(len(memberData)):
            if memberData[x].distance>maxDistance:
                maxDistance = memberData[x].distance
                print(maxDistance)
    return maxDistance

def showMaxDistance(maxDistance):
    print("The maximum distance walked is {}".format(maxDistance))

def createResults(memberData,maxDistance):
    with open('results.txt','w') as resultsfile:
        resultsfile.write("Walking club results file\n")
        resultsfile.write("First Name               Second Name\n")
        resultsfile.write("-------------------------------------\n")
        for x in range(len(memberData)):
            if memberData[x].distance > 0.7*maxDistance:
                resultsfile.write("{}{}".format(memberData[x].fname,memberData[x].sname.rjust(18)))
                resultsfile.write("\n")
        resultsfile.close()

memberdata=getMemberData()
maxDistance=maxDistanceWalked(memberdata)
showMaxDistance(maxDistance)
createResults(memberdata,maxDistance)
