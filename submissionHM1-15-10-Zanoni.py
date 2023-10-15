##############################
##############################
#PYTHON INTRODUCTION - 7
##############################
##############################
#---------------------------------
#1-SAY "HELLO, WORLD!" WITH PYTHON

string="Hello, World!"
print(string)

#-----------------------------------
#2-IF-ELSE

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2 !=0:
    print("Weird")
    
if n%2==0 and 2<=n<=5:
    print("Not Weird")
    
if n%2==0 and 6<=n<=20:
    print("Weird")
    
if n%2==0 and n>20:
    print("Not Weird")

#-------------------------------
#3- ARITHMETIC OPERATORS

a=int(input())
b=int(input())

sum=a+b
diff=a-b
mol=a*b

print(sum)
print(diff)
print(mol)

#-----------------------------------
#4-PYTHON:DIVISION

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a//b)
    print(a/b)

#-----------------------------------
#5-LOOPS

if __name__ == '__main__':
    n = int(input())
    
for i in range(n):
    print(i*i)


#-----------------------------------
#6-WRITE A FUNCTION

def is_leap(year):
    leap = False
    
    if year%400 ==0:
        leap=True
    elif year%100 ==0:
        leap=False
    elif year%4 ==0:
        leap=True    
        
        
    return leap

year = int(input())
print(is_leap(year))


#-----------------------------------
#7-PRINT A FUNCTION

if __name__ == '__main__':
    n = int(input())
    
    
stringa=""
for i in range(1,n+1):
    elem=str(i)
    stringa+=elem

print(stringa)

#--------------------------------
##############################
##############################
#PYTHON - BASIC DATA TYPES - 6
##############################
##############################
#1-LIST COMPREHENSION

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    

coordinate=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k !=n:
                coordinate.append([i,j,k])
            
print(coordinate)

#---------------------------------
#2- FIND THE RUNNER-UP SCORE!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
        
lista=list(arr)
m1=max(lista)
m2=-101
for elem in lista:
    if elem>m2 and elem!=m1:
        m2=elem
print(m2)

#---------------------------------
#3-NESTED LISTS

if __name__ == '__main__':
    N=int(input())
    records=[]
    grades=[]
    for _ in range(N):
        name = str(input())
        score = float(input())
        records.append([name,score])
        grades.append(score)
        
s=sorted(set(grades))
smin=s[1]
for student,mark in sorted(records):
    if mark==smin:
        print(student)

#---------------------------------
#4- FINDING THE PERCENTAGE
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    

import builtins 
#student_marks[query_name]
somma=0
m=0
for voto in student_marks[query_name]:
    somma+=voto
    m+=1
avf="{:.2f}".format(somma/m)
print(avf)

#--------------------------------
#5- LISTS

if __name__ == '__main__':
    N = int(input())
    result=[]
    for voice in range(N):
        function, *line= input().split()
        value = list(map(float,line))
        if function=="insert":
            result.insert(int(value[0]),int(value[1]))
        
        if function=="print":
            print(result)
        
        if function=="remove":
            result.remove(int(value[0]))
        
        if function=="append":
            result.append(int(value[0]))
        
        if function=="sort":
            result.sort()
        
        if function=="pop":
            result.pop()
            
        if function=="reverse":
            result.reverse()


#--------------------------------
#6-TUPLE

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    
    
import builtins
    
l=list(integer_list)
t=tuple(l)
print(hash(t))

#--------------------------------
##############################
##############################
#PYTHON -PY STRINGS - 14
##############################
##############################

#------------------------------
#1 - SWAP CASE

def swap_case(s):
    s2=[]
    for letter in s:
        if 65<=ord(letter)<=91:
            letter= chr(ord(letter)+32)
        elif 97<=ord(letter)<=123:
            letter= chr(ord(letter)-32)
        s2.append(letter)
    s2="".join(s2)
    return (s2)
    
#alternativly using swapcase
#s=s.swapcase()
#return(s)

#-----------------------------
#2- STRING SPLIT AND JOIN



def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#--------------------------------
#3-WHAT'S YOUR NAME

def print_full_name(first, last):
    convey="Hello " + first + " "+ last+"! You just delved into python."
    print(convey)

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
#----------------------------------
#4-MUTATION

