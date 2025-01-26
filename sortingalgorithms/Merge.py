import array 

def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        mid = len(unsorted_array) // 2  # Finding the mid of the array
        left = unsorted_array[:mid]  # Dividing the array elements
        right = unsorted_array[mid:]  # into 2 halves

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        #  data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1
            k += 1


a = array.array('i', [])
print ("\n---------------\nMerge Sort\n---------------")
n = int(input('\nEnter  size of Array='))

for i in range(n):
    item= int(input("Enter number in array:"))
    a.append(item)

merge_sort(a)

print ("Sorted array is:")
for i in a:
    print (i, '\t')