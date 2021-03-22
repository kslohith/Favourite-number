# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 12:08:54 2018

@author: K.S.LOHITH
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


N = 30
d = 10
number_of_selected = [0] * d
sum_of_rewards = [0] * d
reward = ""
total_reward = 0
number_selected = []
my_reward = 0
for n in range( 0 , N ):
    number = 0
    maximum_upper_limit = 0
    for i in range(0 , d):
        if( number_of_selected[i] > 0 ):
           average_reward = (sum_of_rewards[i] / number_of_selected[i])
           delta = ( math.sqrt((3/2) * ( math.log(n + 1)/number_of_selected[i] )) )
           upper_limit = average_reward + delta
        else:
            upper_limit = 1e400
        if( upper_limit > maximum_upper_limit ):
            maximum_upper_limit = upper_limit
            number = i
    number_selected.append(number)
    print( "Do you like the number " + str(number) + " " )
    reward = (input())
    if( reward == "yes" or reward == "YES" ):
           my_reward = 1
    else:
           my_reward = 0
           
    number_of_selected[number] += 1
    sum_of_rewards[number] += my_reward
    total_reward += my_reward
    
    plt.hist(number_selected)
    plt.xlabel('favorite number')
    plt.ylabel('number of times selected')