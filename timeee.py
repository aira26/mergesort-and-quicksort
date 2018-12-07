import timeit

setup = """

from functionsQuicksortandMergesort import quickSort
from functionsQuicksortandMergesort import mergeSort


import random 
myrandom1= random.sample(range(50), 10)                    
myrandom2= random.sample(range(500), 100)
myrandom3= random.sample(range(5000), 1000)
myrandom4= random.sample(range(50000), 10000)


"""
# we use setup because its the correct installation of the software/ function and packages we are using and then,
### import the functions inside the setup and lastly we measure the efficiency of both of the functios that we imported and compare :)



t1= timeit.Timer('quickSort(myrandom1)', setup = setup)
t2= timeit.Timer('mergeSort(myrandom1)', setup = setup)
t3= timeit.Timer('quickSort(myrandom2)', setup = setup)
t4= timeit.Timer('mergeSort(myrandom2)', setup = setup)
t5= timeit.Timer('quickSort(myrandom3)', setup = setup)
t6= timeit.Timer('mergeSort(myrandom3)', setup = setup)
t7= timeit.Timer('quickSort(myrandom4)', setup = setup)
t8= timeit.Timer('mergeSort(myrandom4)', setup = setup)

print('quickSort time:', t1.timeit(5))
print('mergeSort time:', t2.timeit(5))
print(t3.timeit(5))
print(t4.timeit(5))
print(t6.timeit(5))
print(t5.timeit(5))
print(t7.timeit(5))
print(t8.timeit(5))

import matplotlib.pyplot as plt

plt.plot([0.0004697080000000131, 0.006510414999999936, 0.17511782500000006, 1.402740026], 'bo-', label= 'QuickSort')

plt.plot([ 0.0007822230000000263, 0.011975684000000042, 0.09060686899999992, 2.0248449360000005], 'ro-', label='MergeSort')
plt.legend()

plt.grid()
plt.xlabel("t1 , t2 , t3 , t4 , t5 , t6 , t7 , t8")
plt.ylabel("time in sec")
plt.title("Difference between QuickSort and MergeSort")
plt.show()

plt.savefig('plot')

 # we conclude that quicksort is much faster than mergesort
