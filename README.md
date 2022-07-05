<p align="center">
<img width="400" height="400" src="https://upload.wikimedia.org/wikipedia/commons/0/05/100_prisoners_problem_qtl1.svg" alt="Banner">
</p>

# The 100 Prisoners Riddle

Very small experimental repository for the 100 Prisoners Riddle

## 💡 According to Wikipedia (https://en.wikipedia.org/wiki/100_prisoners_problem):

>The 100 prisoners problem is a mathematical problem in probability theory and combinatorics. In this problem, 100 numbered prisoners must find their own numbers in one of 100 drawers in order to survive. The rules state that each prisoner may open only 50 drawers and cannot communicate with other prisoners. At first glance, the situation appears hopeless, but a clever strategy offers the prisoners a realistic chance of survival. 

## Solutioon

The future goal of this repository is twofold: 
 - Code the strategy in Python that maximizes the successful outcome (... surprisingly, this is over 30%!)
 - Employ *lean* to define the problem and give a proof of a lower bound for the optimal strategy. 

## Result

Fascinating :) A bar plot of the results:

<p align="center">
<img width="600" src="https://user-images.githubusercontent.com/263321/177413311-1426b169-90c7-4be9-988a-2cb65db77430.png" alt="Histogram">
</p>

With higher number of tries, the success rate is constantly over 30%.
