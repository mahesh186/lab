import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
j=cm.sqrt(-1)
def dft(x):
	N=len(x)
	y=[]
	for k in range(0,N,1):
		sum=0
		for n in range(0,N,1):
			sum=sum+x[n]*np.exp((-j*(2*np.pi)*n*k)/N)
		y.append(sum)
	return y
#now the program of dft starts
x=np.array(input('enter a sequence:'))
y=dft(x)
#print y
plt.subplot(1,2,1)
plt.title('MAGNITUDE PLOT',color='r')
plt.xlabel('SAMPLES',color='r')
plt.ylabel('MAGNITUDE',color='r')
plt.stem(np.abs(y),color='g')
plt.subplot(1,2,2)
plt.title('PHASE PLOT',color='r')
plt.xlabel('SAMPLES',color='r')
plt.ylabel('ANGLE IN PI',color='r')
plt.stem(np.angle(y),color='g')
plt.show()

