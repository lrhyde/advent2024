infile = open("day1.txt")
list1 = []
list2 = []
for line in infile:
    nums = line.strip().split()
    list1.append(int(nums[0]))
    list2.append(int(nums[-1]))
list1 = sorted(list1)
list2 = sorted(list2)
diffs = [abs(list1[i] - list2[i]) for i in range(len(list1))]
print(sum(diffs))