import numpy as np
import matplotlib.pyplot as plt 

X = np.array([
			[0,0,1],
			[0,1,1],
			[1,0,1],
			[1,1,1]]) # (4,3)

y = np.array([[0,0,1,1]]).T # (4,1)

#plt.matshow(np.hstack((x,y)), fignum=10, cmap=plt.cm.gray)
#plt.show()

def nonlin(x, derive=False):
	if derive == True:
		return x*(1-x)
	return 1/(1+np.exp(-x))

Xaxis = np.arange(-5,5, 0.2)

#plt.plot(Xaxis, nonlin(Xaxis))
#plt.show()

np.random.seed(1)

# initialise weight

syn0 = 2*np.random.random((3,1)) - 1

for iter in range(15000):
	#forward propagation
	l0 = X
	l1 = nonlin(np.dot(l0, syn0))

	# how bad did we do?
	l1_error = y - l1

	# multiply how much we missed by slope of the sigmoid function
	l1_delta = l1_error * nonlin(l1, True)

	# update weights
	syn0 += np.dot(l0.T, l1_delta)

# After we have trained the network we introduce new data
X = np.array([
			[1,0,0],
			[1,1,0],
			[1,0,0],
			[1,1,0]]) 
l0 = X
l1 = nonlin(np.dot(l0, syn0))

print("Output: ")
print(l1)