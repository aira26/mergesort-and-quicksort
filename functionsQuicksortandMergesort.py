import random

a = random.sample(range(1000), 600)  # generating a random list


# MergeSort divide and conquer


def mergeSort(lst):
    if len(lst) > 1:
        middle = len(lst) // 2        #this means splitting the list we have in two and then starting to sort them
        left1 = lst[:middle]           #depending on their integer value
        right1 = lst[middle:]

        mergeSort(left1)
        mergeSort(right1)

        i = 0
        j = 0
        k = 0

        while i < len(left1) and j < len(right1):
            if left1[i] < right1[j]:
                lst[k] = left1[i]
                i = i + 1
            else:
                lst[k] = right1[j]
                j = j + 1
            k = k + 1

        while i < len(left1):
            lst[k] = left1[i]
            i = i + 1
            k = k + 1

        while j < len(right1):
            lst[k] = right1[j]
            j = j + 1
            k = k + 1

    return (lst)


# QuickSort

def quickSort(lst):
    if len(lst) > 1:
        pivot = lst[0]           # This function takes last element as pivot
        left2 = []
        right2 =[]
        for i in range(1, len(lst)):       #the pivot element at its correct position in sorted array, and places all smaller elements
                                            #  (smaller than pivot) to left of pivot and all greater elements to right of pivot
            if (lst[i] < pivot):
                left2.append(lst[i])

            else:
                right2.append(lst[i])
        return quickSort(left2) + [pivot] + quickSort(right2)

    else:
        return lst


print(quickSort(a))
print(mergeSort(a))


