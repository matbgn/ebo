import random
MAX_LIST = 72*2
MAX_NUM = 60
# Numerator is not random:
bIsFixValue = True

for i in range(round(MAX_LIST/2)):
    if bIsFixValue:
        iTempNumerator = MAX_NUM
    else:
        iTempNumerator = random.choice(list(range(2, MAX_NUM)))
    iTmpDenominator = random.randrange(1, iTempNumerator, 1)
    print(iTempNumerator, "-", iTmpDenominator, "=")