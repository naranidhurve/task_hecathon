
t=int(input("enter the num"))
l=int(input("enter the num"))
i=t
c=0
while i<=l:
    k=i%10
    if k==2 or k==3 or k==9:
        c=c+1
    i=i+1
print(c)

