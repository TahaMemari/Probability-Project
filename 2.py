import numpy as np
import matplotlib.pyplot as plt

#initials
y = 0
x = 0
n = [200,100,600,400] #final numbers of markov chain
N = 1000 #number of repeats
pn = [0.5,0.25,0.75,0.9] #probabilities of each step
Xn = [0] * 1000
X0 = 0

#Simulate Markov chain using nested loops
fig, axs = plt.subplots(4, 4,figsize=(8, 8), layout="constrained")
for k in n:
    for p in pn:
        for i in range(N):
            X0 = 0
            for j in range(k):
                X0 = X0 + 2*np.random.binomial(1, p) - 1
            Xn[i] = X0
        counts, bins = np.histogram(Xn)
        axs[x,y].hist(bins[:-1], bins, weights=counts);
        axs[x,y].set_title('n = '+ str(k) +', p = '+str(p))
        y = y + 1
    x = x + 1
    y = 0

#plot different conditions of Xn
plt.show()