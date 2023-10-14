##############################
##############################
#ALGORITHMS- 6
##############################
##############################
#---------------------------------
#1-BIRTHDAY CAKE CANDLES

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#
from collections import Counter

def birthdayCakeCandles(candles):
    # Write your code here
    total=Counter(candles).values()
    return(max(total))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()


#---------------------------------
#2- KANGAROO

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if x2>x1 and v2>=v1:
        return("NO")
    if x1>x2 and v1>v2:
        return("NO")
    t=1
    while t<10000:
        if x1-x2==(v2-v1)*t:
            return("YES")
        t+=1
    return("NO")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#---------------------------------
#3-VIRAL ADVERTISING

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    shared=[5]
    liked=[2]
    cumulative=[2]
    for i in range(1,n):
        #print("contatore:", liked)
        #print("cumulativa:", sum(liked))
        shared.append((int(liked[i-1])*3))
        liked.append(int(shared[i])//2)
        cumulative.append(int(liked[i])+int(cumulative[i-1]))
        #print("condiviso ora a:", shared[i], "persone")
    return(cumulative[i])
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#---------------------------------
#4- RECURSIVE DIGIT SUM

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#
def somma1(p):
    res=0
    for number in range(len(p)):
        res+= int(p[number])
    return(res)

def superDigit(n, k):
    # Write your code here
    p=str(somma1(n)*k)
    while len(p)>1:
        p=str(somma1(p))
    return(int(p))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#---------------------------------
#5- INSERTIONSORT1

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def printarray(a):
    a=str(a)[1:-1]
    a=a.split(", ")
    a=" ".join(a)
    print(a)

def insertionSort1(n, arr):
    # Write your code here
    if n==1:
        print(arr[0])
    else:
        store=arr[n-1]
        if n==2:
            if arr[0]>arr[1]:
                arr[1]=arr[0]
                arr[0]=store
            printarray(arr)
        else:
            arr[-1]=arr[-2]
            for i in range(1,n):
                if store<arr[-i-1]:
                    arr[-i]=arr[-i-1]
                    printarray(arr)
                    if i==(n-1):
                        arr[0]=store
                        printarray(arr)
                else:
                    arr[-i]=store
                    printarray(arr)
                    break
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#---------------------------------
#6-INSETIONSORT2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def printarray(a):
    a=str(a)[1:-1]
    a=a.split(", ")
    a=" ".join(a)
    print(a)

def insertionSort1(n, arr):
    # Write your code here
    if n>1:
        store=arr[n-1]
        if n==2:
            if arr[0]>arr[1]:
                arr[1]=arr[0]
                arr[0]=store
        else:
            arr[-1]=arr[-2]
            for i in range(1,n):
                if store<arr[-i-1]:
                    arr[-i]=arr[-i-1]
                    if i==(n-1):
                        arr[0]=store
                else:
                    arr[-i]=store
                    break
    return(arr)
                
def insertionSort2(n, arr):
    if n==1:
        print(arr[0])
        return
    a=arr
    #printarray(a)
    for i in range(1,n):
        b=insertionSort1(i+1,a[:i+1])
        b= b + a[i+1:]
        printarray(b)
        a=b
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)






