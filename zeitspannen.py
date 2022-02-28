import random


def create_journey():
    hours_begin = random.randint(0, 23)
    minutes_begin = random.randint(0, 59)
    print(f'\nDépart {str(hours_begin).zfill(2)}:{str(minutes_begin).zfill(2)}')
    hours_end = random.randint(0, 23)
    minutes_end = random.randint(0, 59)
    print(f'Arrivée {str(hours_end).zfill(2)}:{str(minutes_end).zfill(2)}')
    delta = hours_end + minutes_end / 60 - hours_begin - minutes_begin / 60
    delta = delta if delta > 0 else 24 + delta
    print(f'{"{:.0f}".format(delta)}h{str(int(round(delta % 1 * 6000)/100)).rjust(2, "0")}')


for i in range(9):
    create_journey()
