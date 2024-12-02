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

# part 2:
# This time, you'll need to figure out exactly how often each number from the left list appears in the right list. 
# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number 
# of times that number appears in the right list.

similarities = [item * list2.count(item) for item in list1]
print(sum(similarities))