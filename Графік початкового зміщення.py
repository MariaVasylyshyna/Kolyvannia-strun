import matplotlib.pyplot as plt
import numpy as np
import math
pi=math.pi

#f(x)=Asin(3pi*x/L)
def fourier_fi(x,n):
    a0=2*A/(3*pi)
    s=a0
    for k in range(1,n):
        r=pi*k/L
        r0=3*pi/L
        if k!=3:
            a1=A*r0*((-1)**k+1)/(r0**2-r**2)
            b1=0
        else:
            a1=0
            b1=A*L/2
        ak=2*a1/L
        bk=2*b1/L
        
        s=s+ak*np.cos(r*x)+bk*np.sin(r*x)
    return s/2

def fourier_string(x,n):
    y=[]
    for i in range(len(x)):
        y.append(fourier_fi(x[i],n))
    return y
A=0.007
L=0.63
L1=round(0.3*L,1)
print('L1=',L1)
n1=7

x1=np.arange(0,L*100)/100
y1=fourier_string(x1,n1)
y1_2=A*np.sin(3*pi*x1/L)

fig1=plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)

yox=[0]*len(x1)
xoy=[0,0,0]
yoy=[-1.2*A,0,1.2*A]
ax1.plot(x1,yox)
ax1.plot(xoy,yoy)
ax1.plot(x1, y1_2, linewidth=2)
ax1.plot(x1, y1, linewidth=2)
ax1.set_xlabel('x', fontsize=10)
ax1.set_ylabel(r'$\phi(x)$', fontsize=10)


#f(x)={h1x/L1, 0<xL1; h1(L–x)/(L–L1), L1<x<L)}
def fourier_fi_2(x,n):
    a0=h1/2
    s=a0
    for k in range(1,n):
        r=pi*k/L
        a1=math.cos(r*L1)*h1*L/(L1*(L-L1)*r**2)
        a2=-(h1*(-1)**k)/((L-L1)*r**2)-h1/(L1*r**2)
        ak=2*(a1+a2)/L
        
        b1=h1*L*math.sin(r*L1)/(L1*(L-L1)*r**2)
        bk=2*b1/L
        
        s=s+ak*np.cos(r*x)+bk*np.sin(r*x)
    return s/2

def fourier_string_2(x,n):
    y=[]
    for i in range(len(x)):
        y.append(fourier_fi_2(x[i],n))
    return y
n2=7
h1=A
y2=fourier_string_2(x1,n2)
x2_2=[0,L1,L]
y2_2=[0,h1,0]

fig2=plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
yox=[0]*len(x1)
xoy=[0,0,0]
yoy=[-0.2*A,0,1.2*A]
ax2.plot(x1,yox)
ax2.plot(xoy,yoy)
ax2.set_xlabel('x', fontsize=10)
ax2.set_ylabel(r'$\phi(x)$', fontsize=10)
ax2.plot(x2_2, y2_2, linewidth=2)
ax2.plot(x1, y2, linewidth=2)
# plt.axis('equal')
plt.show()