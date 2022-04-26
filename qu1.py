

def num(a,l):
    i=0
    string=""
    while i<l:
        j=str(a[i])
        n=j[-1]
        string=string+n
        i=i+1
    print(string)
    if (int(string))%10==0:
        print ("yes")
    else:
        print ("no")
a=[85, 25 ,65 ,21 ,84]
l=len(a)
e=num(a,l)
print(e)


