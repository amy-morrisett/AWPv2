import random
import math

def printPartner(studentName):
    return 'You will be working with ' + studentName + ' on your class project!'

auroraAcademyDict = {
    'kani': ["Zenda", "Darius", "Mykal", "Alexandra"],
    'aura sight': ["Zenda", "Kyomi", "Lana", "Devi", "Mai", "Will", "Kenji", "Alden", "Sorrel", "Namiko"],
    'koah': ["Willow"],
    'teaching': ["Ferris", "Keli"],
    'psychich powers': ['Astrid'],
    'enti': ['Camille'],
    'emotion painting': [],
    'image singing': ['Chen'],
    'freezing powers': [],
    'levitation': ['Stella', 'Torin'],
    'sound painting': ['Sophia']
}

def chooseRandomElement(list):
    return list[math.floor(random.uniform(0, 1) * len(list))]

def classProjectPartner(gift, studentDict):
    for x in studentDict:
        partnerList = studentDict[x]
        if x == gift:
            if len(partnerList) == 0:
                allStudentsList = []
                for y in studentDict:
                    currentList = studentDict[y]
                    for z in currentList:
                        if z in allStudentsList:
                            continue
                        allStudentsList.append(z)
                randomFriend = chooseRandomElement(allStudentsList)
                return "I'm sorry -- you have no partner because you are the only student in your class! However, you can be friends with" + randomFriend + " !"
            else:
                randomStudent = chooseRandomElement(partnerList)
                return printPartner(randomStudent)

print(classProjectPartner('kani', auroraAcademyDict))
print(classProjectPartner('aura sight', auroraAcademyDict))
print(classProjectPartner('emotion painting', auroraAcademyDict))