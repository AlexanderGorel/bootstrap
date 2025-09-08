import numpy as np
import matplotlib.pyplot as plt

# combine distributions, assuming they are Gaussian, into a new distribution

def combinedistributions(means,stds,nsamples):
    distribution=[]
    for n in range(len(means)):
        distribution.extend(np.random.normal(means[n],sds[n],nsamples).tolist())
    return distribution

means=[
1.683,
1.604,
1.686,
1.818,
1.745,
1.559,
1.723,
1.506,



]
sds=[
0.0566,
0.0606,
0.0473,
0.0868,
0.0965,
0.0492,
0.0812,
0.0596,


]
print(np.std(means))
nsamples=100
ntries=100
mean,std=[],[]
for n in range(ntries):
    distribution=combinedistributions(means,sds,nsamples)
    mean.append(np.mean(distribution))
    std.append(np.std(distribution))
print(np.mean(mean),'+/-',np.mean(std))
plt.hist(distribution)
plt.grid()
plt.show()
