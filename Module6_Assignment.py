# zcrowell_module6_assignment.py
# international gymnastics scoring
# last edited by Zane Crowell Oct. 20, 2020
# CSCI 111 Section 002

# define all variables:
    # gymnastScore = float(0.0)
    # count = int(1)
    # judgeCount = int(1)
    # scoreList = []
    # totalScore = float(0.0)
    # avgScore = (judgeScore() / 6) 

# define function asking for scores and adding them:
def judgeScore():
    # establish function variables:
    count = int(1)
    judgeCount = int(1)
    scoreList = []
    # obtain scores from 6 judges:
    while count < 7:
        print("Judge",judgeCount,"- please enter your score below:")
        gymnastScore = float(input("\tScore: "))
        scoreList.append(gymnastScore)
        count += 1
        judgeCount += 1
    # reset judgeCount variable:
    judgeCount = int(1)
    # sum scores:
    totalScore = sum(scoreList)
    # print scores:
    for score in scoreList:
        print("Score for Judge",judgeCount,"-  ",score)
        judgeCount += 1
    # return sum of scores for use in averageScore() function
    return totalScore

# define function to find average of six input scores
def averageScore():
    avgScore = (judgeScore() / 6) 
    print("The average score is:",round(avgScore, 2))
    
# calling the averageScore function: 
averageScore()




        







