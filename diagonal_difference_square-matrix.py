n =int(input());

arr = []
 
for i in range(0,n):
    arr_item = list(map(int, input().split()))
    arr.append(arr_item)
    




sum1 = 0;
sum2 = 0;
l = n - 1
g =0;

while g < n and l >=0:
#     print(arr[g][g]);
#     print(arr[g][l]);
    
    sum1 += arr[g][g]
    sum2 += arr[g][l]
    l = l - 1;
    g = g + 1;


print(abs(sum1 - sum2))