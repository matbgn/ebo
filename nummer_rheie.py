import random

# Calculate for which operation:
DIVISION = True
MULTIPLICATION = True

HOW_MUCH_OUTPUT_VALUES = 60
# if ALLOW_DUPLICATE is false it takes precedence on HOW_MUCH_OUTPUT_VALUES
ALLOW_DUPLICATE = False

FACTOR_MAX_VAL = 12

MAX_NUM = 12
# Calculate all the range till MAX_NUM or only MAX_NUM?
ONLY_MAX = True

NUM_LIST = []
NUM_LIST = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]

# MAX_NUM or NUM_LIST?
dict_reihe = [MAX_NUM] if ONLY_MAX else list(range(2, MAX_NUM))
dict_reihe = dict_reihe if len(NUM_LIST) == 0 else NUM_LIST

numberOfValues = round(HOW_MUCH_OUTPUT_VALUES / 2) if ALLOW_DUPLICATE else len(dict_reihe) * FACTOR_MAX_VAL

tempFactorList = []
tempDivisionList = []
for i in range(numberOfValues):
    while True:
        iTempVal = random.choice(dict_reihe)
        iTmpFactor = random.randrange(1, FACTOR_MAX_VAL + 1)
        sTmpValuesCouple = f'{iTmpFactor}x{iTempVal}'
        if sTmpValuesCouple in tempFactorList:
            pass
        else:
            break

        if ALLOW_DUPLICATE:
            break
    tempFactorList.append(sTmpValuesCouple)
    print(iTmpFactor, "*", iTempVal, "=") if MULTIPLICATION else "" #,iValTmp*iTmp)

    while True:
        iTempVal = random.choice(dict_reihe)
        iTmpDivision = iTempVal * random.randrange(1, FACTOR_MAX_VAL + 1)
        sTmpValuesCouple = f'{iTmpDivision}/{iTempVal}'
        if sTmpValuesCouple in tempDivisionList:
            pass
        else:
            break

        if ALLOW_DUPLICATE:
            break
    tempDivisionList.append(sTmpValuesCouple)
    print(iTmpDivision, "/", iTempVal, "=") if DIVISION else ""  # ,(iTmp - (iTmp % iValTmp))/iTmp)

