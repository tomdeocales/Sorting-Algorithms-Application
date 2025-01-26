import array

def insertionsort(arr): 
  
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 

a = array.array('i', [])

print ("\n---------------\nInsertion Sort\n---------------")
n = int(input('\nEnter  size of Array='))

for i in range(n):
    item= int(input("Enter number in array:"))
    a.append(item)


insertionsort(a)


print ("Sorted array is:")
for i in a:
    print (i, '\t')
    continue
