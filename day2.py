infile = open("day2.txt")
safe = 0

def levelsafe(diffs):
    if(min(diffs)>0):
        if(max(diffs)<=3):
            return True
    if(max(diffs)<0):
        if(min(diffs)>=-3):
            return True
    return False

def calcdiffs(nums):
    diffs = [nums[i+1]-nums[i] for i in range(len(nums)-1)]
    return diffs

for line in infile:
    nums = [int(n) for n in line.strip().split()]
    diffs = calcdiffs(nums)
    lsafe = levelsafe(diffs)
    for i in range(len(nums)):
        if(not lsafe):
            n2 = [nums[j] for j in range(len(nums)) if(j!=i)]
            diffs = calcdiffs(n2)
            lsafe = levelsafe(diffs)
    safe+=lsafe
print(safe)