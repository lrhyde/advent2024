infile = open("day5.txt")
predecessors = dict()
s = 0
for line in infile:
    if("|" in line):
        nums = line.strip().split("|")

        if(nums[1] in predecessors):
            predecessors[nums[1]].append(nums[0])
        else:
            predecessors[nums[1]] = [nums[0]]
    elif("," in line):
        nums = line.strip().split(",")
        isValid = True
        prevs = []
        for i in range(len(nums)):
            if(nums[i] in predecessors):
                for p in predecessors[nums[i]]:
                    if(p in nums and p not in nums[:i]):
                        isValid = False
                        break
                if(not isValid):
                    break
        if(isValid):
            s+=int(nums[int((len(nums)-1)/2)])
print(s)