#2-5小明“吃土”
budget=int(input())
N=int(input())
e=0
for i in range(0,N):
    a=float(input())
    if 100>a>=50:
        b=a-5
    elif 100<=a<200:
        b=a-15
    elif a>=200:
        b=a-40
    elif a<50:
        b=a
    e=e+b
if 1000>e>=500:
    s=e*0.9
elif e>=1000: