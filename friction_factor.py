#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 02:57:49 2020

@author: teesha
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:52:16 2020

@author: teesha
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 00:46:57 2020

@author: payneta2
"""# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Friction factor for a straight pipe 
# Dimensions of pipe and fluid properties of water at T=20 degree Celsius
epsilon= 4.6e-3    # relative roughness for commercial steel unit cm 
density= 998       # density of water units Kg/m^3
d_vis= 0.001005    # dynamic viscosity units  N*s/m^2
d= 1.7120          # diameter of the pipe unit cm

def fF_L(Re):
    """Define the function for laminar flow.
    Re: Value for Reynolds number """
    return 64./Re
     
def fF_T(Re):
    """Define the function for turbulant flow using the Swamee-Jain correlation.
    To solve, the denominator (den) of the equation was broken into 
    its left and right components.
    Re: Value for Reynolds number """
    
    left_side = (epsilon/d)/3.7
    right_side = 5.74/(Re**0.9)

    den = np.log10(left_side + right_side)**2

    result = 0.25/den
    return result 
   
# The flow is considered laminar if the Reynolds number is < 2300
Re_L = np.linspace(int(800), int(2.3e3), int(1e3))
f1 = fF_L(Re_L)

# The flow is considered turbulant if the Reynolds number is > 2300
Re_T = np.linspace(int(2.3e3),int(100e3), int(3e3))
f2 = fF_T(Re_T)

plt.figure(figsize=(15,7))
plt.plot(Re_L, f1,'-b', label='Laminar')
plt.plot(Re_T, f2, '-r', label='Turbulant')
plt.xscale('log')
plt.yticks(np.arange(0.02, 0.09, 0.015))
plt.xlabel('Reynolds number')
plt.ylabel('Friction factor')
plt.grid()
plt.legend()

plt.savefig('pipe.png')