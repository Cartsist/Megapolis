def srav(a, b):
    if a<b:
        return True
    else:
        return False
f = open('game').read()
f=f.split('\n')
a=[]

for i in f:
    a.append(i.split('$'))
i=1
while i < len(a)-1:
    if (srav(a[i][0],a[i-1][0])):
        while i ==1 or srav(a[i][0],a[i-1][0]) !=False:
            s=a[i-1]
            a[i-1]=a[i]
            a[i]= s
            i-=1

    i+=1
print(a)

