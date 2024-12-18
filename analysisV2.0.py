def readCsv():
    """Assembles list of dictionaries, each match is an index in the list.
    A match is represented by a dictionary containing the info for that match.
    The range in the nested loop has to match the number of values, just trust me I can't fix it"""
    matches = open(r'C:\Users\barne\OneDrive\Desktop\Desktop\programs\data5.csv', 'r', encoding = 'utf-8')
    total = []
    accum = 0
    for line in matches:
        if accum == 0:
            firstline = line.strip().split(",")
        else:
            nextline = line
            data = nextline.strip().split(",")
            nextdictionary = {}
            for i in range(20):
                nextdictionary[firstline[i]] = data[i]
                
            total.append(nextdictionary)
        accum = accum + 1
    return total

def NumOfMatches(matches):
    "creates a dic of the number of recorded matches for each team"
    teams = {}
    for i in range(len(matches)-1):
        teamnum = str(matches[i]["TEAM Number"])
        if teamnum in teams:
            teams[teamnum] = int(teams[teamnum]) + 1
        else:
            teams[teamnum] = 1
    return teams

def eachTeam(matches):
    "creates a dic of 0s for each team"
    teams = {}
    for i in range(len(matches)-1):
        teamnum = str(matches[i]["TEAM Number"])
        if teamnum not in teams:
            teams[teamnum] = 0
    return teams

def listTeams(matches):
    "creates a list for each team"
    teams = []
    for i in range(len(matches)-1):
        teamnum = str(matches[i]["TEAM Number"])
        if teamnum not in teams:
            teams.append(teamnum)
    return teams

def averageTele(matches):
    "creates a dic of the averge teleop score for each team"
    teamShots = eachTeam(matches)
    teamMatches = NumOfMatches(matches)
    teamAverage = eachTeam(matches)
    teams = listTeams(matches)
    shots = 0
    for i in range(len(matches)-1):
        if matches[i]["Total Teleop shots taken."] != "" and int(matches[i]["Total Teleop shots taken."]) < 100:
            shots = matches[i]["Total Teleop shots taken."]
        else:
            shots = 0
        teamnum = matches[i]["TEAM Number"]
        teamShots[teamnum] = int(teamShots[teamnum]) + int(shots)
    for team in teams:
        teamAverage[team] = float(teamShots[team]) / float(teamMatches[team])
    return teamAverage

def teleAccuracy(matches):
    "calcuates the percentage of successful shots. value of 0 if no shots taken"
    teams = listTeams(matches)
    teamShots = eachTeam(matches)
    teamScores = eachTeam(matches)
    teamAccuracy = eachTeam(matches)
    shots = 0
    successshots = 0
    for i in range(len(matches)-1):
        if matches[i]["Total Teleop shots taken."] != "" and int(matches[i]["Total Teleop shots taken."]) < 100:
            shots = matches[i]["Total Teleop shots taken."]
        else:
            shots = 0
        teamnum = matches[i]["TEAM Number"]
        teamShots[teamnum] = int(teamShots[teamnum]) + int(shots)
    for i in range(len(matches)-1):
        if matches[i]["Total Telop shots scored."] != "" and int(matches[i]["Total Telop shots scored."]) < 100:
            successshots = matches[i]["Total Telop shots scored."]
        else:
            successshots = 0
        teamnum = matches[i]["TEAM Number"]
        teamScores[teamnum] = int(teamScores[teamnum]) + int(successshots)
    for team in teams:
        if teamShots[team] != 0:
            teamAccuracy[team] = (float(teamScores[team]) / float(teamShots[team]))*100
        else:
            teamAccuracy[team] = 0
    return teamAccuracy

def taxiLine(matches):
    "returns a boolean dict if each team can cross the taxi line"
    taxiteams = eachTeam(matches)
    for i in range(len(matches)-1):
        teamnum = matches[i]["TEAM Number"]
        cross = str(matches[i]["Did they across the taxi line?"])
        if taxiteams[teamnum] != "yes" and cross == "yes":
            taxiteams[teamnum] = "yes"
    return taxiteams

def maxAuto(matches):
    "returnes a dict of the max number of auto shots for each team"
    teamAuto = eachTeam(matches)
    currentShots = 0
    for i in range(len(matches)-1):
        if matches[i]["How many successful autonomous shots?"] != '':
            currentShots = matches[i]["How many successful autonomous shots?"]
        else:
            currentShots = 0
        teamnum = matches[i]["TEAM Number"]
        if int(teamAuto[teamnum]) < int(currentShots) and int(currentShots) <= 6 and int(currentShots)>=0:
            teamAuto[teamnum] = int(currentShots)
    return teamAuto

