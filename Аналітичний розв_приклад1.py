import math 
import numpy as np
import matplotlib.pyplot as plt

def fi(xx):
    return fi_m*math.sin(pi*xx*3/(L))

def psi(x):
    return 0
# АНАЛІТИЧНИЙ РОЗВ'ЯЗОК
# функція початкового зміщення - f(x)=Asin(3pi*x/L)

# t<<h/(q^0.5)

fi_m=0.007
F=96
M=0.00495
L=0.63
q=F*L/M
print('q=',q)
T=2*L/(3*q**0.5)
n=160
m=180
h=L/n
t=T/m
p=h**2/(q*t**2)
krok_t=10  # t*krok_t - різниця в часі між зображеними графіками
print('h=',h,' t=',t)
pi=math.pi

x=[h*k for k in range(0,n)]
y=[t*k for k in range(0,m)]
        
kx=[[0]*(n) for k in range(m)]
for j in range(m):
    for i in range(n):
        kx[j][i]=fi_m*math.sin(3*pi*i*h/L)*math.cos(3*pi*(q**0.5)*j*t/L)

#побудова графіків
fig1=plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
yox=[0]*len(x)
xoy=[0,0,0]
yoy=[-1.2*fi_m,0,1.2*fi_m]
plt.ylim([-1.2*fi_m, 1.2*fi_m])
ax1.plot(x,yox)
ax1.plot(xoy,yoy)
ax1.set_xlabel('x', fontsize=10)
ax1.set_ylabel(r'$\xi(x)$', fontsize=10)
for k in range(0,m,krok_t):
    ax1.plot(x,kx[k])

#plt.axis('equal')
plt.show()
