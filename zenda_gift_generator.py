import random
import math

def printResult(gift):
    return 'Congratulations -- your gift is ' + gift + '!'

myAnswerDict = {
    'kani': 'a',
    'aura sight': 'c',
    'koah': 'b',
    'teaching': 'c',
    'psychich powers': 'b',
    'enti': 'a',
    'emotion painting': 'a',
    'image singing': 'c',
    'freezing powers': 'a',
    'levitation': 'a'
}

soundPaintingAnswerDict = {
    'kani': 'a',
    'aura sight': 'c',
    'koah': 'b',
    'teaching': 'c',
    'psychich powers': 'b',
    'enti': 'a',
    'emotion painting': 'c',
    'image singing': 'c',
    'freezing powers': 'a',
    'levitation': 'a'
}

def chooseRandomElement(list):
    return list[math.floor(random.uniform(0, 1) * len(list))]

def determineGift(answerDict):
    cAnswers = []
    bAnswers = []
    aAnswers = []
    gift = 'none'

    if answerDict['emotion painting'] == 'c' and answerDict['image singing'] == 'c':
        gift = 'sound painting'
    else:
        for x in answerDict:
            currentGift = x
            if answerDict[currentGift] == 'c':
                cAnswers.append(x)
            if answerDict[currentGift] == 'b':
                bAnswers.append(x)
            if answerDict[currentGift] == 'a':
                aAnswers.append(x)
        if len(cAnswers) == 0:
            if len(bAnswers) == 0:
                gift = chooseRandomElement(aAnswers)
            else:
                gift = chooseRandomElement(bAnswers)
        else:
            gift = chooseRandomElement(cAnswers)
    
    return printResult(gift)

#print(determineGift(myAnswerDict))
print(determineGift(soundPaintingAnswerDict))