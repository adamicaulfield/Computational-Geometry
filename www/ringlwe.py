import numpy as np
import matplotlib.pyplot as plt
import random


# User determines these things
print("---------- USER INITIALIZES ----------")
d = 2
q = 19
psi = [1] + [0]*(d-1) + [1]

print("Parameters:")
print("d="+str(d)+" q="+str(q))

print("psi(x)= ")
print(np.poly1d(psi))
print("R_q = Z_q[x]/psi(x) \tInitialize ring mod psi(x) with coefficients mod q")

s = []
for i in range(0, d):
	s.append(random.randint(0,q))

print("Secret key:")
print(np.poly1d(s))



# User determines these things
print("---------- CLOUD REQUESTS Public Key ----------")
# Cloud requests public key
a = []
e = []
for i in range(0, d):
	a.append(random.randint(0,q)) # random element on R_q
	e.append(int(np.random.normal(q, 2*q))%q) #gaussian error

print("User samples elements a-<R_q and e<-chi")
print("a:")
print(np.poly1d(a))
print("e:")
print(np.poly1d(e))

print("User generates b =  a*s+e")

# b = a*s+e
b = np.polymul(a,s)
print(b)
b = np.polyadd(b,e)
print(b)
b = (np.polydiv(b,psi))[1]%q # ensure b is Z_q[x]/psi(x)

print("b:")
print(np.poly1d(b))

print("User returns public key: tuple (a,b)")

m = 25
print("-------------- ATTACK: attacker requests a public keys m="+str(m)+" times-------------")

A = []
B = []
B_uni = []
for i in range(0, m):
	a = []
	e = []
	bu = []
	for i in range(0, d):
		a.append(random.randint(0,q)) # random element on R_q
		bu.append(random.randint(0,q)) # random element on R_q
		e.append(int(np.random.normal(q, 2*q))%q) #gaussian error

	# b = a*s+e
	b = np.polymul(a,s)
	b = np.polyadd(b,e)
	b = (np.polydiv(b,psi))[1]%q # ensure b is Z_q[x]/psi(x)

	A.append(a)
	B.append(b)
	B_uni.append(bu)

print("All (a,b)'s:")
for i in range(0,len(A)):
	print("("+str(A[i])+","+str(B[i])+")")

for i in range(0,len(A)):
	# plt.plot([A[i][0],B[i][0]], [A[i][1],B[i][1]], "k-")
	# plt.plot(A[i][0], A[i][1], "bo")
	plt.plot(B_uni[i][0], B_uni[i][1], "bo")
	plt.plot(B[i][0], B[i][1], "go")

plt.plot(s[0],s[1],"ro")
plt.show()