import random
import math

userAnswerDict = {
    'kani': None,
    'aura sight': None,
    'koah': None,
    'teaching': None,
    'psychic powers': None,
    'enti': None,
    'emotion painting': None,
    'image singing': None,
    'freezing powers': None,
    'levitation': None
}

def putAnswerInDict(selection, giftName):
    if selection in ('a', 'b', 'c'):
        userAnswerDict[giftName] = selection
        return True
    print("Not a valid input! Please choose a, b, or c :)")
    return False

#txt = input("Type something to test this out: ")

#print(f"Is this what you just said? {txt}")
while True:
    kaniAnswer = input("1. What is your success rate of keeping houseplants alive?\na. Basically every plant I've ever owned has died (pick this one as well if you haven't ever owned a houseplant)\nb. I'm fairly good, but have had my fair share of dead plants\nc. I'm excellent at keeping them alive and rarely have them die!\n")
    if putAnswerInDict(kaniAnswer, 'kani'):
        break

while True:
    auraSightAnswer = input("2. How good are you at sensing someone's ~vibes~?\na. Pretty horrible; I always have trouble telling how others are feeling\nb. I'd say I'm a fairly good judge of someone else's emotions/nc. The best -- I have a high success rate of sensing others' feelings\n")
    if putAnswerInDict(auraSightAnswer, 'aura sight'):
        break

while True:
    koahAnswer = input("3. Are you good at caring for animals?\na. Ew, get those gross things away from me\nb. Animals are cute, but I don't really enjoy being responsible for one\nc. Give me all the animals!!!\n")
    if putAnswerInDict(koahAnswer, 'koah'):
        break

while True:
    teachingAnswer = input("4. How good are you at explaining things to other people?\na. I always just get confused stares when I try to explain something\nb. Pretty hit-or-miss; sometimes I can explain things clearly, but other times people get lost\nc. I have top-notch communication skills and am great at explaining things\n")
    if putAnswerInDict(teachingAnswer, 'teaching'):
        break

while True:
    psychicPowersAnswer = input("5. Do you have good intuition for future events?\na. No, everything always seems to surprise me\nb. Sometimes my intuition is trustworthy, and other times it's completely off\nc. Yes, I always seem to be able to predict what will happen and can easily trust my gut\n")
    if putAnswerInDict(psychicPowersAnswer, 'psychic powers'):
        break

while True:
    entiAnswer = input("6. How do you feel about insects?\na. Get them the hell away from me right now\nb. I can handle a pretty butterfly or ladybug, but not a fan of anything else\nc. If I could, I would own my own bug museum\n")
    if putAnswerInDict(entiAnswer, 'enti'):
        break

while True:
    emotionPaintingAnswer = input("7. Are you a fan of visual art?\na. I can appreciate a pretty painting, but not a fan of creating them myself\nb. I love a good sketching or painting session every once in a while\nc. I am the next Picasso; my work even seems to evoke strong emotions in other people\n")
    if putAnswerInDict(emotionPaintingAnswer, 'emotion painting'):
        break

while True:
    imageSingingAnswer = input("8. How about music?\na. My singing is reserved for the shower\nb. I'll bust out some tunes at karaoke night\nc. I am the next Beyoncé; people cry at my voice\n")
    if putAnswerInDict(imageSingingAnswer, 'image singing'):
        break

while True:
    freezingPowersAnswer = input("9. Do you tend to prefer hot or cold temperatures?\na. Blast the heat, or take me to a tropical island!\nb. Please keep things at a nice room temperature\nc. Take me to the Arctic and give me a snow cone!\n")
    if putAnswerInDict(freezingPowersAnswer, 'freezing powers'):
        break

while True:
    levitationAnswer = input("10. Do you usually get asked to lift heavy items?\na. Nah, not my thing\nb. Sure, if there aren't any stronger people around\nc. Heck yeah, check out these guns\n")
    if putAnswerInDict(levitationAnswer, 'levitation'):
        break

def printResult(gift):
    return 'Congratulations -- your gift is ' + gift + '!'

def chooseRandomElement(someList):
    return someList[math.floor(random.uniform(0, 1) * len(someList))]

def determineGift(answerDict):
    cAnswers = []
    bAnswers = []
    aAnswers = []
    gift = ''

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
#print(determineGift(soundPaintingAnswerDict))
print(determineGift(userAnswerDict))