def averageAuto(matches):
    "returns a dict of the average number of shots made in auto for each team"
    teamShots = eachTeam(matches)
    teamMatches = NumOfMatches(matches)
    teamAverage = eachTeam(matches)
    teams = listTeams(matches)
    shots = 0
    for i in range(len(matches)-1):
        if (matches[i]["How many successful autonomous shots?"] != ""
        and int(matches[i]["How many successful autonomous shots?"]) < 100):
            shots = matches[i]["How many successful autonomous shots?"]
        else:
            shots = 0
        teamnum = matches[i]["TEAM Number"]
        teamShots[teamnum] = int(teamShots[teamnum]) + int(shots)
    for team in teams:
        teamAverage[team] = float(teamShots[team]) / float(teamMatches[team])
    return teamAverage

def maxClimb(matches):
    "returnes a dict of the max height of the climb for each team"
    teamClimb = eachTeam(matches)
    currentclimb = ""
    for i in range(len(matches)-1):
        if matches[i]["What level did they climb?"] != '':
            currentclimb = matches[i]["What level did they climb?"]
        else:
            currentclimb = "no"
        teamnum = matches[i]["TEAM Number"]
        if teamClimb[teamnum] == 0:
            teamClimb[teamnum] = currentclimb
        elif teamClimb[teamnum] == "no":
            teamClimb[teamnum] = currentclimb
        elif teamClimb[teamnum] == "Low":
            if currentclimb == "Mid" or currentclimb == "High" or currentclimb == "Traversal":
                teamClimb[teamnum] = currentclimb
        elif teamClimb[teamnum] == "Mid":
            if currentclimb == "High" or currentclimb == "Traversal":
                teamClimb[teamnum] = currentclimb
        elif teamClimb[teamnum] == "High":
            if currentclimb == "Traversal":
                teamClimb[teamnum] = currentclimb
    return teamClimb

def averageClimbPoints(matches):
    "returns the average points earned by climbing per match per team"
    teamClimbs = eachTeam(matches)
    teamMatches = NumOfMatches(matches)
    teamAverage = eachTeam(matches)
    teams = listTeams(matches)
    currentclimb = ""
    for i in range(len(matches)-1):
        climbvalue = -1
        if (matches[i]["What level did they climb?"] != ""):
            currentclimb = matches[i]["What level did they climb?"]
        else:
            currentclimb = "no"
        teamnum = matches[i]["TEAM Number"]
        if currentclimb == "Traversal":
            climbvalue = 15
        elif currentclimb == "High":
            climbvalue = 10
        elif currentclimb == "Mid":
            climbvalue = 6
        elif currentclimb == "Low":
            climbvalue = 4
        elif currentclimb == "no":
            climbvalue = 0
        teamClimbs[teamnum] = int(teamClimbs[teamnum]) + int(climbvalue)
    for team in teams:
        teamAverage[team] = float(teamClimbs[team]) / float(teamMatches[team])
    return teamAverage

def averageIndPoints(matches):
    """returnes the average points earned independently per match per team. Climb, auto, cargo
    WARNING: ASSUMES SCORING ON UPPER HUB!!! There was no info on upper/lower on the sheet, so I did what I could"""
    teams = listTeams(matches)
    averageTeam = eachTeam(matches)
    teamAuto = averageAuto(matches)
    teamCargo = averageTele(matches)
    teamClimb = averageClimbPoints(matches)
    taxi = taxiLine(matches)
    for team in teams:
        total = (teamAuto[team]*4) + (teamCargo[team]*2) + teamClimb[team]
        if taxi[team] == "yes":
            total = total + 2
        averageTeam[team] = total
    return averageTeam

def findMax(dic, matches):
    "Returns the biggest number from a dictonary"
    teams = listTeams(matches)
    ma = 0
    for team in teams:
        if ma < dic[team]:
            ma = dic[team]
    return float(ma)

