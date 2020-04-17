import math
def f1(x):
    val=-(x*x)+3*x+2
    return val

def f2(x):
    val=-80*(x*x)+3*x+2
    return val

def f3(x):
    val=-8*(x*x)+3*x+2
    return val
print('#------------------1-------------------#')
a=-4
b=5
tol=0.2
ep=0.01
interval=math.log((b-a)/tol)/math.log(2)
internval=math.ceil(interval)

for i in range(0,internval+1):
    x1=((a+b)/2)-ep
    x2=((a+b)/2)+ep
    f1x1=f1(x1)
    f1x2=f1(x2)
    
    if(f1x1)>=f1x2:
        b=x2
    else:
        a=x1
    print("%d %.3f %.3f %.3f %.3f"% (i,x1,x2,f1x1,f1x2))
xStar=(a+b)/2

print('XStra=%.3f' %(xStar))

print('#----------------2---------------------#')
a=-5
b=1
tol=0.3
ep=0.02
interval=math.log((b-a)/tol)/math.log(2)
internval=math.ceil(interval)

for i in range(0,internval+1):
    x1=((a+b)/2)-ep
    x2=((a+b)/2)+ep
    f1x1=f1(x1)
    f1x2=f1(x2)
    
    if(f1x1)>=f1x2:
        b=x2
    else:
        a=x1
    print("%d %.3f %.3f %.3f %.3f"% (i,x1,x2,f1x1,f1x2))
xStar=(a+b)/2

print('XStra=%.3f' %(xStar))

print('#----------------3---------------------#')
a=-8
b=-2
tol=0.25
ep=0.03
interval=math.log((b-a)/tol)/math.log(2)
internval=math.ceil(interval)

for i in range(0,internval+1):
    x1=((a+b)/2)-ep
    x2=((a+b)/2)+ep
    f1x1=f1(x1)
    f1x2=f1(x2)
    
    if(f1x1)>=f1x2:
        b=x2
    else:
        a=x1
    print("%d %.3f %.3f %.3f %.3f"% (i,x1,x2,f1x1,f1x2))
xStar=(a+b)/2

print('XStra=%.3f' %(xStar))

