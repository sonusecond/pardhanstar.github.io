# 1st program 
num_str = input()
num = num_str.split()
lis = []
for n in num:
    if(str(n)[-1] != '4'):
        lis.append(n)
print(*lis)

# 2nd program 
nums = input()
num = nums.split()
lis = []
for n in num:
    if n not in lis:
        lis.append(n)
for i in range(0,len(lis)):
    lis[i] = int(lis[i])
if(len(lis)>=2):
    lis.remove(min(lis))
    lis.remove(max(lis))
    print(min(lis)+max(lis),end="")
else:
    print(lis[0]+lis[0],end="")

# 3rd program 
nums = input()
num = nums.split()
lis = []
for n in num:
    if n not in lis:
        lis.append(n)
for i in range(0,len(lis)):
    lis[i] = int(lis[i])
print(*lis)