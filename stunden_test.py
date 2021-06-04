#!/usr/bin/python3
from datetime import datetime
import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import pi
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--withHands",
                    help='Results either with hands xor blank with time to fulfill by setting to True or False')
args = parser.parse_args()


def update(now, bWithHands, ax):
    plt.cla()
    plt.setp(ax.get_yticklabels(), visible=False)
    ax.set_xticks(np.linspace(0, 2*pi, 12, endpoint=False))
    ax.set_xticklabels(range(1,13))
    ax.set_theta_direction(-1)
    ax.set_theta_offset(pi/3.0)
    ax.grid(False)
    plt.ylim(0,1)
    # now = datetime.now()
    hour= now.hour
    minute = now.minute
    second = now.second
    angles_h =2*pi*hour/12+2*pi*minute/(12*60)+2*second/(12*60*60)-pi/6.0
    angles_m= 2*pi*minute/60+2*pi*second/(60*60)-pi/6.0
    angles_s =2*pi*second/60-pi/6.0

    if bWithHands:
        # ax.plot([angles_s,angles_s], [0,0.9], color="black", linewidth=1)
        ax.plot([angles_m,angles_m], [0,0.7], color="black", linewidth=2)
        ax.plot([angles_h,angles_h], [0,0.3], color="black", linewidth=4)
        plt.title(f'{random.choice(["am","pm","am + pm"])}:___________')

    if not bWithHands:
        ax.plot([0, 0], [0, 0.001], color="black", linewidth=2)
        plt.title(f'{str(hour).zfill(2)}h:{str(minute).zfill(2)}min')

    for i in range(1, 61):
        ticks = 2 * pi * i / 60 - pi / 6.0
        if i % 5 == 0 :
            ax.plot([ticks,ticks], [0.9,1], color="black", linewidth=2)
        else:
            ax.plot([ticks,ticks], [0.95,1], color="black", linewidth=1)
    return ax


fig= plt.figure(figsize=(10,6),dpi=100)

# Results either with hands xor time specified
bWithHands = args.withHands == 'True'  # True or False

NB_OF_FIG = 8
NB_Y = 2
NB_X = 4
for iFig in range(1, NB_OF_FIG+1):
    for i in range(1, NB_X+1):
        for j in range(1,NB_Y+1):
            iTmp = int(NB_Y*100 + NB_X*10 + iFig)
            ax = fig.add_subplot(iTmp, polar=True)
            update(datetime(2021, 3, 13, random.randrange(0,23), random.randrange(0,59), 0, 878062), bWithHands, ax)

# Packing all the plots and displaying them
plt.tight_layout()
plt.show()




