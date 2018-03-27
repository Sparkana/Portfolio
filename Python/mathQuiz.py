#Quiz + results storage

#Imports
import random as rd
import numbers
import csv

#Constants
password = "mathquiz123"
maxQuestions = 10
mathSigns = ["+","-","*"]
fieldnames = ["Name", "Score1", "Score2", "Score3"]

#Variables
currentQuestion = 1
userType = ""

name = ""
classNo = 0
score = 0


#Gets the student's details for storage
def getDetails():
    #Get name
    global name
    global classNo
    while name == "":    
        name = input("Enter your name: ").upper()
        if name == "":
            print("Error: No name entered")

    #Get class number
    valid = False
    while not valid:
        try:
            classNo = int(input("Enter class number: "))
            #If input is an int, and is between 0 and 4
            if isinstance(classNo, numbers.Integral) and int(classNo) > 0 and int(classNo) <= 3:
                valid = True
            else:
                print("Error: That class does not exist")
        except:
            print("Error: Invalid class")

#Performas the quiz for the student   
def quiz():
    #Global variables
    global currentQuestion
    global maxQuestion
    global score

    #Local variables
    score = 0

    #Welcome message
    print("Welcome to the maths quiz!")
    print("Coming up are 10 random addition, subtraction or multiplication questions.")
    input("Press enter to start. ")

    #Asks 10 questions
    while currentQuestion <= maxQuestions:
        print("Question %d: " % currentQuestion)

        #Generate random question parts
        num1 = rd.randint(1,15)
        num2 = rd.randint(1,15)
        op = rd.choice(mathSigns)
        
        #Calculate answer
        if op == "+":
            ans = num1 + num2
        if op == "-":
            ans = num1 - num2
        if op == "*":
            ans = num1 * num2
        #print(ans) #Debugging

        #Print question
        userAns = input("%d %s %d = " % (num1, op, num2))
        try:
            if int(userAns) == ans:
                score += 1
                print("Correct!")
            else:
                print("Incorrect, the answer was %d" % ans)
        except:
            print("Incorrect, the answer was %d" % ans)
        
        currentQuestion += 1    

    print("\nYou scored %d out of %d." % (score, maxQuestions))

#Store data into the class file
def storeData():
    global name
    global classNo
    global score
    score1 = ""
    score2 = ""

    #Open the class file
    classFile = open("class%s.csv" % classNo, "r+", newline="")
    csvWriter = csv.DictWriter(classFile, fieldnames=fieldnames)
    csvReader = csv.DictReader(classFile, fieldnames=fieldnames)

    #if not csv.Sniffer().has_header("class%s.csv" % classNo):
    csvWriter.writeheader()
    
    #for row in csvReader:                  #Debugging
    #    print(row["Name"], row["Score1"])  #Debugging

    #Get previous scores
    for row in csvReader:
        if row["Name"] == name:
            score1 = row["Score1"]
            score2 = row["Score2"]
    
    #Write score to file
    csvWriter.writerow({"Name": name, "Score1": score, "Score2": score1, "Score3": score2})

    #Close file
    classFile.close()
    
    
