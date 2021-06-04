import random
MAX_LIST = 72
MAX_NUM = 12

dict_reihe = list(range(MAX_NUM)) # [7]

for i in range(round(MAX_LIST/2)):
    iTempVal = random.choice(dict_reihe)
    iTmpFactor = random.randrange(1,MAX_NUM)
    print(iTmpFactor, "*", iTempVal, "=") #,iValTmp*iTmp)
    iTmpDivision = random.choice(dict_reihe) * random.randrange(1,MAX_NUM)
    print(iTmpDivision, "/", iTempVal, "=") #,(iTmp - (iTmp % iValTmp))/iTmp)