def weighter(matches, avTeleW, teleAccW, taxiLW, mAutoW, avAutoW, mClimbW, avClimbW, avIndPointsW):
    "Gives the weighted score out of 100. Each input is"
    teams = listTeams(matches)
    weightedTeams = eachTeam(matches)
    avTele = averageTele(matches)
    teleAcc = teleAccuracy(matches)
    taxiL = taxiLine(matches)
    mAuto = maxAuto(matches)
    avAuto = averageAuto(matches)
    mClimb = maxClimb(matches)
    avClimb = averageClimbPoints(matches)
    avIndPoints = averageIndPoints(matches)
    TLscore = 0
    MCscore = 0
    for team in teams:
        ATscore = int((avTele[team]/findMax(avTele, matches))*100)
        TAscore = int((teleAcc[team]/findMax(teleAcc, matches))*100)
        MAscore = int((mAuto[team]/findMax(mAuto, matches))*100)
        AAscore = int((avAuto[team]/findMax(avAuto, matches))*100)
        ACscore = int((avClimb[team]/findMax(avClimb, matches))*100)
        AIPscore = int((avIndPoints[team]/findMax(avIndPoints, matches))*100)
        if taxiL[team] == "yes":
            TLscore = 100
        else:
            TLscore = 0
        if mClimb[team] == "Traversal":
            MCscore = 100
        elif mClimb[team] == "High":
            MCscore = 75
        elif mClimb[team] == "Mid":
            MCscore = 50
        elif mClimb[team] == "Low":
            MCscore = 25
        elif mClimb[team] == "no":
            MCscore = 0
        score = (ATscore*avTeleW + TAscore*teleAccW + MAscore*mAutoW + AAscore*avAutoW + ACscore*avClimbW +
        AIPscore*avIndPointsW + TLscore*taxiLW + MCscore*mClimbW)
        weightedTeams[team] = score
    return weightedTeams
        
def main():
    "main"
    print("*************************************")
    print("Welcome to the auto-analyzer! Version 1.0")
    print("You will be asked to weight the robot's info!")
    print("Think of weight like a weighted grade, enter a num between 0 and 1 for each answer.")
    print("There are 8 categories: averageTele, teleAccuracy, taxiLine, maxAuto, averageAuto, maxClimb,")
    print("averageClimbPoints, and averageIndPoints(WARNING: averageIndPoints ASSUMES UPPER HUB!!!)")
    print("This program works best if the numbers add up to 1, but they don't necessarily have to!")
    print("The closer a robot's score is to 100, the closer they were to being the best in their categorie(s)!")
    print("All right, get ready to enter your values!!")
    print("*************************************")
    avTeleW = float(input("Enter the weight for the average cargo scored:" ))
    teleAccW= float(input("Enter the weight for the Teleop Accuracy Score: "))
    taxiLW = float(input("Enter the weight for crossing the Taxi Line: "))
    mAutoW = float(input("Enter the weight for the maximum Auto points: "))
    avAutoW = float(input("Enter the weight for the average Auto Points: "))
    mClimbW = float(input("Enter the weight for the maximum Climbing Points:"))
    avClimbW = float(input("Enter the weight for the average Climbing Points:"))
    avIndPoints = float(input("Enter the weight for the average individual score (ASSUMES UPPER HUB! USE WITH CAUTION!): "))
    print("*************************************")
    print("Value input complete! Let me get those robots for you:")
    print("*************************************")
    teams = listTeams(readCsv())
    avTele = averageTele(readCsv())
    teleAcc = teleAccuracy(readCsv())
    taxiL = taxiLine(readCsv())
    mAuto = maxAuto(readCsv())
    avAuto = averageAuto(readCsv())
    mClimb = maxClimb(readCsv())
    avClimb = averageClimbPoints(readCsv())
    avIndPoint = averageIndPoints(readCsv())
    numMatch = NumOfMatches(readCsv())
    score = weighter(readCsv(), avTeleW, teleAccW, taxiLW, mAutoW, avAutoW, mClimbW, avClimbW, avIndPoints)
    for i in range(len(teams) - 1):
        for j in range(i + 1, len(teams)):
            if score[teams[j]] > score[teams[i]]:
                tmp = teams[i]
                teams[i] = teams[j]
                teams[j] = tmp
    length = int(input("How long would you like the list to be? "))
    choice = input("Do you want full details? (Y or N) ")
    print("*************************************")
    if choice == "N" or choice =="n":
        for i in range(length):
            if numMatch[teams[i]] > 1:
                print(f"{teams[i]} Score: {score[teams[i]]:.2f}")
                print("*************************************")
            else:
                length = length + 1
    if choice == "Y" or choice == "y":
        for i in range(length):
            if numMatch[teams[i]] > 1:
                print(f"{teams[i]}, Score: {score[teams[i]]:.2f}, Average Cargo Scored: {avTele[teams[i]]:.2f},")
                print(f"Teleop Accuracy: {teleAcc[teams[i]]:.2f}%, Taxi Line: {taxiL[teams[i]]},")
                print(f"Average Auto Score: {avAuto[teams[i]]:.2f}, Max Auto Score: {mAuto[teams[i]]},")
                print(f"Max Climb: {mClimb[teams[i]]}, Average Climb Score: {avClimb[teams[i]]:.2f},")
                print(f"Average Individual Points (Assumes top hab!): {avIndPoint[teams[i]]:.2f}")
                print("*************************************")
            else:
                length = length+ 1
            
main()