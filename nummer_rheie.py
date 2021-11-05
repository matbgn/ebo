import random
MAX_LIST = 72
MAX_NUM = 60
FACTOR_MAX_VAL = 12

ONLY_MAX = True

dict_reihe = [MAX_NUM] if ONLY_MAX else list(range(MAX_NUM))

for i in range(round(MAX_LIST/2)):
    iTempVal = random.choice(dict_reihe)
    iTmpFactor = random.randrange(1,FACTOR_MAX_VAL)
    print(iTmpFactor, "*", iTempVal, "=") #,iValTmp*iTmp)
    iTmpDivision = random.choice(dict_reihe) * random.randrange(1,FACTOR_MAX_VAL)
    print(iTmpDivision, "/", iTempVal, "=") #,(iTmp - (iTmp % iValTmp))/iTmp)
