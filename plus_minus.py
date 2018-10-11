n = int(input())
arr= list(map(int, input().rstrip().split() ))
no_0 = 0
no_plus = 0
no_minus= 0
for i in arr:
    if i == 0:
        no_0 += 1;
    elif i < 0:
        no_minus += 1;
    else:
        no_plus +=1
zero_ratio = float(no_0 / n)
plus_ratio = float(no_plus / n)
minus_ratio = float(no_minus /n)
print(plus_ratio)
print(minus_ratio)
print(zero_ratio)