def mutate_string(string, position, character):
    succ=list(string)
    succ[position]=character
    stringa="".join(succ)
    return (stringa)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#--------------------------------------
#5-FIND A STRING
def checkstring(string,sub_string,i):
    l1=list(string)
    l2=list(sub_string)
    for j in range(0,len(l2)):
        if l1[i+j]!=l2[j]:
            return False
    return True

def count_substring(string, sub_string):
    if len(string)<len(sub_string):
        return 0
    count=0
    for i in range((len(string)-len(sub_string))+1):
        count+=(checkstring(string,sub_string,i)==True)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

#--------------------------
#6-STRING VALIDATORS
if __name__ == '__main__':
    s = input()
   
l=list(s) 
l1=[elem.isalnum() for elem in l]
l2=[elem.isalpha() for elem in l]
l3=[elem.isdigit() for elem in l]
l4=[elem.islower() for elem in l]
l5=[elem.isupper() for elem in l]

def ifany(lista):
    for elem in lista:
        if elem==True:
            return True
    return False

print(ifany(l1))            
print(ifany(l2))
print(ifany(l3))
print(ifany(l4))
print(ifany(l5))


#---------------------------------------
#7- TEXT ALIGNMENT

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__=="__main__":
    N=int(input())
        
    for i in range(N):
        print(("H"*i).rjust(N-1)+"H"+("H"*i).ljust(N-1))

    for i in range(N+1):
        print(("H"*N).center(N*2)+("H"*N).center(N*6))

    for i in range((N+1)//2):
        print(("H"*N*5).center(N*6))    

    for i in range(N+1):
        print(("H"*N).center(N*2)+("H"*N).center(N*6))    

    for i in range(N):
        print((("H"*(N-i-1)).rjust(N)+"H"+("H"*(N-i-1)).ljust(N)).rjust(N*6))

#-------------------------------------------------------------
#8- TEXT WRAP

import math

def wrap(string, max_width):
    l=list(string)
    k=math.ceil(len(string)/max_width)
    i=0
    for times in range(k-1):
        pr="".join(l[i:i+max_width])
        print (pr)
        i+=max_width
        
    return("".join(l[i:]))

#-------------------------------------------------------
#9- DESIGNER DOOR MAT

if __name__ == "__main__":
    inp=input()
    n=inp.split(" ")
    N=int(n[0])
    M=int(n[1])
    for i in range(M-1):
        if i==N//2+1:
            wl=(M//2)-3
            print("-"*wl+"WELCOME"+"-"*wl)
        upper(i,N,M)
     
def riga(i,N,M):
    i=max(1+3*i,3)
    trat=M//2-i
    s="-"*trat+".|"
    for j in range(N//2):
        s="-"*trat+".|"
        s+="..|"*i
        print(s)
    #return s
             
             
             i=min(i,2*size-2-i)
    trat=large//2-2*(i)
    s="-"*trat
    for j in range(2*i+1):
        s+=chr(96+size-min(j,2*i-j))
        if j<2*i:
            s+="-"
    s+="-"*trat
    return s  
 

#--------------------------------
#10-STRING FORMATTING
def print_formatted(n):
    g = len(bin(n)[2:])
    for i in range(1, n+1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(dec.rjust(g),octa.rjust(g),hexa.rjust(g),bina.rjust(g))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#------------------------------
#11-ALPHABET RANGOLI

def riga(i,large,size):
    i=min(i,2*size-2-i)
    trat=large//2-2*(i)
    s="-"*trat
    for j in range(2*i+1):
        s+=chr(96+size-min(j,2*i-j))
        if j<2*i:
            s+="-"
    s+="-"*trat
    return s     
    
def print_rangoli(size):
    large=4*size-3
    #(2*size-1)+(2*size-2)
    for i in range(2*size-1):
        print(riga(i,large,size))


#-------------------------------------
#12-CAPITALIZE!

#!/bin/python3

import math
import os
import random
import re
import sys
def solve(s):
    res=list(s)
    if ord(res[0])>=97 and ord(res[0])<=122:
            res[0]=chr(ord(res[0])-32)
    for i in range(2,len(res)):
        if res[i-1]==" ":
            if ord(res[i])>=97 and ord(res[i])<=122:
                res[i]=chr(ord(res[i])-32)
    res="".join(res)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#-------------------------------
#13-THE MINION GAME
def minion_game(string):
    l=len(string)
    substrings = l*(l+1)/2
    kevin= sum([len(string[i:]) for i in range(len(string)) if string[i] in "AEIOU"])
    stuart=substrings-kevin
    
    if kevin==stuart:
        print("Draw")
    if kevin<stuart:
        print( "Stuart",int(stuart))
    if stuart<kevin:
        print ("Kevin",int(kevin))
    
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
    
#---------------------------------------
#14-MERGE THE TOOLS

def merge_the_tools(string, k):
    for i in range(0, len(string),k):
        mono=list(set(string[i:i+k]))
        print("".join(mono))
    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
##############################
##############################
#PYTHON -PY SETS - 13
##############################
##############################

#----------------------------------------
#1-INTRODUCTION TO SETS

def average(array):
    somma=0
    for elem in set(array):
        somma+=elem
    res="{:.3f}".format(somma/len(set(array)))
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
    
#--------------------------------------------
#2-NO IDEA!
def happiness(la,lb,lq):
    score=0
    for elem in lq:
        if elem in la:
            score+=1
        if elem in lb:
            score-=1
    print(score)          

if __name__ =="__main__":
    l=list(input().split())
    lq=list(map(int,input().split()))
    la=set(list(map(int,input().split())))
    lb=set(list(map(int,input().split())))
    happiness(la,lb,lq)
    
 
#--------------------------------------------
#3- SYMMETRIC_DIFFERENCE

if __name__ =="__main__":
    M=int(input())
    a=set(map(int,input().split()))
    N=int(input())
    b=set(map(int,input().split()))
    ab=a.difference(b)
    ba=b.difference(a)
    res=ab.union(ba)
    res=sorted(res)
    for elem in res:
        print(elem)
    

    
#----------------------------------------------
#4-SET.ADD()

if __name__=="__main__":
    N=int(input())
    countries=set()
    for row in range(N):
        stamp=input()
        countries.add(stamp)
    res=len(countries)
    print(res)


#------------------------------------
#5-SET.DISCARD(),.REMOVE(),.POP()

if __name__=="__main__":
    n=int(input())
    elem=set(map(int,input().split()))
    N = int(input())
    instr=[]
    for line in range(N):
        instr.append(input().split())
   # print(instr)
    
    for obj in instr:
       # print(obj)
        if obj[0]=="pop":
            elem.discard(list(elem)[0])
        if obj[0]=="remove" and int(obj[1]) in elem:
            elem.remove(int(obj[1]))
        if obj[0]=="discard":
            elem.discard(int(obj[1]))
        #print(elem)
    
    som=sum(elem)
    print(som)


#--------------------------------------------
#6-SET.UNION() OPERATION

if __name__ =="__main__":
    n=int(input())
    english=set(map(int,input().split()))
    b=int(input())
    french=set(map(int,input().split()))
    union=english.union(french)
    count=0
    for elem in union:
        count+=1
    print(count)

#----------------------------------------------
#7-SET.INTERSECTION() OPERATION

if __name__ =="__main__":
    n=int(input())
    english=set(map(int,input().split()))
    b=int(input())
    french=set(map(int,input().split()))
    intersection=english.intersection(french)
    count=0
    for elem in intersection:
        count+=1
    print(count)


#----------------------------------------------
#8-SET.DIFFERENCE() OPERATION
if __name__ =="__main__":
    n=int(input())
    english=set(map(int,input().split()))
    b=int(input())
    french=set(map(int,input().split()))
    difference=english.difference(french)
    count=0
    for elem in difference:
        count+=1
    print(count)



#-----------------------------------
#9-SET.SYMMETRIC_DIFFERENCE() OPERATION

if __name__ =="__main__":
    n=int(input())
    english=set(map(int,input().split()))
    b=int(input())
    french=set(map(int,input().split()))
    symmetric_difference=english.symmetric_difference(french)
    count=0
    for elem in symmetric_difference:
        count+=1
    print(count)

#-----------------------------------
#10-SET MUTATIONS
def doinstruction(A,B,fun):
    if fun=="intersection_update":
        A.intersection_update(B)
    if fun=="difference_update":
        A.difference_update(B)
    if fun=="symmetric_difference_update":
        A.symmetric_difference_update(B)
    if fun=="update":
        A.update(B)
    
if __name__=="__main__":
    la=int(input())
    A=set(map(int,input().split()))
    op=int(input())
    for i in range(op):
        fundirty=list(input().split())
        fun=fundirty[0]
        B=set(map(int,input().split()))
        doinstruction(A,B,fun)
    print(sum(A))


#----------------------------------------------
#11-THE CAPTAIN ROOM

if __name__=="__main__":
    K=int(input())
    rcus=list(map(int, input().split()))
    cus=set(rcus)
    print (((sum(cus)*K)-(sum(rcus)))//(K-1))
   
   
#-------------------------------------------
#12-CHECK SUBSET

def return_Subs(A,B):
    res=True
    for elem in A:
        if elem not in B:
            res =False
    print(res)

if __name__=="__main__":
    T=int(input())
    for i in range(T):
        na=int(input())
        A=set(map(int,input().split()))
        nb=int(input())
        B=set(map(int,input().split()))
        return_Subs(A,B)
        
        
#--------------------------------------------
#13-CHECK STRICT SUPERSET
if __name__=="__main__":
    A=set(map(int,input().split()))
    sets=int(input())
    arestrictsets=True
    for i in range(sets):
        B=set(map(int,input().split()))
        if B.difference(A)!=set():
            arestrictsets=False
    print(arestrictsets)
    

##############################
##############################
#PYTHON -PY COLLECTIONS - 8
##############################
##############################

#-----------------------------
#1-COLLECTIONS.COUNTER()

from collections import Counter

if __name__=="__main__":
    N=int(input())
    sizes=list(map(int,input().split()))
    C=int(input())
    numtot=[]
    prices=[]
    for i in range(C):
        info=list(map(int,input().split()))
        numtot.append(info[0])
        prices.append(info[1])
    
    #print (Counter(sizes).items())
    #print(Counter(num).values()[1])

    diff=[]
    tot=0
    inter = [value for value in sizes if value in numtot]
    #OBS:it returns also repetition and will be ordered
    #as are ordered in "prices" list with Missing Values
    inter2=set(inter.copy())
    #print("intervallo", inter2)
    for obj in inter2:
     #   print("obj= ", obj)
        for i in range(len(numtot)):
            if obj==numtot[i] and obj in inter:
                tot+=prices[i]
                inter.remove(obj)
                #print(tot, inter)
    
    print(tot)
        
    
#------------------------------------
#2-DEFAULTDICT TUTORIAL

from collections import defaultdict
def returnindex(lis,second,n):
    ind=defaultdict(list)
    for elem in second:
       # print("elemento: ", elem)
        if elem not in lis:
            ind[elem]=[-1]
        else:
            for i in range(n):
                if elem==lis[i]:
                    ind[elem].append(i+1)
                    #  print("diz: ",ind)
    for elem in second:
        s=str(ind[elem])
        if len(ind[elem])>1:
            n=(s[1:-1]).split(", ")
            print((" ").join(n))
        elif len(ind[elem])==1:
            print(str(ind[elem][0]))
        
        
if __name__=="__main__":
    n,m=map(int,input().split())
    a=[]
    for i in range(n):
        a.append(input())
    b=[]
    for j in range(m):
        b.append(input())
        
    returnindex(a,b,n)



#------------------------------
#3-COLLECTIONS.NAMEDTUPLE()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

if __name__=="__main__":
    N=int(input())
    namecolumn=input().split()
    stud=[]
    for i in range(N):
        stud.append(input())
    #print(stud)
    index=-1
    for i in range(4):
        if namecolumn[i]=='MARKS':
            index=i
           # print(index)
    Students = namedtuple('Student','MARKS')
    tot=0
    for i in range(N):
        student=list(stud[i].split())
        tot+=int(student[index])
        #print('student'+str(i),student[index])
    print("{:.2f}".format(tot/N))
        

#-------------------------------------------
#4-COLLECTIONS.ORDERDICT()

from collections import OrderedDict

if __name__=="__main__":
    N=int(input())
    sold=OrderedDict()
    for i in range(N):
        items=list(map(str,input().split()))
        names=str(((items)[0:-1]))
        names=names[2:-2]
        names=names.split("', '")
        names=" ".join(names)
        #print(names)
        sold[names] = sold.get(names, 0) + int(items[-1])
    for names, sold[names] in sold.items():
        print(names, sold[names])

#------------------------------------------------
#5-COLLECITONS.DEQUE

from collections import deque

if __name__ == '__main__':
    N = int(input())
    d=deque()
    for voice in range(N):
        instr=list(input().split())
        function=instr[0]
        if len(instr)>1:
            value =instr[1]
       
        if function=="append":
            d.append(value)
        
        if function=="pop":
            d.pop()
            
        if function=="popleft":
            d.popleft()
        
        if function=="appendleft":
            d.appendleft(value)

    res=[]
    for i in range(len(d)):
        res.append(d[i])  
    res=str(res)         
    d2=res[2:-2].split("', '")
    #print(res)
    res=" ".join(d2)
    print(res)

#-----------------------------------
#6-WORD ORDER

from collections import OrderedDict

if __name__=="__main__":
    rep=OrderedDict()
    for i in range(int(input())):
        s=input()
        if s in rep.keys():
            rep[s] = rep[s] + 1
        rep[s] = rep.get(s,1) 
    print(len(rep.items()))
    print (" ".join(str(rep[s]) for s,rep[s] in rep.items()))

#---------------------------------
#7-COMPANY LOGO

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from operator import itemgetter
from collections import defaultdict


if __name__ == '__main__':
    s = list(input())
    d=defaultdict(int)
    d1=[]
    for l in s:
        d[l]+=1    
    #print(d)
    for e in d:
        d1.append([e,d[e]])
    d1.sort(key=(itemgetter(0)))
    #print("ordinato cont")
    d1.sort(key=(itemgetter(1)),reverse=True)
    
    for i in range(0,3):
        print(d1[i][0],d1[i][-1])

#----------------------
#8-PILING UP!

def pile(e, elem):
    i=0
    j=len(e)-1
    while j>=i:
        if elem>=e[j] and e[j]>=e[i]:
            j-=1
        elif elem>=e[i] and e[i]>=e[j]:
            i+=1
        else:
            return("No")
    return("Yes")
            
            
def sta(cubes):
    if cubes[0]>=cubes[-1]:
        return(pile(cubes[1:],cubes[0])) 
    else:
        return(pile(cubes[:len(cubes)-1],cubes[-1]))
    
if __name__=="__main__":
    for i in range(int(input())):
        l = input()
        e=list(map(int,input().split()))
        print(sta(e))
        
##############################
##############################
#PYTHON -PY-DATA-TIME - 2
##############################
##############################

#-----------------------------------
#1-CALENDAR MODULE

import calendar

m,d ,y = map(int,input().split())
res= calendar.weekday(y, m, d)
if res==0:
    print("MONDAY")
elif res==1:
    print("TUESDAY")
elif res==2:
    print("WEDNESDAY")
elif res==3:
    print("THURSDAY")
elif res==4:
    print("FRIDAY")
elif res==5:
    print("SATURDAY")
elif res==6:
    print("SUNDAY")


#---------------------------------------
#2-TIME DELTA

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    pattern= '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, pattern)
    t2 = datetime.strptime(t2, pattern)
    return str(int(abs((t1-t2).total_seconds())))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()

    
##############################
##############################
#PYTHON -EXEPCTIONS -1
##############################
##############################
    
    
#--------------------------------------------
#1-EXCEPTIONS

N=int(input())
test=[list(map(str, input().split())) for _ in range(N)]
for couple in test:
    try:
        print(int(couple[0])//int(couple[1]))
    except ZeroDivisionError as e:
        print ("Error Code: {}".format(e))
    except ValueError as v:
        print ("Error Code: {}".format(v))
    


##############################
##############################
#PYTHON -BUILTINS- 3
##############################
##############################

#---------------------------------------
#1-ZIPPED


if __name__=="__main__":
    N, X= map(int,input().split())
    sub = []
    for _ in range(X):
        sub.append( map(float, input().split()) ) 
        
    for i in zip(*sub): 
        print( sum(i)/len(i) )
    
    
    
#--------------------------------
#2-PYTHON-SORT-SORT

#!/bin/python3

import math
import os
import random
import re
import sys
from operator import itemgetter 



if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    
    #print(arr)
    res =sorted(arr, key=itemgetter(k))
    for i in range(n):
        s=str(res[i])
        if len(res[i])>1:
            n=(s[1:-1]).split(", ")
            print((" ").join(n))
        elif len(res[i])==1:
            print(str(res[i][0]))

#--------------------------------
#3-ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__=="__main__":
    s=input()
    s=list(s)
    low=[]
    up=[]
    ev=[]
    od=[]
    odds=['1','3','5','7','9']
    for i in range(len(s)):
        if s[i].islower():
            low.append(s[i])
        elif s[i].isupper():
            up.append(s[i])
        elif s[i] in odds:
            od.append(s[i])
        elif s[i] not in odds:
            ev.append(s[i])
    low=sorted(low)
    up=sorted(up)
    od=sorted(od)
    ev=sorted(ev)
    print("".join(low)+"".join(up)+"".join(od)+"".join(ev))
            



######################################
######################################
#PYTHON -MAP AND LAMBDA EXPRESSION- 1
######################################
######################################

#-------------------------------------
#1- MAP AND LAMBDA EXPRESSION
cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    if n==0:
        return([])
    if n==1:
        return([0])
    res=[0,1]
    for i in range(2,n):
        res.append(res[i-1]+res[i-2])
    return(res)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))



##############################
##############################
#PYTHON -PY REGEX- 17
##############################
##############################

#------------------------------------
#1- RE.SPLIT()

regex_pattern = r"\W"


#----------------------------------------
#2-GROUP(), GROUPS(), GROUPDICT()

import re
s0=input()
s = re.search(r'([a-z0-9])\1+',s0)
if s is None:
    print (-1)
else:
    print (s.group(0)[1])

#------------------------------
#3-RE.FINDALL(), RE.FINDITER()

import re

c="qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
v="aeiouAEIOU"
m=re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c),input())
print('\n'.join(m or ['-1']))

#----------------------------
#4-RE.START(),  RE.END()

import re
s=input()
k=input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')
    


#-----------------------------
#5-VALIDATE A ROMAN NUMBER

regex_pattern = r"^M{,3}(CM|D?C{,3}|CD)(XC|L?X{,3}|XL)(V?I{,3}|I[XV])$"    

import re
print(str(bool(re.match(regex_pattern, input()))))

#------------------------------------
#6-VALIDATING PHONE NUMBER
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
p=[input() for i in range(int(input()))]
regex_pattern = r"^[789][0-9]{9}$"  
for i in range(len(p)):
    if bool(re.match(regex_pattern, p[i])):
        print('YES')
    else:
        print('NO')


#------------------------------------
#7-VALIDATING AND PARSING AN EMAIL

# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re


if __name__=="__main__":
    pattern= r'^<[a-zA-Z]{1}[\w\.\-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$'
    #before a dot what characters can be?
    mails=[]
    for i in range(int(input())):
        mails.append(input().split())
        if bool(re.match(pattern, mails[i][1])):
            mails[i][1]=mails[i][1][1:-1]
            print(email.utils.formataddr(mails[i]))

#-------------------------------------------
#9- DETECT FLOATING POINT NUMBER

import re

if __name__=="__main__":
    pattern= r'[\+\-]?[0-9]*\.[0-9]+$'
    flo=[]
    for i in range(int(input())):
        flo.append(input().split())
        print( bool(re.match(pattern, flo[i][0])))

#------------------------------------------
#10- HEX COLOR CODE

import re

if __name__=="__main__":
    pattern= r'#([a-fA-F0-9]{3}){1,2}'
    tex=[]
    deli = [" ", "#", ":", ";", ")"]
    for i in range(int(input())):
        tex.append(input())
        tex[i] = tex[i].replace(':#', ': #').replace(', ', ' ').replace(");", "").replace(";","").split()
        for j in range(1,len(tex[i])):
            if bool(re.match(pattern, tex[i][j])):
                print(tex[i][j])
        
        

#----------------------------------------------
#11- THMTLParser -PART1

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ("Start :",tag)
        for val in attrs:
            print ("->",val[0],'>',val[1])
            
    def handle_endtag(self, tag):
        print ('End   :',tag)
        
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for val in attrs:
            print ('->', val[0],'>', val[1])
        
if __name__=="__main__":
    parser=MyHTMLParser()
    for i in range(int(input())):
        p = parser.feed(input())
#----------------------------------------
#12-HTML PARSER- Part2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if (len(data.split('\n')) != 1):
            print (">>> Multi-line Comment")
            
        elif (len(data.split('\n')) == 1):
            print (">>> Single-line Comment")
        print(data)
        
    def handle_data(self, data):
        if data.strip():
            print (">>> Data")
            print(data)
  
   
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


#-------------------------------------------
#13-DETECT HTML Tags, Attributes and Attributes Values

from html.parser import HTMLParser
import re

exp = r'^="\w"$'
q=[]
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):    
        q.append(tag)    
        print (tag)
        for val in attrs:
            print ("->",val[0],'>',val[1])
                
        
if __name__=="__main__":
    parser=MyHTMLParser()
    for i in range(int(input())):
        p = parser.feed(input())

#----------------------------------
#14-VALIDATING CREDIT CARDS NUMBERS

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'^[456]\d{3}(-?\d{4}){3}$'
rep = r'.*(\d)-?(\1-?){3}.*'

for i in range(int(input())):
    cid=input()
    cid2=cid
    if re.match(pattern, cid):
        if not re.match(rep, cid2):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")

#-------------------------------------
#15- VALIDATING UID

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern_num=r'[0-9]{3,}.+'
pattern_s = r'.+[A-Z]{2,}.*'

for _ in range(int(input())):
    a=input()
    if len(a)!=10:
        print("Invalid")
        continue
    a=set(a)
    b=''.join(sorted(a))
    if len(a)!=10:
        print("Invalid")
        continue
    if (re.match(pattern_num, b) and b.isalnum() and re.match(pattern_s, b)):
        print("Valid")
    else:
        print("Invalid")
        
        
        
#--------------------------------------
#16-VALIDATING POSTAL CODES

regex_integer_in_range = r'^[1-9][0-9]{5}$'	
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'	

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


#--------------------------------------
#17-MATRIX SCRIPT

#!/bin/python3

import math
import os
import random
import re
import sys


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

delimit = r'[\!\@\#\$\%\&]\ {1,}?'

s=""
for i in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
    #print("La matrice aggiornata",matrix)     
    #print("matrice111", matrix)

for j in range(m):
    for i in range(n):
        s+= matrix[i][j]
        s= ''.join(s)
        #print(s, type(s))
    
pattern = r'(?<=\w)[\!\@\#\$\&\%\ ]+(?=\w)'
print(re.sub(pattern,' ',s))


##############################
##############################
#PYTHON -PY XML - 2
##############################
##############################

#--------------------------------------------
#1-FIND THE SCORE
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    return len(node.attrib) + sum(get_attr_number(child) for child in node)

if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))


