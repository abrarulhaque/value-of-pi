i=1
j=0
x=0
while True:
    y=(-1)**j
    p=1/i
    q=y*p
    x=x+q
    j=j+1
    i=i+2
    if j%10000==0:
        q=input("press 'q' to quit:")
        if q=='q':
            break
print("value of py:")
print(4*x)
