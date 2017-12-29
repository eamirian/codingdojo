# Assignment: Type List

l=['magical unicorns',19,'hello',98.98,'world']
tS=[]
tI=0
i = 0
while (i < (len(l))):
    if type(l[i]) is str:
        tS.append(l[i])
    elif type(l[i]) is int:
        tI += l[i]
    i = i + 1

if len(tS) >0 and tI>0:
    print "The list you entered is of mixed type"
elif tI > 0:
    print "The list you entered is of integer type"
else:
    print "The list you entered is of string type"
s= ' '.join(tS)
print "String:", s
print "Sum:", tI