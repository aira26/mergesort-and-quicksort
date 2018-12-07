# mergesort-and-quicksort
<br>
This is my codes for quick sort and merge sort and, the differnce of the timing between them !<br>
<br>
![graph](https://github.com/aira26/mergesort-and-quicksort/blob/master/mergequick.png) 
<br> <br>

As we can see I first made my random list by importing random to see if everytime we get the same timing using both of the functions.<br>
Then, I applied the function Merge Sort, which is a way of "divide and conquer", it divides the list of bunch of numbers that i randomly chose in two smaller halves, and then keep doing that recursively, and for the two halves at last to reach only one number and then merges the sorted parts to get my final list. BUT the problem with this one is that it takes lots of memory! but MergeSort is better for large data <br> 

Quick Sort on the other hand, is also a "divide and conquer" function but, it picks the random list that we already talked about, and then picks an element as pivot which is a central element on small values on the left for example and another big element on the right and start swapping and partitions the other numbers of the list around the picked pivot, until it reachs the right order. But QuickSort can skip some swaps.<br>

Finally, I used timeit by first importing it and then I used the setup function, which is the right way to import other function, a way of ordering them and using them all in the correct way. And then I measured the time between both of QuickSort and MergeSort and What we can notice is that QuickSort is Faster than MergeSort and that’s also what we can see in the graph, where MergeSort took more time to do it’s job, but that doesn’t mean it’s better because in one of the times we had QuickSort was slower than MergeSort on point(2.0, 0.0905), where it was a worst case of quicksort where merge sort was faster than it, because MergeSort is better for large data. <br>


 But in conclusion QuickSort is faster due to the fact that it takes less memory/space than MergeSort.
