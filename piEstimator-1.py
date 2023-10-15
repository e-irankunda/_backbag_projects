import matplotlib.pyplot as plt
import numpy as np
import random
import time
    
piValue = []
nTrials = []

withinCount = 0

k = True    
while k == True:
    try:
        maxTrials = int(input('Enter the number of trials you want to perform:'))
        radius = int(input('Enter the radius you want to use:'))
        k = False
            
    except:
        print('Only integers accepted! Try again...')
    
tInitial = time.time()
    
for trial in range(1,maxTrials):
    x = random.uniform(-1*radius, radius)
    y = random.uniform(-1*radius, radius)
    
    if np.sqrt(x**2 + y**2) < radius:
        withinCount += 1
        
    piValue.append(4 * withinCount / trial)
        
        
tFinal = time.time()
    
piEstim = 4 * withinCount / maxTrials
print(f'PI estimates to {piEstim}, after {maxTrials} simulations.')
print(f'The real value of PI = {np.pi}')
print()
    
#how close is the estimated pi value to the actual pi
percentError= 100*(np.pi-piEstim)/np.pi
print(f'The margin error = {percentError} %')
    
#how time does it take to run all the process?
timing = tFinal - tInitial
print(f'The elapsed time for calculations = {timing} s')
    
plt.figure(facecolor = 'green')
plt.axes().set_facecolor(color = 'black')
plt.plot(piValue, color='red', linewidth = 4)
plt.title('PI Estimator, CARLO-MONTE METHOD')
plt.xlabel('Simulations Performed')
plt.ylabel('PI value')
plt.grid(color='yellow', linewidth=0.5, alpha=0.5)
plt.show()
