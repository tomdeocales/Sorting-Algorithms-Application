nums = []
print ("\n---------------\nSelection Sort\n---------------")
print("\nEnter the size of elements: ", end="")
tot = int(input())
print("Enter", tot, "numbers: ", end="\n")
for i in range(tot):
  nums.append(int(input()))

for i in range(tot-1):
    chk = 0
    small = nums[i]
    for j in range(i+1, tot):
        if small > nums[j]:
            small = nums[j]
            chk = chk + 1
            index = j
    if chk != 0:
        temp = nums[i]
        nums[i] = small
        nums[index] = temp

print("\nSorted List is: ", end="")
for i in range(tot):
    print(nums[i], end=" ")