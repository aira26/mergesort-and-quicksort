# mergesort-and-quicksort
#Hello, i’m aia rahim 
#Matricola 1804936
#This is my codes for quick sort and merge sort and the differe of the timing ! 
#As we can see I first made my random list by importing random 
##Then, I applied the function Merge Sort, which is a way of divide and conquer, it divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. BUT the problem with this one is that it takes lots of memory!
##Quick Sort on the other hand, is also a divide and conquer function but, it picks an element as pivot and partitions the given array around the picked pivot.
##We start from the leftmost element and keep track of index of smaller (or equal to) elements as i. While traversing, if we find a smaller element, we swap current element with arr[i].
######Finally, I used timeit by first importing it and then I used the setup function, which is the right way to import other function, a way of ordering them and using them all in the correct way. And then I measured the time between both of QuickSort and MergeSort and What we can notice is that QuickSort is Faster than MergeSort and that’s also what we can see in the graph, where MergeSort took more time to do it’s job, but that doesn’t mean it’s better because in one of the times we had QuickSort was slower than MergeSort .. which was the worst case for QuickSort, because MergeSort is better for large data.
#But in conclusion QuickSort is faster due to the fact that it takes less memory/space than MergeSort.