#Returns the results to the teacher
def returnResults(classNo, sortType):
    #Open the class file
    classFile = open("class%s.csv" % classNo, "r", newline="")
    csvReader = csv.DictReader(classFile, fieldnames=fieldnames)

    print()
    
    if sortType == 1: #Alphabetically
        userList = []
        #Compare each name to the current list, only get unique names
        for row in csvReader:
            new = True
            #print(row)
            for item in userList:
                if row["Name"] == item:
                    new = False
            #Skip headers
            if new and row["Name"] != "Name":
                userList.append(row["Name"])
        #print(userList)    #Debugging

        #Get each of the students' highest score out of the last 3

        scoreDict = {}
        for item in userList:
            #Restart file
            classFile = open("class%s.csv" % classNo, "r", newline="")
            csvReader = csv.DictReader(classFile, fieldnames=fieldnames)
            revCsvReader = [x for x in csvReader]
            highScore = 0
            
            #csvReader = reversed(list(csv.DictReader(classFile, fieldnames=fieldnames)))
            #print(csvReader)
            for row in revCsvReader[::-1]:
                if row["Name"] == item:
                    try:
                        if int(row["Score1"]) > highScore:
                            highScore = int(row["Score1"])
                        if int(row["Score2"]) > highScore:
                            highScore = int(row["Score2"])
                        if int(row["Score3"]) > highScore:
                            highScore = int(row["Score3"])
                    except:
                        pass
                    break
                #print(row)     #Debugging
            scoreDict[item] = highScore
        #print(scoreList)

        #Reverses the list, sorted in decending order.
        userList.sort()
        '''
        print(scoreList)   #Debugging
        print(scoreDict)   #Debugging
        '''

        #Print the students alphabetically with their high score
        print("Students alphabetically: ")
        for user in userList:
            print("%s: %d" % (user, scoreDict[user]))

    if sortType == 2: #Highest score
        userList = []
        #Compare each name to the current list, only get unique names
        for row in csvReader:
            new = True
            #print(row)
            for item in userList:
                if row["Name"] == item:
                    new = False
            #Skip headers
            if new and row["Name"] != "Name":
                userList.append(row["Name"])
        '''
        #print(userList)    #Debugging
        '''
        
        #Get each of the students' highest score out of the last 3

        scoreList = []
        scoreDict = {}
        for item in userList:
            #Restart file
            classFile = open("class%s.csv" % classNo, "r", newline="")
            csvReader = csv.DictReader(classFile, fieldnames=fieldnames)
            revCsvReader = [x for x in csvReader]
            highScore = 0
            
            #csvReader = reversed(list(csv.DictReader(classFile, fieldnames=fieldnames)))
            #print(csvReader)
            for row in revCsvReader[::-1]:
                if row["Name"] == item:
                    try:
                        if int(row["Score1"]) > highScore:
                            highScore = int(row["Score1"])
                        if int(row["Score2"]) > highScore:
                            highScore = int(row["Score2"])
                        if int(row["Score3"]) > highScore:
                            highScore = int(row["Score3"])
                    except:
                        pass
                    break
                #print(row)     #Debugging
            scoreList.append(highScore)
            scoreDict[item] = highScore
        #print(scoreList)

        #Reverses the list, sorted in decending order.
        scoreList.sort(reverse=True)
        '''
        print(scoreList)   #Debugging
        print(scoreDict)   #Debugging
        '''
        
        #Print the student and their high score (passed 3), by high score
        print("Students by high score: ")
        for score in scoreList:
            for key in scoreDict:
                if score == scoreDict[key] and key in userList:
                    print("%s: %d" % (key, score))
                    userList.remove(key)

    if sortType == 3: #Average score
        userList = []
        #Compare each name to the current list, only get unique names
        for row in csvReader:
            new = True
            #print(row)
            for item in userList:
                if row["Name"] == item:
                    new = False
            #Skip headers
            if new and row["Name"] != "Name":
                userList.append(row["Name"])
        #print(userList)    #Debugging56

        #Get each of the students' avarage score out of the last 3

        scoreList = []
        scoreDict = {}
        for item in userList:
            #Restart file
            classFile = open("class%s.csv" % classNo, "r", newline="")
            csvReader = csv.DictReader(classFile, fieldnames=fieldnames)
            revCsvReader = [x for x in csvReader]
            averageScore = 0
            
            #csvReader = reversed(list(csv.DictReader(classFile, fieldnames=fieldnames)))
            #print(csvReader)
            for row in revCsvReader[::-1]:
                if row["Name"] == item:
                    total = 0
                    count = 0
                    try:
                        if int(row["Score1"]) != "":
                            total += int(row["Score1"])
                            count += 1
                        if int(row["Score2"]) != "":
                            total += int(row["Score2"])
                            count += 1
                        if int(row["Score3"]) != "":
                            total += int(row["Score3"])
                            count += 1
                    except:
                        pass
                    averageScore = total / count
                    #print(averageScore)    #Debugging
                    break
                #print(row)     #Debugging
            scoreList.append(averageScore)
            scoreDict[item] = averageScore
        #print(scoreList)

        #Reverses the list, sorted in decending order.
        scoreList.sort(reverse=True)
        #print(scoreList)   #Debugging
        #print(scoreDict)   #Debugging

        #Print the student and their average score (passed 3), by high score
        print("Students by average score: ")
        for score in scoreList:
            for key in scoreDict:
                if score == scoreDict[key] and key in userList:
                    print("%s: %2.2f" % (key, score))
                    userList.remove(key)
        

#Gets whether the user is a teacher or student
def getUserType():
    global userType
    
    userType = input("Are you a (s)tudent or a (t)eacher?: ").lower()
    while userType != "s" and userType != "t":
        print("Error: Invalid entry.")
        userType = input("Are you a (s)tudent or a (t)eacher?: ").lower()
    return userType

#START
userType = getUserType()
#Student
if userType == "s":
        getDetails()
        quiz()
        storeData()

#Teacher
elif userType == "t":
    classNo = 0
    #Validate class number
    valid = False
    passInput = input("Enter the password: ")
    if passInput == password:
        while not valid:
            try:
                classNo = int(input("Enter class number: "))
                #If input is an int, and is between 0 and 4
                if isinstance(classNo, numbers.Integral) and int(classNo) > 0 and int(classNo) <= 3:
                    valid = True
                else:
                    print("Error: That class does not exist")
            except:
                print("Error: Invalid class")
        #Validate sort type
        print("Sort methods:\n(1). Alphabetically\n(2). Highest score\n(3). Average score")
        valid = False
        while not valid:
            try:
                sortType = int(input("Enter sort number (1,2,3): "))
                #If input is an int, and is between 0 and 4
                if isinstance(sortType, numbers.Integral) and int(sortType) > 0 and int(sortType) <= 3:
                    valid = True
                else:
                    print("Error: That sort type does not exist")
            except:
                print("Error: Invalid sort type")
        
        #Returns the values from the stores
        returnResults(classNo, sortType)
    else:
        print("Bad password")




        
