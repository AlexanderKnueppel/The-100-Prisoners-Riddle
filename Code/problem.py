# 100 Prisoner Problem:
# The 100 prisoners problem is a mathematical problem in probability theory and combinatorics. 
# In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers 
# in order to survive. The rules state that each prisoner may open only 50 drawers and cannot 
# communicate with other prisoners. At first glance, the situation appears hopeless, but a clever 
# strategy offers the prisoners a realistic chance of survival.
#
# Usually, one thinks that the success probability is very low (e.g., the first prisoner has a success
# prob. of 50%,... the second also 50%. Together, they should have no more than 25% of successful tries...)
#
# For large N (= rounds), the success probability of the optimal strategy is actually  over 30%.
#
# This short python script is an implementation of this strategy to emperically see that this is the case.

import random
import matplotlib.pyplot as plt

def OptimalStrategy(N, P):
    failures = 0

    for n in range(N):
        drawers = random.sample(range(P), P)
        idx = 0
        while idx < P:
            # Create loop
            loop = [drawers[idx]]
            while True:
                next = drawers[loop[-1]]
                drawers[loop[-1]] = -1
                if next == loop[0]:
                    break
                loop.append(next)

            if len(loop) > 50:
                failures += 1
                break

            # Move idx
            while idx < P and drawers[idx] == -1:
                idx += 1
    return float(1-failures/N)

P = 100 # Number of prisoners

D = [2**x for x in range(15)]
H = []

for d in D:
    H.append(OptimalStrategy(d, P))

print(H)
index = range(len(D))
plt.bar(index, H, 0.5, color="blue")
plt.xticks(index, D) # labels get centered
plt.show()