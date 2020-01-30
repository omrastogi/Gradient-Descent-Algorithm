import numpy as np

def grad_descend(x,y,theta0,theta1,alpha=0.01):
	m = len(x)
	for i in range(0,30):
		h = hypothesis(theta0, theta1, x)
		j = cost_function(h,y)
		theta0 = theta0 - alpha*((h-y).dot(x))/m
		theta1 = theta1 - alpha*((h-y).dot(x))/m
		print (theta0, theta1)
	print (h)
	print (j)

	
def hypothesis(theta0,theta1,x):
	h = theta0+theta1*x
	return h

def cost_function(h,y):
	j = (1/(2*len(y)))*np.sum((h-y))
	return j 

def main():
	alpha = 0.01
	x = [1,2,3,4,5,6,7,8,9]
	x = np.array(x)
	theta0 = theta1 = 0 
	#theta0 = theta1 = 2
	#h = [4,6,8,10,12,14,16,18,20]
	y = [5,7,9,11,16,14,15,19,20]
	y = np.array(y)

	#y = np.array(y)print (cost_function(h,y))
	grad_descend(x,y,theta0,theta1,alpha)
	

main()