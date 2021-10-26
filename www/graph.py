import numpy as np
import matplotlib.pyplot as plt
import random

q = 7;
n = 2;
m = 2;

debug = True

if(debug):
	A =[[1,6],[5,0]]
	s = [3, 1]
	e = [1,1]
else:
	A = []
	for i in range(0, m):
		a = []
		for j in range(0, n):
			a.append(random.randint(0,q))
		A.append(a)

	s = []
	for i in range(0, n):
		s.append(random.randint(0,q))

	e = []
	for i in range(0, m):
		e.append(random.randint(0,int(q/2)))

print("Matrix A: "+str(A))
print("Vector s: "+str(s))
print("Vector e: "+str(e))

b = np.mod(np.matmul(A,s),q)
b = np.mod(np.add(b, e),q)
print("b = As+e = "+str(b))

print("Basis vectors: of L(A)")
basis = []
for j in range(0, n):
	v = []
	for i in range(0, m):
		v.append(A[i][j])
	print(v)
	basis.append(v)

x = []
y = []
for i in range(0, 10):
	for j in range(0, 10):
		c1v1 = np.array(basis[0])*i
		c2v2 = np.array(basis[1])*j
		tmp = np.add(c1v1,c2v2)
		x.append(tmp[0])
		y.append(tmp[1])

print(x)
print(y)

plt.plot(x,y,'ro')
plt.plot(b[0],b[1],'bo')
plt.show()