# This programs has implementation of two algorithms:
# linear search and binary search ...
#KINGSLEY OTTO
#CSI 33

from time import time

def linear_search(items,target):  
  i = 0
  while i < len(items): #iterate over the number of numbers in the list
    if items[i] == target: 
      return i
    i += 1
  return -1

def binary_search(items,target):
  
  low = 0
  high = len(items) - 1
  while low <= high:
    mid = (low + high) // 2 
    item = items[mid]
    if target == item :
      return mid
    elif target < item:
      high = mid - 1
    else:
      low = mid + 1
  return -1

 

 

def main():
  numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999
  

  start = time()
  linear_search(numbers,10)
  end = time()
  
  print("first linear search in secs: ",end - start)

  start = time()
  linear_search(numbers,499999)
  end = time()
  
  print ("Second linear search in secs: ",end - start)

  start = time()
  linear_search(numbers,999999)
  end = time()
  
  print ("Third linear search in secs",end - start)

  #do the same for binary search
  numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999
  
  start = time()
  binary_search(numbers,10)
  end = time()
  
  print("first binary search in secs: ",end - start)

  start = time()
  binary_search(numbers,10)
  end = time()
  
  print ("Second binary search in secs: ",end - start)

  start = time()
  binary_search(numbers,10)
  end = time()
  
  print ("Third binary search in secs: ",end - start)

main()

"""
first linear search in secs:  0.0
Second linear search in secs:  0.09803104400634766
Third linear search in secs 0.20906615257263184


first binary search in secs:  0.0
Second binary search in secs:  0.0
Third binary search in secs:  0.0

"""
