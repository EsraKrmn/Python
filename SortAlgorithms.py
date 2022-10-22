'''
Complexity test of sort algorithms.
'''
import random
import string
import time
import heapq

#Generate an array of random entries. (n ∈ ℤ and n ≥ 1) (tflag ∈ {0,1,2}: 0=string (default), 1=integer, 2=float) (wmax > wmin ≥ 1: default values wmin=1, wmax=10)
def Generaterandomarray(n,wmin=1,wmax=10,tflag=0):
    ls = []
    sl= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    if tflag == 0:
        for i in range(n):
            strl = random.randint(wmin, wmax)
            strings=''.join(random.choices(string.ascii_letters+string.digits,k=strl))
            if len(ls)!=n:
                ls.append(strings)
        return ls
            
    if tflag == 1:
        for i in range(n):
            values = random.randint(wmin,wmax)
            ls.append(values)
        return ls
    
    if tflag == 2:
        for i in range(n):
            ls.append(random.uniform(wmin, wmax))
        return ls

#Insertion Sort by pair wise swaps. (rl: a list)    
def Insertionsortbyswaps(rl):
    time1= time.perf_counter_ns()
    N = len(rl)
    for i in range(1,N):
        j = i
        while (j > 0 and rl[j] < rl[j - 1]):
            temp = rl[j]
            rl[j] = rl[j - 1]
            rl[j-1] = temp
            j -= 1
    time2= time.perf_counter_ns()
    return time2-time1

#Insertion Sort by pair wise comp. & pop/insert.
def Insertionsortbypopinsert(rl):
    time1= time.perf_counter_ns()
    N = len(rl)
    for i in range(1,N):
        j = i
        while (j > 0 and rl[j] < rl[j - 1]):
            temp=rl[j]
            rl.pop(j)
            rl.insert(j-1,temp)
            j -= 1
    time2= time.perf_counter_ns()
    return time2-time1   

#Insertion Sort by binary search.
def InsertionsortbyBS(rl):
    time1 =time.perf_counter_ns()
    def binary_search(rl, val, start, end):
        for i in range(len(rl)):
             for j in range(len(rl) - 1):
                 if rl[j] > rl[j+1]:
                    rl[j], rl[j+1] = rl[j+1], rl[j]
        if start == end:
            if rl[start] > val:
                return start
            else:
                return start+1
        if start > end:
            return start
        mid = (start+end)//2
        if rl[mid] < val:
            return binary_search(rl, val, mid+1, end)
        elif rl[mid] > val:
            return binary_search(rl, val, start, mid-1)
        else:
            return mid
    for i in range(1, len(rl)):
        val = rl[i]
        j = binary_search(rl, val, 0, i-1)
        rl = rl[:j] + [val] + rl[j:i] + rl[i+1:]
    time2=time.perf_counter_ns()
    return time2-time1

#Merge Sort.
def MergeSort(rl):
    time1 =time.perf_counter_ns()
    rl.sort()
    time2=time.perf_counter_ns()
    return time2-time1
    
#Heap Sort.
def HeapSort(rl):
    time1= time.perf_counter_ns()
    h = []
    for value in rl:
        heapq.heappush(h, value)
    time2= time.perf_counter_ns()
    return [heapq.heappop(h) for i in range(len(h))], time2-time1