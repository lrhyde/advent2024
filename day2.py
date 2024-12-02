infile = open("day2.txt")
safe = 0
for line in infile:
    nums = [int(n) for n in line.strip().split()]
    diffs = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
    if(min(diffs)>0):
        if(max(diffs)<=3):
            safe+=1
    if(max(diffs)<0):
        if(min(diffs)>=-3):
            safe+=1
print(safe)