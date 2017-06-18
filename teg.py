import numpy as np
import copy
import sys

def roll_attack(n):
    if n >= 4: nrolls=3
    else:      nrolls=n-1
    dice = np.random.randint(1,7,nrolls)
    dice.sort()
    return dice[::-1]


def roll_defend(n):
    if n >= 4: nrolls=3
    else:      nrolls=n
    dice = np.random.randint(1,7,nrolls)
    dice.sort()
    return dice[::-1]


def fight(nattack,ndefend):
    this_nattack=copy.deepcopy(nattack)
    this_ndefend=copy.deepcopy(ndefend)
    while True:
        dice_attack = roll_attack(this_nattack) 
        dice_defend = roll_defend(this_ndefend)
        lim = int(min(len(dice_attack),len(dice_defend)))
        diference = dice_attack[0:lim] - dice_defend[0:lim]
        for i in range(lim):
            if diference[i] > 0: 
                this_ndefend -= 1
            else:
                this_nattack -= 1 
        if this_ndefend <= 0:
            status = 'Win'
            break
        elif this_nattack < 2:
            status = 'Lost'
            break
 
    return status

def run(nattack,ndefend):
    nsample = 50000

    if nattack < 2: exit('ERROR: El numero de atacantes debe ser mayor a 2')
    if ndefend <= 0: exit('ERROR: El numero de defensores debe ser mayor a 0!')

    wins = 0
    loss = 0
    for i in range(nsample):
        status = fight(nattack,ndefend)    
        if status == 'Win': wins += 1
        elif status == 'Lost': loss += 1
        else: exit('ERROR')

    print '                 Probabilidad'
    print 'Atacan Defienden     de exito'
    print '   %3i       %3i       %5.1f'%(nattack,ndefend,wins*100/float(nsample))+'%'


    
run(int(sys.argv[1]),int(sys.argv[2]))    