#----------------------------------------
#2-FIND THE MAXDEPTH

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if (level==maxdepth):
        maxdepth +=1
    # each time I enter a child i'm advancing 1 level
    for child in elem:
        depth(child, level+1)
    return maxdepth
        

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

###################################
####################################
#PYTHON -CLOSURES AND DECORATORS- 2
##################################
###################################
#-------------------------------------
#1-STANDARDISE MOBILE NUMBER

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            p=[('+91 '+str(l[i][-10:-5])+" "+str(l[i][-5:])) for i in range(len(l))]
            return (f(p))
    return fun
    


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 

#--------------------------------------------------
#2-NAME DIRECTORY

import operator
from operator import itemgetter

def person_lister(f):
    def inner(people2):
        people3=[[l[0],l[1],int(l[2]),l[3]] for l in people2]
        return [f(person) for person in sorted(people3, key=itemgetter(2))]
    return inner
    

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

##############################
##############################
#PYTHON -NUMPY - 15
##############################
##############################

#---------------------------
#1-ARRAYS

import numpy

def arrays(arr):
    s=numpy.array(arr,float)
    return(numpy.flip(s))

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#----------------------------
#2-SHAPE AND RESHAPE

import numpy as np

stri=np.array(input().split(), int)
stri.shape=(3,3)
print(stri)


