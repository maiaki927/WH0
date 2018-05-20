import os
import sys


#print(sys.argv[1])
q=sys.argv[1]
if(q[-1]=='/'):
    ax=sys.argv[1]+'words.txt'
else:
    ax=sys.argv[1]+'/words.txt'
f = open(ax,'r')
a=f.read()

a=a.split(' ')

t = open("words3.txt", "w+")
for c in range (len(a)):

    k=a.count(a[0])
    t.write(a[0].rstrip('\n')+' '+str(c)+' '+str(k)+' \r\n')
    if(len(a)>1):

        a = [x for x in a if x != a[0]]
    else:
        break;




