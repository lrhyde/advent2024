mem = open("day3.txt").read()
muls = mem.split("mul(")
muls = muls[1:]
s = 0
future_do = True
for m in muls:
    do = future_do
    if(m.rfind("don't()")>m.rfind("do()")):
        future_do = False
    elif(m.rfind("don't()")<m.rfind("do()")):
        future_do = True
    nums = m.split(")")[0]
    n = nums.split(",")
    if(len(n)!=2):
        continue
    if(not do):
        continue
    if(len(n[0])<4 and len(n[1])<4):
        if(n[0].strip()==n[0] and n[1].strip()==n[1]):
            if(n[0].isdigit() and n[1].isdigit()):
                print(n)
                s+=int(n[0])*int(n[1])
print(s)