#---------------------------------
#3-TRANSPOSE AND FLATTEN

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

if __name__=="__main__":
    N, M= map(int,input().split())
    mat=[]
    for i in range(N):
        mat.append(list(map(int,input().split())))
    mat1=np.array(mat)
    mat2=np.transpose(mat1)
    print (mat2)
    print(mat1.flatten())


#-------------------------------------------
#4-CONCATENATE


import numpy as np

if __name__=="__main__":
    N,M,P= map(int, input().split())
    a1= np.array([input().split() for _ in range(N)],int)
    a2= np.array([input().split() for _ in range(M)],int)
    print(np.concatenate((a1, a2), axis = 0))


#--------------------------------------
#5-ZEROS AND ONES
# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

if __name__=="__main__":
    mat=tuple(map(int,input().split()))
    z=np.zeros(mat, dtype=np.int)
    z1=np.ones(mat,dtype=np.int)
    print(z)
    print(z1)



#-------------------------------------------
#6-EYE AND IDENTITY

import numpy as np
np.set_printoptions(legacy='1.13')

if __name__=="__main__":
    N,M=map(int,input().split())
    print(np.eye(N,M,k=0))


#------------------------------------------------
#7-ARRAY MATHEMATICS

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
N,M = map(int,input().split())
a, b = (np.array([input().split() for _ in range(N)], dtype=int) for _ in range(2))
print (np.add(a,b))
print (np.subtract(a,b))
print (np.multiply(a,b))
print (a//b)
print (np.mod(a,b))
print (np.power(a,b))


#---------------------------------------------
#8- FLOOR, CEIL AND RINT

import numpy as np
np.set_printoptions(legacy='1.13')

a=np.array((input().split()),float)
print(np.floor(a), np.ceil(a), np.rint(a), sep="\n")


#---------------------------------------------
#9-SUM AND PROD

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

N, M = map(int, input().split())
lists=[]
for i in range(N):
    new= np.array(input().split(),int)
    lists.append(new)
somma=0
for l in range(M): 
    somma=lists[l]+somma
    #print(somma)
   
print(np.prod(somma))
#factors=list(map(int, input().split())
#for i in range(M):

    


#---------------------------------------------
#10- MIN AND MAX

import numpy as np
np.set_printoptions(legacy='1.13')

N, M= map(int, input().split())
mat = [list(map(int,input().split())) for _ in range(N)]
print(max(np.min(mat,axis=1)))


#--------------------------------------------
#11-MEAN, VAR AND STD

import numpy as np
#np.set_printoptions(legacy='1.13') 

N, M = map(int, input().split())
mat= [list(map(int, input().split())) for _ in range(N)]
print(np.mean(mat, axis=1))
print(np.var(mat, axis=0))
print(round(np.std(mat),11))



#----------------------------------------
#12-DOT AND CROSS

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
np.set_printoptions(legacy='1.13') 

N=int(input())
A = np.array([input().split() for _ in range(N)],int)
B = np.array([input().split() for _ in range(N)],int)
prod = np.dot(A,B)
print (prod)


#------------------------------------------
#13-INNER AND OUTER

import numpy as np

A = np.array(input().split(),int)
B = np.array(input().split(),int)
print(np.inner(A, B))
print(np.outer(A, B))




#-------------------------------------
#14-POLYNOMIALS

import numpy as np

coeff = np.array(input().split(),float)
num=float(input())
print(np.polyval(coeff, num))

    
#----------------------------------
#15-LINEAR ALGEBRA

# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
np.set_printoptions(legacy='1.13')

N = int(input())
#if N ==1:
#    elem=int(input)
#    print(elem)
if N>1:
    mat =[ list(map(float,input().split())) for _ in range(N)]
    #print("matrice quadrata:", mat)
    det = np.linalg.det(mat)
    print(det)
