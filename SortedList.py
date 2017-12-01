
#KINGSLEY OTTO
#CSI 33
#This program sorts a list by finding the smallest element and swapping
#it with the element in position zero of the list.It then finds the next
#smallest element and swaps it with the element in position one of the list.
#This process repeats until we have found the n -1 th smallest element and
#put it in position n - 2. At this point, the largest element is in position n - 1.

from time import time

def SelectionSort(List):
    """Sorts a list of items into ascending order using the
       selection sort algorighm."""
     
    for loc in range(len(List)):
        # Find the location of the smallest element in a list
        
        smallestLoc = loc
        for location in range(loc, len(List)):
            # determine location of smallest
            if List[location] < List[smallestLoc]:
                smallestLoc = location
        # Exchange List[loc] with list[smallestLoc]
        temp = List[loc]
        List[loc] = List[smallestLoc]
        List[smallestLoc] = temp

def main():
    List = [2500,60000,3000,45,1,15,88,69,745,852,10000,5546,8743,5,436,735]
    print("[unsorted list]")
    print(List)
    print()
    print("[Sorted list]")
    start = time()
    SelectionSort(List)
    end = time()
    print(List)
    print()
    print("Time taken to sort out list: ",end - start)

main()

"""
[unsorted list]
[2500, 60000, 3000, 45, 1, 15, 88, 69, 745, 852, 10000, 5546, 8743, 5, 436, 735]

[Sorted list]
[1, 5, 15, 45, 69, 88, 436, 735, 745, 852, 2500, 3000, 5546, 8743, 10000, 60000]

Time taken to sort out list:  0.0
Classification is (Θ(n^2))
"""

